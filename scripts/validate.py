"""Validate the public vault using Python 3.10+ and no third-party packages.

Checks local structure and selected leakage patterns; not an exhaustive secret
scanner, external link checker, package audit or React runtime test.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote,urlparse
import xml.etree.ElementTree as ET


def inspect_text(text,display_path):
    rules={
        'machine path':r'(?:[A-Za-z]:\\|/(?:Users|home)/)[^\s`<>]+',
        'credential-shaped value':r'\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{35,}|sk-proj-[A-Za-z0-9_-]{20,}|AKIA[0-9A-Z]{16})\b',
        'private key block':r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
    }
    return [f'{display_path}: {name}' for name,pattern in rules.items() if re.search(pattern,text)]


def resolve_local_link(root,origin,target):
    target=target.strip('<>')
    if urlparse(target).scheme or target.startswith('#'):return None
    destination=(origin.parent/unquote(target.split('#')[0].split('?')[0])).resolve()
    if not destination.is_relative_to(root.resolve()):raise ValueError('link escapes repository')
    return destination


def check_source_bytes(record,raw):
    git_blob=hashlib.sha1(f'blob {len(raw)}\0'.encode()+raw).hexdigest()
    return git_blob==record['sha'] and hashlib.sha256(raw).hexdigest()==record['sha256'] and len(raw)==record['size']


def validate(root):
    root=root.resolve();vault=root/'vault';errors=[];link_count=0;hash_count=0
    files=[p for p in root.rglob('*') if p.is_file() and not any(x in p.relative_to(root).parts for x in ['.git','__pycache__'])]
    required=['README.md','LICENSE','THIRD_PARTY_NOTICES.md','CONTRIBUTING.md','SECURITY.md','CHANGELOG.md','AGENTS.md','vault/AGENT START.md','vault/START HERE.md','docs/catalogue.json']
    for name in required:
        if not (root/name).is_file():errors.append(f'Missing required file: {name}')
    md=[p for p in files if p.suffix=='.md']
    authored=[p for p in md if vault in p.parents and 'React Snapshot' not in p.parts]
    seen=set()
    for p in files:
        relative=p.relative_to(root).as_posix()
        if relative.casefold() in seen:errors.append(f'Case-insensitive path collision: {relative}')
        seen.add(relative.casefold())
        if p.is_symlink():errors.append(f'Symlink is not part of this distribution: {relative}')
        if p.name in {'workspace.json','community-plugins.json','auth.json','.env'} or p.suffix in {'.pem','.key','.pfx','.p12'}:errors.append(f'Private/local file must not ship: {relative}')
        if p.suffix in {'.md','.json','.svg','.tsx','.ts','.css'}:
            text=p.read_text(encoding='utf-8')
            errors.extend(inspect_text(text,relative))
        if p.suffix=='.json':
            try:json.loads(p.read_text(encoding='utf-8'))
            except (ValueError,UnicodeError) as exc:errors.append(f'Invalid JSON {relative}: {type(exc).__name__}')
    for p in authored:
        text=p.read_text(encoding='utf-8')
        if not text.startswith('---\n') or not re.search(r'^updated: \d{4}-\d{2}-\d{2}$',text,re.M):errors.append(f'Missing note metadata: {p.relative_to(root)}')
        if re.search(r'\[\[[^\]]+\]\]',text):errors.append(f'Nonportable wiki link: {p.relative_to(root)}')
    for p in md:
        if 'React Snapshot' in p.parts:continue
        text=p.read_text(encoding='utf-8')
        targets=re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',text)+re.findall(r'(?:href|src|srcset)="([^"]+)"',text)
        for target in targets:
            if '"' in target:target=target.split('"')[0].strip()
            try:dest=resolve_local_link(root,p,target)
            except ValueError:errors.append(f'Escaping link in {p.relative_to(root)}');continue
            if dest is None:continue
            link_count+=1
            if not dest.is_file():errors.append(f'Broken link: {p.relative_to(root)} -> {target}')
    source=vault/'90 Sources'/'React Snapshot'
    manifest=json.loads((source/'manifest.json').read_text(encoding='utf-8'))
    for record in manifest['files']:
        p=(source/record['name']).resolve()
        if not p.is_relative_to(source.resolve()):errors.append('Source manifest escapes its directory');continue
        if not p.is_file() or not check_source_bytes(record,p.read_bytes()):errors.append(f'Source integrity mismatch: {record["name"]}')
        hash_count+=1
    if 'Copyright (c) 2023 shadcn' not in (source/'LICENSE.md').read_text(encoding='utf-8'):errors.append('Upstream copyright notice missing')
    if 'Permission is hereby granted' not in (root/'LICENSE').read_text(encoding='utf-8'):errors.append('Root MIT license missing')
    if any((vault/'90 Sources'/name).exists() for name in ['Design Taste Source.md','UI UX Source.md']):errors.append('Local skill archive must not ship')
    actual={'authored_notes':len(authored),'genres':len(list((vault/'02 Genres').glob('*.md')))-1,'react_components':len(list((source/'ui').glob('*.tsx'))),'usage_examples':len(list((source/'examples').glob('*.tsx'))),'library_profiles':len(list((vault/'04 React'/'Libraries').glob('*.md')))}
    stats=json.loads((root/'docs'/'catalogue.json').read_text(encoding='utf-8'))
    for key,value in actual.items():
        if stats.get(key)!=value:errors.append(f'Catalogue count mismatch: {key}')
    if len(list((vault/'04 React'/'Components').glob('*.md')))!=actual['react_components']:errors.append('Source/card coverage mismatch')
    entry_words=sum(len(p.read_text(encoding='utf-8').split()) for p in [vault/'AGENT START.md',vault/'01 Foundations'/'Core Design Rules.md'])
    if entry_words>800:errors.append('Entry/core exceeds 800-word budget')
    for p in (root/'docs'/'assets').glob('*.svg'):
        try:
            element=ET.parse(p).getroot()
            for child in element.iter():
                if child.tag.split('}')[-1] in {'script','foreignObject','animate','animateTransform'}:errors.append(f'Unsafe/animated SVG element: {p.name}')
                for attr,value in child.attrib.items():
                    if attr.lower().startswith('on') or (attr.split('}')[-1] in {'href','src'} and not value.startswith('#')):errors.append(f'External/active SVG attribute: {p.name}')
        except ET.ParseError:errors.append(f'Invalid SVG: {p.name}')
    return {'status':'PASS' if not errors else 'FAIL','files':len(files),'notes':len(authored),'local_links':link_count,'source_hashes':hash_count,'entry_core_words':entry_words,'catalogue':actual,'errors':errors,'limits':'Selected public-sharing patterns and local integrity only. No external-link, React runtime or complete security audit.'}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    args=parser.parse_args();report=validate(args.root)
    print(json.dumps(report,indent=2));raise SystemExit(0 if report['status']=='PASS' else 1)
