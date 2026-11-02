---
title: "Forms and Validation"
type: pattern
status: proposed
updated: 2026-11-02
tags: []
---

# Forms and Validation

Give every input a persistent visible label and suitable autocomplete/input mode. Use native controls when they satisfy the task. Explain requirements before submission; associate hints and errors with their fields.

Define initial, editing, validating, submitting, success and failure states. Preserve values after recoverable errors. Make duplicate submission behavior intentional; reflect progress and prevent accidental repeated operations. Server validation remains authoritative.

Use validation timing that helps users complete the task. Avoid error messages before a person has had a reasonable chance to enter information. On failed submission, summarize errors and move focus appropriately; connect each message to its input.

A date-only value is not a timestamp. Choose the locale, timezone, parsing rules, allowed range and serialization deliberately. Format money with currency and locale. Do not restrict names with simplistic assumptions.

Check keyboard-only operation, autofill, paste, password managers, long input, empty input, slow network, server rejection and retry. File pickers require separate server-side upload controls.

React candidates: [React - field](../04%20React/Components/React%20-%20field.md), [React - input](../04%20React/Components/React%20-%20input.md), [React - select](../04%20React/Components/React%20-%20select.md), [React - combobox](../04%20React/Components/React%20-%20combobox.md), [React - calendar](../04%20React/Components/React%20-%20calendar.md), [React Hook Form](../04%20React/Libraries/React%20Hook%20Form.md), [Zod](../04%20React/Libraries/Zod.md).
