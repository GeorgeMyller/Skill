# Design: [Feature Name]

## Architecture

### Overview

[1-2 paragraphs: high-level architecture. How this feature fits into the existing system. What components are new vs modified.]

### Component Diagram

<!-- Use text diagram, mermaid, or a simple table to show how components interact. -->

```
[Component A] → [Component B] → [Component C]
                      ↓
                [Component D]
```

## Data Model

<!-- Database tables, collections, or data structures this feature introduces or modifies. -->

### [Table/Entity Name]

| Column/Field | Type | Constraints | Description |
|-------------|------|-------------|-------------|
| id | UUID | PK | Unique identifier |
| [field] | [type] | [constraints] | [description] |

<!-- Add more tables as needed. -->

## API Design

<!-- Endpoints, message formats, or interfaces this feature introduces. -->

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| [GET/POST/etc] | [path] | [Public/Token] | [what it does] |

### Request/Response Examples

```json
// POST /api/[endpoint]
// Request:
{
  "field": "value"
}

// Response (200):
{
  "id": "uuid",
  "field": "value",
  "created_at": "2026-01-01T00:00:00Z"
}
```

## Key Technical Decisions

<!-- Document the "why" behind significant choices. Future developers (and agents) will thank you. -->

1. **[Decision]:** [What was chosen] over [alternatives considered]. Reason: [why].
2. **[Decision]:** [What was chosen]. Reason: [why].

## Error Handling

<!-- How errors are handled, propagated, and presented to users. -->

- [Error scenario 1]: [How it's handled]
- [Error scenario 2]: [How it's handled]

## Security Considerations

<!-- Relevant security aspects: auth, input validation, data protection, rate limiting. -->

- [Security measure 1]
- [Security measure 2]

## Performance Considerations

<!-- Expected load, caching strategy, optimization targets. -->

- [Performance target or strategy]

---

## Notes

<!-- Implementation notes, known limitations, future improvements. -->
