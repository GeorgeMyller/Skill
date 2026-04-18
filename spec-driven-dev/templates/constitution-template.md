# Project Constitution

<!-- 
  This file captures project-wide rules, conventions, and architectural decisions 
  that apply to ALL features. Every spec inherits these rules automatically.
  
  Customize the sections below for your project. Remove sections that don't apply.
  Keep this document concise — it's loaded into context frequently.
-->

## Project Overview

- **Name:** [Project Name]
- **Type:** [Web App | API | CLI | Mobile | Library]
- **Stack:** [Primary languages, frameworks, databases]
- **Repository:** [URL or path]

## Architecture Principles

<!-- High-level architectural decisions that guide all development. -->

- [Principle 1 — e.g., "Monolith-first. No microservices until proven necessary."]
- [Principle 2 — e.g., "Server-side rendering by default. Client components only for interactivity."]
- [Principle 3 — e.g., "Clean Architecture. Dependencies flow inward."]

## Coding Standards

### Language & Style
- [Standard 1 — e.g., "Python 3.12+. Type hints on all public functions."]
- [Standard 2 — e.g., "Formatter: ruff. Linter: ruff. No exceptions."]
- [Standard 3 — e.g., "Maximum function length: 30 lines. Extract if longer."]

### Naming Conventions
- [Convention 1 — e.g., "Files: snake_case. Classes: PascalCase. Constants: UPPER_SNAKE."]
- [Convention 2 — e.g., "API endpoints: plural nouns (/users, /products)."]

### Error Handling
- [Pattern — e.g., "Custom exception hierarchy. Never catch generic Exception."]
- [Logging — e.g., "Structured JSON logging. Include correlation_id in all log entries."]

## Testing Requirements

- [Framework — e.g., "pytest for unit/integration. Playwright for E2E."]
- [Coverage — e.g., "Minimum 80% coverage on business logic. No coverage requirements for glue code."]
- [Pattern — e.g., "AAA pattern (Arrange/Act/Assert). One assertion per test method."]

## Security Policies

- [Policy 1 — e.g., "No secrets in code or config files. Use environment variables or vault."]
- [Policy 2 — e.g., "All user input validated with Pydantic. Never trust client-side validation alone."]
- [Policy 3 — e.g., "OWASP Top 10 compliance. Security review required for auth changes."]

## Dependencies

### Adding New Dependencies
- [Rule — e.g., "Evaluate maintenance status, license, and bundle size before adding."]
- [Process — e.g., "New dependencies require a brief justification in the PR description."]

### Banned
- [Banned 1 — e.g., "No moment.js (use date-fns or dayjs)."]
- [Banned 2 — e.g., "No lodash for operations available in ES2020+."]

## Git & Workflow

- [Commits — e.g., "Conventional Commits format. feat/fix/chore/docs/refactor."]
- [Branching — e.g., "Trunk-based. Feature branches max 2 days."]
- [Reviews — e.g., "All PRs require at least one review. CI must pass."]

## Don't

<!-- Anti-patterns discovered during the project. Add entries as you learn. -->

- [Anti-pattern 1 — e.g., "Don't use global state for form data."]
- [Anti-pattern 2 — e.g., "Don't bypass the ORM for raw SQL unless performance-critical."]

---

*Last updated: [date]*
*Review schedule: [quarterly | after major feature | as needed]*
