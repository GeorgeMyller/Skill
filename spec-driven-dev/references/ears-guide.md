# EARS — Easy Approach to Requirements Syntax

A simplified guide to writing structured requirements that AI agents (and humans) can parse unambiguously. EARS is optional — use it when precision matters (security features, regulatory compliance, complex business logic). For simpler features, natural language acceptance criteria work fine.

## Table of Contents
- [Why EARS](#why-ears)
- [The Five Patterns](#the-five-patterns)
- [When to Use EARS vs Natural Language](#when-to-use-ears-vs-natural-language)
- [Examples by Domain](#examples-by-domain)

---

## Why EARS

Natural language requirements are inherently ambiguous. "The system should handle errors gracefully" means different things to different people — and to different AI agents. EARS constrains natural language into predictable patterns that eliminate common ambiguities:

- Who does the action? (the system)
- When does it happen? (trigger condition)
- What exactly happens? (the requirement)

This structure makes requirements directly testable — each EARS statement maps to at least one test case.

---

## The Five Patterns

### 1. Ubiquitous (Always True)
Things the system must do at all times. No trigger needed.

**Template:** `The [system] shall [requirement].`

**Examples:**
- The API shall return responses in JSON format.
- The application shall encrypt all data at rest using AES-256.
- The system shall log all authentication attempts.

### 2. Event-Driven (When Something Happens)
Triggered by a specific event or user action.

**Template:** `When [trigger], the [system] shall [requirement].`

**Examples:**
- When a user submits the registration form, the system shall validate all required fields before creating the account.
- When the API receives a request without a valid auth token, the system shall return a 401 Unauthorized response.
- When the payment is confirmed, the system shall send a receipt email to the user.

### 3. State-Driven (While in a State)
Active only while a specific condition holds.

**Template:** `While [state], the [system] shall [requirement].`

**Examples:**
- While the system is in maintenance mode, the API shall return 503 Service Unavailable for all endpoints.
- While the user is on a free plan, the system shall display usage limits in the dashboard.
- While offline, the application shall queue mutations for sync when connectivity is restored.

### 4. Unwanted Behavior (Error Handling)
How the system responds to faults, failures, or invalid states.

**Template:** `If [condition], then the [system] shall [requirement].`

**Examples:**
- If a database connection fails, then the system shall retry 3 times with exponential backoff before returning an error.
- If the upload exceeds 10MB, then the system shall reject the file and display a clear error message.
- If the user's session expires during a form submission, then the system shall preserve the form data and prompt re-authentication.

### 5. Optional Features (Conditional Capabilities)
Applies only when a specific feature or configuration is present.

**Template:** `Where [feature/configuration], the [system] shall [requirement].`

**Examples:**
- Where two-factor authentication is enabled, the system shall require a TOTP code after password verification.
- Where the premium tier is active, the system shall allow up to 100 API calls per minute.
- Where the camera hardware is available, the application shall offer QR code scanning.

---

## When to Use EARS vs Natural Language

| Situation | Recommendation |
|-----------|---------------|
| Security features | Use EARS — precision prevents vulnerabilities |
| Business logic with edge cases | Use EARS — each pattern maps to test cases |
| Regulatory compliance | Use EARS — auditable, traceable requirements |
| Simple UI changes | Natural language is fine |
| Prototype or MVP | Natural language — speed over precision |
| Team with mixed experience | Natural language with EARS for critical paths |

A practical approach: write acceptance criteria in natural language first, then convert the critical ones to EARS format. This keeps specs readable while ensuring precision where it matters.

---

## Examples by Domain

### Authentication System (EARS)
```
- The system shall hash all passwords using bcrypt with a minimum cost factor of 12.
- When a user logs in successfully, the system shall issue a JWT access token (15min TTL) and a refresh token (7d TTL).
- If the refresh token is expired, then the system shall require full re-authentication.
- While the account is locked, the system shall reject all login attempts and display the remaining lockout time.
- If 5 consecutive login failures occur, then the system shall lock the account for 15 minutes.
- Where MFA is enabled, the system shall require TOTP verification after password authentication.
```

### E-commerce Cart (Natural Language + EARS for critical paths)
```
**User Story:** As a shopper, I want to add items to my cart so I can purchase them later.

**Acceptance Criteria:**
- Users can add products to the cart from the product detail page
- Cart shows item count in the header badge
- Users can update quantities or remove items
- Cart persists across browser sessions (localStorage)

**Critical Path (EARS):**
- When a user adds an item to the cart, the system shall verify inventory availability before confirming.
- If the requested quantity exceeds available stock, then the system shall set the quantity to maximum available and notify the user.
- When checkout is initiated, the system shall re-validate all cart items against current inventory and pricing.
```
