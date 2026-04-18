# Constitution Guide

How to create and maintain a project constitution — the document that captures non-negotiable rules, conventions, and architectural decisions that every spec inherits automatically.

## Table of Contents
- [What is a Constitution](#what-is-a-constitution)
- [When to Create One](#when-to-create-one)
- [Constitution vs Spec](#constitution-vs-spec)
- [Maintaining the Constitution](#maintaining-the-constitution)

---

## What is a Constitution

A constitution is a project-level file that captures decisions that apply to ALL features, not just one. It prevents repetition across specs and ensures consistency when multiple agents or developers work on the same codebase.

Common names for this file:
- `constitution.md` (GitHub Spec Kit convention)
- `GEMINI.md` (Gemini CLI)
- `CLAUDE.md` (Claude Code)
- `.cursorrules` (Cursor)
- `CONVENTIONS.md` (general)
- `AGENTS.md` (multi-agent projects)

The SDD skill reads any of these automatically during Context Scan.

---

## When to Create One

Create a constitution when:
- Starting a new project (invest 15 minutes now, save hours later)
- Multiple specs are repeating the same constraints
- New team members keep asking "how do we do X here?"
- The project has non-obvious conventions that aren't self-evident from the code

Don't create one for throwaway prototypes or single-file scripts.

---

## Constitution vs Spec

| Aspect | Constitution | Spec |
|--------|-------------|------|
| Scope | Entire project | Single feature |
| Lifespan | Long-lived, evolves slowly | Created per feature, archived after delivery |
| Content | Conventions, standards, constraints | Requirements, design, tasks |
| Changes | Require team consensus | Author decides |
| Inheritance | Specs inherit from constitution | Specs don't inherit from each other (unless explicit) |

---

## Maintaining the Constitution

The constitution is a living document. Update it when:

1. **New architectural decision:** Add it immediately. "We chose PostgreSQL over MongoDB because of relational integrity requirements."
2. **Pattern emerges:** If three specs use the same approach, promote it to the constitution.
3. **Anti-pattern discovered:** Add to "Don't" section. "Don't use global state for form data — use React Hook Form with controlled inputs."
4. **Dependency change:** When a major dependency is added or removed, update the relevant sections.

Review the constitution quarterly or when major features ship. Remove outdated entries — a constitution with stale rules erodes trust.

Use `templates/constitution-template.md` for the starting structure.
