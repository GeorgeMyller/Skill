---
name: spec-driven-dev
description: "Spec-Driven Development for AI coding agents. Structure software implementation through formal specifications before writing code. Use whenever the user wants to build a new feature, implement a complex change, plan before coding, create a specification, needs architecture for AI-assisted development, mentions 'spec', 'SDD', 'spec-driven', 'specification', 'plan before code', 'requirements first', or asks to build anything non-trivial — even if they don't say 'spec-driven' explicitly. Also activate for refactors, migrations, or multi-file changes where a plan would prevent rework."
category: code
compatible_with: [Claude Code, Gemini CLI, Cursor, Codex CLI]
tags: [specification, planning, architecture, implementation, ai-agents, requirements, sdd]
version: "1.0.0"
---

# Spec-Driven Development (SDD)

Transform how AI coding agents build software by specifying intent before implementation. Instead of iterative "vibe-coding" where you prompt and pray, SDD provides agents with structured blueprints that eliminate ambiguity, prevent scope creep, and produce code that aligns with your actual goals on the first attempt.

The core insight: AI agents are pattern matchers that struggle with vague prompts. Formal specs give them the context and constraints they need to produce reliable, maintainable code.

## When to Use

Activate this skill when:
- Building new features, components, or modules
- Refactoring or migrating existing code
- Making multi-file changes with architectural impact
- The user asks to "plan", "spec", "architect", or "design" something
- A task is complex enough that a wrong implementation would waste time
- The user wants to ensure AI-generated code matches their intent

Do **not** force full spec workflow for trivial tasks — the Smart Triage handles this automatically.

## Workflow Overview

The workflow adapts its rigor to task complexity through Smart Triage:

```
User Prompt → Smart Triage → [nano | mini | full]
                                 ↓
              nano: Execute directly (zero overhead)
              mini: Generate inline spec → Review → Implement
              full: Spec Interview → SPEC.md + design.md + tasks.md → Review → Implement
                                 ↓
                    Spec Diffing → Feedback Loop
```

---

## Step 1: Smart Triage

Analyze the user's request and classify it into one of three levels. The goal is proportional rigor — never impose more process than the task warrants.

### Classification Rules

| Level | When | Examples | Spec Artifact |
|-------|------|----------|---------------|
| **Nano** | Single-file, low-risk, obvious intent | Fix typo, rename variable, adjust CSS, add comment, bump version | None — execute directly |
| **Mini** | Multi-step but bounded scope | Add pagination, implement dark mode toggle, add form validation, create new endpoint | Inline spec (5-10 bullets + acceptance criteria) |
| **Full** | Architectural impact, multi-file, complex domain | Rebuild auth system, add real-time features, payment integration, database migration | Full spec package (requirements + design + tasks) |

### Triage Signals

Lean toward **Full** when you detect:
- Multiple files or modules affected
- New dependencies or infrastructure changes
- Security-sensitive features (auth, payments, PII)
- Cross-cutting concerns (logging, i18n, error handling)
- The user says "I need to think about this" or asks for help planning

Lean toward **Nano** when:
- The fix is obvious from the error message
- Only one file changes
- No architectural decisions involved
- The user says "just fix it" or "quick change"

If uncertain, briefly ask: "This looks like it could benefit from a quick spec. Should I draft one, or proceed directly?"

The user can always override: explicitly requesting a spec level takes priority over auto-triage.

---

## Step 2: Context Scan

Before generating any spec, scan the project for existing conventions. This prevents generic specs and ensures alignment with the project's architecture.

1. **Read constitution files** — Check for `constitution.md`, `GEMINI.md`, `CLAUDE.md`, `.cursorrules`, `CONVENTIONS.md`, or equivalent. These contain non-negotiable project rules that every spec inherits automatically.

2. **Analyze codebase** — Detect:
   - Tech stack (language, frameworks, libraries)
   - Project structure (monorepo, microservices, etc.)
   - Patterns in use (repository pattern, MVC, Clean Architecture)
   - Testing conventions (framework, coverage expectations)
   - Existing similar features (for consistency)

3. **Identify dependencies** — What existing modules, APIs, or services does this feature touch?

The context scan produces an internal "project profile" that shapes the spec. The user never sees this directly, but the spec reflects it — a Python/FastAPI project gets specs mentioning Pydantic models and Alembic migrations; a Next.js project gets specs mentioning server components and API routes.

---

## Step 3: Spec Generation

### Nano Path — Direct Execution

No spec generated. Proceed to implementation with a brief confirmation: "This is a straightforward change — implementing directly."

### Mini Path — Inline Spec

Generate a compact spec directly in the conversation. Structure:

```markdown
## Spec: [Feature Name]

**Goal:** [1-sentence description of what and why]

**Changes:**
- [ ] [Specific change 1]
- [ ] [Specific change 2]
- [ ] [Specific change 3]

**Acceptance Criteria:**
- [ ] [Testable criterion 1]
- [ ] [Testable criterion 2]

**Out of Scope:** [What this change does NOT include]
```

Present to the user for approval before implementing.

### Full Path — Spec Interview + Documents

Conduct a focused interview (3-5 questions) to clarify intent, then generate the full spec package.

#### Spec Interview Questions

Ask only what's unclear — skip questions the prompt already answers. Pick from:

1. **Who uses this?** — "Who is the end user? What's their primary use case?"
2. **What does success look like?** — "How will you know this feature works correctly?"
3. **What are the constraints?** — "Any non-negotiable rules? Performance targets? Compatibility requirements?"
4. **What's out of scope?** — "What should this explicitly NOT do?"
5. **How does it connect?** — "Are there existing features or systems this needs to integrate with?"

After the interview, generate three documents in the project. Read `references/spec-gallery.md` for examples of well-written specs. Save to `.specs/[feature-name]/` at project root:

1. **`requirements.md`** — What to build and why. User stories, acceptance criteria, constraints. Read `references/ears-guide.md` for optional structured requirements syntax.

2. **`design.md`** — How to build it. Architecture decisions, data flow, API design, component structure. Include diagrams when they clarify relationships.

3. **`tasks.md`** — Execution plan. Atomic, testable units of work ordered by dependency. Each task should be independently verifiable.

Read `templates/full-spec/` for the document templates.

Present all three to the user for review before proceeding.

---

## Step 4: Implementation

Execute the spec task by task. For each task:

1. Implement the change
2. Verify against the relevant acceptance criteria
3. Mark the task complete
4. Move to the next task

If a task reveals something the spec didn't anticipate, pause and update the spec before continuing — don't silently diverge. A spec that drifts from reality is worse than no spec at all.

---

## Step 5: Spec Diffing (Post-Implementation)

After implementation, compare what was specified against what was built. Report:

- **Fully implemented** — Spec criterion met exactly
- **Partially implemented** — Criterion met with deviations (explain why)
- **Not implemented** — Criterion skipped (explain why)
- **Bonus** — Something useful was implemented beyond the spec

This isn't about punishment — it's about learning. Deviations often reveal spec gaps that future specs should address.

---

## Step 6: Feedback (Optional)

After delivery, briefly ask: "Did the spec capture what you actually wanted? Anything it missed?"

Use the response to calibrate future triage decisions and spec quality for this project.

---

## Constitution Integration

If the project has a constitution file (or equivalent), every spec inherits its rules automatically. If the project doesn't have one, offer to create one using `templates/constitution-template.md`.

The constitution captures project-wide decisions that apply to all specs:
- Coding standards and conventions
- Architectural constraints
- Testing requirements
- Security policies
- Performance targets

This eliminates repetition — instead of specifying "use Pydantic for validation" in every spec, it's declared once in the constitution and inherited by all specs.

---

## Edge Cases

**User wants to skip the spec:** Respect this. Say "Understood, proceeding without spec" and implement directly. SDD is a tool, not a mandate.

**Spec becomes obsolete mid-implementation:** Update the spec to reflect reality, then continue. The spec is a living document, not a contract.

**Multiple features in one request:** Triage each feature independently. One might be nano while another is full.

**Existing spec needs updating:** Read the existing spec, identify what changed, and update only the affected sections.

**Project has no conventions file:** Generate specs using sensible defaults for the detected stack. Offer to create a constitution for future consistency.

---

## References

- `references/triage-rules.md` — Detailed classification rules and edge cases for Smart Triage
- `references/ears-guide.md` — EARS (Easy Approach to Requirements Syntax) for structured requirements
- `references/spec-gallery.md` — Real examples of well-written specs for different scenarios
- `references/constitution-guide.md` — How to create and maintain a project constitution
- `references/spec-diffing-guide.md` — How spec conformance analysis works
- `templates/` — All spec templates (nano, mini, full, constitution)
