# Mini-Spec Template

Use this template for bounded, multi-step features that don't require full architectural documentation.

---

## Spec: [Feature Name]

**Goal:** [1-sentence: what this feature does AND why it's needed]

**Context:** [Brief note on how this fits into the existing system — what it touches, what it extends]

**Changes:**
- [ ] [Specific change 1 — include file/module if known]
- [ ] [Specific change 2]
- [ ] [Specific change 3]
- [ ] [Add more as needed, typically 3-8 items]

**Acceptance Criteria:**
- [ ] [Testable criterion 1 — should be verifiable by running the code]
- [ ] [Testable criterion 2]
- [ ] [Testable criterion 3]

**Out of Scope:** [Explicitly list what this feature does NOT include — prevents scope creep]

**Dependencies:** [Any existing modules, APIs, or services this touches — helps with impact analysis]

---

## Usage Notes

- Keep the goal to one sentence. If it needs two, the feature might need a full spec.
- Each change should map to roughly one commit or one logical unit of work.
- Acceptance criteria must be testable — "works correctly" is not testable; "returns 200 with valid JSON" is.
- Out of scope is not optional — it's the primary defense against scope creep.
