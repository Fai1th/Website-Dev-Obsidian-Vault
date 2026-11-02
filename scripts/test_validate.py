"""Regression checks for public-sharing guardrails (standard library only)."""
import hashlib
from pathlib import Path
import unittest

from validate import check_source_bytes, inspect_text, resolve_local_link


class SharingGuardrails(unittest.TestCase):
    def test_security_guidance_is_not_mistaken_for_a_secret(self):
        self.assertEqual(inspect_text('Keep API tokens out of .env files committed to Git.', 'guide.md'), [])

    def test_personal_windows_path_is_flagged_without_echoing_content(self):
        result=inspect_text('Source: '+chr(67)+':'+chr(92)+'Users'+chr(92)+'example'+chr(92)+'notes', 'guide.md')
        self.assertTrue(any('machine path' in x for x in result))
        self.assertTrue(all('example' not in x for x in result))

    def test_token_shape_is_flagged(self):
        fake='gh'+'p_'+'x'*36
        self.assertTrue(inspect_text(fake,'guide.md'))

    def test_relative_links_resolve_spaces(self):
        root=Path(__file__).resolve().parent
        self.assertEqual(resolve_local_link(root,root/'README.md','A%20Note.md'),root/'A Note.md')

    def test_relative_links_cannot_escape_repository(self):
        root=Path(__file__).resolve().parent
        with self.assertRaises(ValueError):resolve_local_link(root,root/'README.md','../outside.md')

    def test_modified_source_is_rejected(self):
        raw=b'original\n'
        record={'sha':hashlib.sha1(b'blob 9\0'+raw).hexdigest(),'sha256':hashlib.sha256(raw).hexdigest(),'size':len(raw)}
        self.assertTrue(check_source_bytes(record,raw))
        self.assertFalse(check_source_bytes(record,b'changed\n'))


if __name__=='__main__':unittest.main()
