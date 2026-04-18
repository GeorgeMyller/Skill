# Tasks: [Feature Name]

<!-- 
  Organize tasks into phases ordered by dependency. 
  Each task should be atomic (one logical unit) and independently testable.
  Estimate complexity as S/M/L if helpful.
-->

## Phase 1: Foundation
<!-- Setup, data models, configuration — things other tasks depend on. -->

- [ ] **Task 1:** [Description] `[S/M/L]`
  - Files: [list affected files]
  - Verify: [how to confirm this task is done]

- [ ] **Task 2:** [Description] `[S/M/L]`
  - Files: [list affected files]
  - Verify: [how to confirm this task is done]

## Phase 2: Core Implementation
<!-- Main feature logic — depends on Phase 1. -->

- [ ] **Task 3:** [Description] `[S/M/L]`
  - Files: [list affected files]
  - Verify: [how to confirm this task is done]
  - Depends on: Task 1, Task 2

- [ ] **Task 4:** [Description] `[S/M/L]`
  - Files: [list affected files]
  - Verify: [how to confirm this task is done]

## Phase 3: Integration & Polish
<!-- Connecting components, error handling, edge cases. -->

- [ ] **Task 5:** [Description] `[S/M/L]`
  - Files: [list affected files]
  - Verify: [how to confirm this task is done]

## Phase 4: Testing & Validation
<!-- Tests, documentation, final verification. -->

- [ ] **Task 6:** Write unit tests for [component] `[M]`
  - Files: [test files]
  - Verify: All tests pass, coverage > [target]%

- [ ] **Task 7:** Write integration tests for [feature] `[M]`
  - Files: [test files]
  - Verify: All tests pass, covers happy path + error cases

---

## Task Guidelines

- **Atomic:** Each task produces a working (if incomplete) state. No task should leave the codebase broken.
- **Ordered:** Complete phases in order. Within a phase, tasks can run in parallel unless "Depends on" is specified.
- **Testable:** Every task has a "Verify" step. If you can't verify it, the task is too vague.
- **Sized:** S = under 30 min, M = 30-120 min, L = 2+ hours. If a task is XL, break it down further.
