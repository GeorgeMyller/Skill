---
description: Structured development workflow combining Spec-Driven Development and Test-Driven Development. Spec first, test first, code last. Use for building features, refactoring, or any non-trivial code change.
---

# /dev - Spec-Driven + Test-Driven Development

$ARGUMENTS

---

## Purpose

Unified development workflow that eliminates "vibe-coding" by enforcing:
1. **Specify** before coding (SDD)
2. **Test** before implementing (TDD)
3. **Verify** after delivering (Spec Diffing)

```
  ┌─────────────────────────────────────────────────────┐
  │                    /dev workflow                     │
  │                                                     │
  │  SPECIFY ──→ TEST ──→ IMPLEMENT ──→ VERIFY          │
  │   (SDD)      (TDD)    (GREEN)      (Diffing)        │
  │                                                     │
  │  Spec tells WHAT. Test proves WHEN. Code does HOW.  │
  └─────────────────────────────────────────────────────┘
```

---

## Sub-commands

```
/dev [feature description]     - Full workflow (triage → spec → TDD → verify)
/dev spec [description]        - Generate spec only (skip implementation)
/dev test [description]        - Generate tests from existing spec
/dev implement [spec path]     - Implement from existing spec using TDD
/dev verify [spec path]        - Run spec diffing on completed feature
```

---

## Phase 1: Smart Triage

> **Skill:** `@spec-driven-dev` — Step 1

Classify the request complexity. This determines the entire workflow path:

| Level | Spec | Tests | Implementation |
|-------|------|-------|----------------|
| **Nano** | None | None (or quick sanity) | Direct execution |
| **Mini** | Inline (5-10 bullets) | Unit tests from acceptance criteria | RED → GREEN → REFACTOR per criterion |
| **Full** | Full package (3 docs) | Full test suite from requirements | RED → GREEN → REFACTOR per task |

**If Nano:** Execute directly. Workflow ends here. Commit.

**If Mini or Full:** Continue to Phase 2.

---

## Phase 2: Spec Generation

> **Skill:** `@spec-driven-dev` — Steps 2-3

### Context Scan
1. Read constitution files (`GEMINI.md`, `CLAUDE.md`, `.cursorrules`, `constitution.md`)
2. Detect tech stack, patterns, testing framework
3. Identify dependencies and affected modules

### Generate Spec

**Mini path:** Inline spec in conversation with:
- Goal, Changes, Acceptance Criteria, Out of Scope

**Full path:** Spec Interview (3-5 questions) → Generate:
- `.specs/[feature]/requirements.md`
- `.specs/[feature]/design.md`
- `.specs/[feature]/tasks.md`

### 🛑 Gate: User Approval

Present spec to user. **Do NOT proceed until approved.**

If user requests changes, update spec and re-present.

---

## Phase 3: Test Generation (RED)

> **Skill:** `@tdd-workflow` — RED Phase

Convert spec into failing tests **before writing any production code.**

### Mini Path

For each acceptance criterion, write one test:

```
Acceptance Criterion → Test Case → Failing Test
```

Example:
```
Criterion: "Returns 200 with paginated JSON"
    → test: "should return 200 with page and per_page params"
    → FAILS (endpoint doesn't exist yet)
```

### Full Path

For each task in `tasks.md`, generate tests by priority:
1. **Happy path** — Core behavior works
2. **Error cases** — Failures are handled
3. **Edge cases** — Boundaries are respected

Save tests alongside production code following project conventions.

### Test Rules (Three Laws of TDD)

- Write ONLY enough test to demonstrate failure
- Test describes expected **behavior**, not implementation
- One assertion per test (ideally)
- Every test MUST fail before writing production code
- Use AAA pattern: **Arrange → Act → Assert**

### Run Tests — Confirm RED 🔴

```bash
# Run the new tests — ALL must fail
[project test command]
```

If any test passes before implementation, the test is wrong (testing existing behavior) or the feature already exists. Investigate.

---

## Phase 4: Implementation (GREEN)

> **Skill:** `@tdd-workflow` — GREEN Phase

For each failing test, write the **minimum code** to make it pass:

```
🔴 Failing Test → Write Minimum Code → 🟢 Test Passes → Next Test
```

### Rules

| Principle | Meaning |
|-----------|---------|
| **YAGNI** | Don't write code no test requires |
| **Simplest thing** | Make it pass, nothing more |
| **No optimization** | Performance comes in Phase 5 |

### Execution Order

**Mini:** Implement acceptance criteria in order.

**Full:** Follow `tasks.md` phase order:
1. Complete all Phase 1 tasks (foundation)
2. Run tests → verify GREEN on Phase 1
3. Complete Phase 2 tasks (core)
4. Run tests → verify GREEN on Phase 2
5. Continue until all phases complete

### Spec Drift Check

If implementation reveals something the spec missed:
1. **STOP** implementation
2. Note what the spec missed
3. Update the spec (add criterion or modify design)
4. Write test for the new criterion (RED)
5. Resume implementation (GREEN)

Never silently diverge from the spec.

---

## Phase 5: Refactor (BLUE)

> **Skill:** `@tdd-workflow` — REFACTOR Phase

After all tests pass, improve code quality:

| Area | Action |
|------|--------|
| Duplication | Extract shared code |
| Naming | Make intent clear |
| Structure | Improve organization |
| Complexity | Simplify logic |

### Refactor Rules

- **All tests MUST stay green** after each change
- Small incremental changes
- Commit after each meaningful refactor
- No new features — only quality improvement

```bash
# After each refactor step
[project test command]  # Must pass
git commit -m "refactor: [description]"
```

---

## Phase 6: Spec Diffing (Verify)

> **Skill:** `@spec-driven-dev` — Step 5

Compare what was specified vs what was built:

| Status | Meaning |
|--------|---------|
| ✅ Fully implemented | Criterion met, test passes |
| ⚠️ Partially implemented | Deviation exists (explain why) |
| ❌ Not implemented | Criterion skipped (explain why) |
| 🎁 Bonus | Implemented beyond spec |

### Conformance Report

```markdown
## Spec Conformance: [Feature Name]

| # | Criterion | Status | Test | Notes |
|---|-----------|--------|------|-------|
| 1 | [criterion] | ✅ | test_name | — |
| 2 | [criterion] | ⚠️ | test_name | [deviation] |

**Coverage:** X/Y criteria. Z tests passing.
```

---

## Phase 7: Commit & Feedback

### Commit Strategy

| Phase | Commit Message |
|-------|---------------|
| Spec approved | `docs: add spec for [feature]` |
| Tests written (RED) | `test: add failing tests for [feature]` |
| Each task GREEN | `feat: implement [task description]` |
| Refactor | `refactor: [improvement description]` |
| Final | `feat: complete [feature] — all tests passing` |

### Feedback Loop

> **Skill:** `@spec-driven-dev` — Step 6

Ask: "Did the spec capture what you wanted? Anything it missed?"

Use response to calibrate future triage and spec quality.

---

## Quick Reference

```
/dev add user authentication

Phase 1: Triage → Full (security-sensitive, multi-file)
Phase 2: Spec Interview → requirements.md + design.md + tasks.md → User approves
Phase 3: RED — Write failing tests for Task 1 → Confirm all fail
Phase 4: GREEN — Implement minimum code → Tests pass
Phase 5: REFACTOR — Clean up → Tests still pass
        ↳ Repeat Phases 3-5 for each task
Phase 6: Verify — Spec diffing report
Phase 7: Commit → Feedback
```

---

## When NOT to Use /dev

| Situation | Use Instead |
|-----------|-------------|
| Quick fix, typo, rename | Direct edit (nano) |
| Exploratory prototype | `/create` then formalize with `/dev` |
| Only need tests | `/test [target]` |
| Only need a plan | `/plan [feature]` |
| UI/UX design focus | `/ui-ux-pro-max` |
| Debugging | `/debug` |

---

## Agents Involved

| Phase | Primary Agent | Skills |
|-------|--------------|--------|
| Triage + Spec | `project-planner` | `spec-driven-dev`, `brainstorming` |
| Test Generation | `test-engineer` | `tdd-workflow`, `testing-patterns` |
| Implementation | Domain specialist | `clean-code` + domain skills |
| Refactor | `code-archaeologist` | `clean-code`, `code-review-checklist` |
| Verify | `project-planner` | `spec-driven-dev` |
