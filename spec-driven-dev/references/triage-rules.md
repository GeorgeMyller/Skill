# Smart Triage Rules

Detailed classification rules for the SDD Smart Triage system. The SKILL.md provides the overview; this file handles edge cases and nuanced decisions.

## Table of Contents
- [Classification Matrix](#classification-matrix)
- [Signal Detection](#signal-detection)
- [Override Protocol](#override-protocol)
- [Edge Cases](#edge-cases)

---

## Classification Matrix

### Nano — Execute Directly (No Spec)

Characteristics:
- Single file affected
- No architectural decisions
- Intent is unambiguous from the prompt
- No new dependencies
- Low risk of side effects

Example prompts that trigger nano:
- "Fix the typo in the README"
- "Rename `getUserData` to `fetchUserProfile`"
- "Add a comment explaining this regex"
- "Bump the version to 2.1.0"
- "Remove the unused import on line 45"
- "Adjust the padding from 16px to 24px"
- "Add `type: module` to package.json"

### Mini — Inline Spec (5-10 bullets)

Characteristics:
- 2-5 files affected
- Clear scope but multiple steps
- No new infrastructure or major dependencies
- Follows existing patterns in the codebase
- Moderate risk — mistakes are annoying but recoverable

Example prompts that trigger mini:
- "Add pagination to the users API"
- "Implement a dark mode toggle"
- "Add email validation to the signup form"
- "Create a new `/health` endpoint"
- "Add error handling to the file upload service"
- "Implement sorting and filtering on the products table"

### Full — Complete Spec Package

Characteristics:
- 5+ files affected, or new module/service
- Architectural decisions required
- New dependencies or infrastructure
- Security-sensitive (auth, payments, PII)
- Cross-cutting concerns
- Domain complexity requires clarification
- The user is uncertain about approach

Example prompts that trigger full:
- "Build an authentication system with JWT + refresh tokens"
- "Add real-time notifications using WebSockets"
- "Integrate Stripe payment processing"
- "Migrate from REST to GraphQL"
- "Implement role-based access control"
- "Build a multi-tenant architecture"
- "Add internationalization (i18n) support"
- "Rebuild the state management layer"

---

## Signal Detection

### Escalation Signals (Nano → Mini or Mini → Full)

Watch for these keywords/patterns that suggest higher complexity:
- "system", "architecture", "redesign", "rebuild" → Full
- "integrate", "migration", "multi-" → Full
- "security", "authentication", "payment", "encryption" → Full
- "several files", "across modules" → Mini or Full
- "I'm not sure how to approach" → Full (user needs design help)
- Numbers: "5+ endpoints", "multiple screens" → Full

### De-escalation Signals (Full → Mini or Mini → Nano)

- "Quick", "simple", "just", "only" → Lower level
- "Like the existing one" → Lower (pattern already exists)
- "Same as before but for X" → Lower (clone + modify)
- The user explicitly says "skip the spec" → Nano

---

## Override Protocol

The user always has final say. Accept overrides gracefully:

- **Explicit level request:** "Give me a full spec for this" → Full, even if triage says nano
- **Skip request:** "Just do it" → Nano, even if triage says full (acknowledge the risk: "Proceeding without spec — this is complex enough that we might need to iterate")
- **Upgrade request:** "Actually, let's think about this more carefully" → Upgrade to next level

Never argue with overrides. Briefly note the risk if downgrading a complex task, but respect the decision.

---

## Edge Cases

### Ambiguous Complexity

When a prompt could be nano OR mini:
- Default to nano but describe what you'll do before starting
- "I'll make these changes directly: [list]. Sound right?"
- If the user adds requirements, upgrade to mini

### Multiple Tasks in One Request

"Fix the login bug AND add OAuth support"
- Triage each independently: login bug = nano, OAuth = full
- Communicate the split: "The bug fix is straightforward — I'll handle it directly. The OAuth feature needs a spec. Starting with the bug fix..."

### Incomplete Information

If the prompt lacks detail for proper triage:
- Don't default to full (over-engineering)
- Ask one clarifying question: "Is this a quick tweak or a bigger feature?"
- Use the answer to triage

### Recurring Patterns

If the project has done similar work before:
- Check for existing specs in `.specs/`
- "This is similar to the [previous feature] spec. Should I base the new spec on that one?"
- Reuse reduces spec time by 40-60%
