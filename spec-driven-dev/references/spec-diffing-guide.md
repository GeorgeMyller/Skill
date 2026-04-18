# Spec Diffing Guide

How spec conformance analysis works — comparing what was specified against what was built, and how to interpret the results.

## How It Works

After implementation is complete, the skill compares each acceptance criterion from the spec against the actual code changes. This is a heuristic analysis — it reads the spec and the implementation to assess alignment.

## Conformance Categories

### ✅ Fully Implemented
The acceptance criterion is met as specified. The code matches the intent and the details.

### ⚠️ Partially Implemented
The criterion is addressed but with deviations. Common reasons:
- A simpler approach was chosen (and may be sufficient)
- The spec was ambiguous and the agent interpreted it differently
- Technical constraints prevented exact implementation

For each partial match, explain the deviation and whether it matters.

### ❌ Not Implemented
The criterion was skipped entirely. Common reasons:
- Blocked by a dependency that wasn't ready
- Discovered during implementation that it conflicts with another requirement
- Time/scope constraints

Flag these clearly — they need explicit user decision (implement later, remove from spec, or accept the gap).

### 🎁 Bonus
Something useful was implemented beyond the spec. Common cases:
- Error handling that the spec didn't mention but is clearly needed
- Performance optimization discovered during implementation
- Helper utilities that emerged from the implementation

Bonuses are fine — just document them so the spec can be updated retroactively.

## Confidence Levels

Not all conformance assessments are equally reliable. Mark each one:

| Level | Meaning | When |
|-------|---------|------|
| **High** | Can verify from code structure/tests | Boolean criteria, API contracts, data models |
| **Medium** | Reasonable inference from implementation | UX behaviors, performance characteristics |
| **Low** | Subjective or hard to verify statically | "Graceful" error handling, "intuitive" UI |

Being honest about confidence prevents false trust. A report that says "high confidence on 8/10 criteria, low on 2" is more useful than one that claims 100% compliance.

## Report Format

```markdown
## Spec Conformance Report: [Feature Name]

**Spec:** `.specs/[feature]/requirements.md`
**Implementation:** [list of changed files]

| # | Criterion | Status | Confidence | Notes |
|---|-----------|--------|------------|-------|
| 1 | [criterion text] | ✅ Implemented | High | — |
| 2 | [criterion text] | ⚠️ Partial | Medium | [deviation explanation] |
| 3 | [criterion text] | ❌ Not implemented | High | [reason] |

**Summary:** X/Y criteria fully implemented. Z deviations noted.
**Recommendation:** [update spec | implement missing | accept as-is]
```

## Using Diffing to Improve

Spec diffing is most valuable as a learning tool:
- Consistent "partial" on similar criteria → spec template needs more detail in that area
- Frequent "bonus" implementations → specs are under-specifying (good agents fill gaps, but it's better to specify)
- "Not implemented" patterns → triage might be classifying tasks at too low a level
