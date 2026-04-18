# Spec Gallery

Real examples of well-written specifications at each triage level. Learn by reading good specs — they're more instructive than abstract rules.

## Table of Contents
- [Mini Spec: API Pagination](#mini-spec-api-pagination)
- [Mini Spec: Dark Mode Toggle](#mini-spec-dark-mode-toggle)
- [Full Spec: User Authentication](#full-spec-user-authentication)
- [Full Spec: Real-Time Notifications](#full-spec-real-time-notifications)

---

## Mini Spec: API Pagination

```markdown
## Spec: Add Pagination to Users API

**Goal:** Allow clients to paginate through user lists instead of loading all users at once, preventing timeout on large datasets.

**Changes:**
- [ ] Add `page` and `per_page` query parameters to `GET /api/users`
- [ ] Default: page=1, per_page=20, max per_page=100
- [ ] Return pagination metadata in response headers (X-Total-Count, X-Total-Pages)
- [ ] Add `Link` header with rel=next, rel=prev, rel=first, rel=last
- [ ] Update existing tests to use pagination

**Acceptance Criteria:**
- [ ] `GET /api/users?page=2&per_page=10` returns users 11-20
- [ ] Response includes correct pagination metadata
- [ ] Invalid page numbers return empty results (not errors)
- [ ] Default behavior (no params) returns first 20 users

**Out of Scope:** Cursor-based pagination, infinite scroll frontend, search/filter.
```

**Why this works:** Clear goal explaining the "why" (timeout prevention). Specific changes with defaults and limits. Acceptance criteria are directly testable. Out-of-scope prevents creep.

---

## Mini Spec: Dark Mode Toggle

```markdown
## Spec: Dark Mode Toggle

**Goal:** Allow users to switch between light/dark themes; persist preference across sessions.

**Changes:**
- [ ] Add theme toggle button in header (sun/moon icon)
- [ ] Implement CSS custom properties for color tokens (--bg-primary, --text-primary, etc.)
- [ ] Store preference in localStorage under key `theme-preference`
- [ ] Respect system preference via `prefers-color-scheme` as default
- [ ] Add smooth transition (200ms) when switching themes

**Acceptance Criteria:**
- [ ] Toggle switches between light and dark immediately
- [ ] Preference persists after page reload
- [ ] New visitors see system-preferred theme
- [ ] No flash of wrong theme on page load (FOUC prevention)

**Out of Scope:** Custom color themes, per-page theme settings, theme API.
```

**Why this works:** Specific implementation details (localStorage key, transition duration). The FOUC criterion catches a common pitfall. Out-of-scope prevents over-engineering.

---

## Full Spec: User Authentication

### requirements.md

```markdown
# Requirements: User Authentication System

## Overview
Implement a secure authentication system allowing users to register, login, and manage sessions using JWT tokens. The system must support email/password authentication with optional MFA via TOTP.

## User Stories

### US-1: Registration
As a new user, I want to create an account with my email and password so I can access the application.

**Acceptance Criteria:**
- Email must be unique and valid (RFC 5322)
- Password minimum 8 characters, at least 1 uppercase, 1 number, 1 special character
- Email verification required before account is fully active
- Registration sends verification email within 30 seconds

### US-2: Login
As a registered user, I want to log in with my credentials so I can access my data.

**Acceptance Criteria:**
- Successful login returns JWT access token (15min) and refresh token (7 days)
- Failed login returns generic "Invalid credentials" (no email enumeration)
- If 5 failed attempts in 15 minutes, lock account for 15 minutes
- Locked account shows remaining lockout time

### US-3: Session Management
As a logged-in user, I want my session to persist so I don't have to re-login frequently.

**Acceptance Criteria:**
- Access token refreshable via refresh token endpoint
- Expired refresh token requires full re-authentication
- User can view active sessions and revoke any session
- Logout invalidates both access and refresh tokens

### US-4: MFA (Optional)
As a security-conscious user, I want to enable TOTP-based MFA.

**Acceptance Criteria:**
- Enable MFA via settings page (QR code + backup codes)
- Login with MFA requires TOTP after password
- 10 single-use backup codes generated on MFA setup
- MFA can be disabled with password confirmation

## Constraints
- Passwords hashed with bcrypt (cost factor 12+)
- Tokens use RS256 signing
- All auth endpoints rate-limited (100 req/min per IP)
- OWASP Top 10 compliance required

## Out of Scope
- Social login (Google, GitHub) — planned for Phase 2
- Passwordless authentication
- SSO/SAML integration
```

### design.md

```markdown
# Design: User Authentication System

## Architecture

### Component Diagram
```
Client → API Gateway → Auth Service → Database (PostgreSQL)
                            ↓
                       Token Store (Redis)
                            ↓
                       Email Service (SMTP/SES)
```

### Data Model

**Users Table:**
| Column | Type | Constraints |
|--------|------|-------------|
| id | UUID | PK, default gen_random_uuid() |
| email | VARCHAR(255) | UNIQUE, NOT NULL |
| password_hash | VARCHAR(255) | NOT NULL |
| email_verified | BOOLEAN | DEFAULT false |
| mfa_enabled | BOOLEAN | DEFAULT false |
| mfa_secret | VARCHAR(255) | NULLABLE, encrypted |
| locked_until | TIMESTAMP | NULLABLE |
| failed_attempts | INTEGER | DEFAULT 0 |
| created_at | TIMESTAMP | DEFAULT now() |
| updated_at | TIMESTAMP | DEFAULT now() |

**Sessions Table:**
| Column | Type | Constraints |
|--------|------|-------------|
| id | UUID | PK |
| user_id | UUID | FK → users.id |
| refresh_token_hash | VARCHAR(255) | NOT NULL |
| device_info | JSONB | NULLABLE |
| expires_at | TIMESTAMP | NOT NULL |
| created_at | TIMESTAMP | DEFAULT now() |

### API Endpoints

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| POST | /auth/register | Public | Create account |
| POST | /auth/login | Public | Authenticate |
| POST | /auth/refresh | Refresh Token | Renew access token |
| POST | /auth/logout | Access Token | End session |
| GET | /auth/sessions | Access Token | List active sessions |
| DELETE | /auth/sessions/:id | Access Token | Revoke session |
| POST | /auth/verify-email | Public | Verify email token |
| POST | /auth/mfa/setup | Access Token | Enable MFA |
| POST | /auth/mfa/verify | Public | Verify TOTP code |

### Security Decisions
- **RS256 over HS256:** Allows token verification without sharing the signing key
- **Redis for token blacklist:** Fast lookup for revoked tokens; TTL auto-cleanup
- **bcrypt over argon2:** Wider library support; cost factor 12 provides adequate security
- **Refresh token rotation:** Each refresh issues new refresh token, invalidating the old one
```

### tasks.md

```markdown
# Tasks: User Authentication System

## Phase 1: Foundation (no dependencies)
- [ ] Task 1: Create database migration for users table
- [ ] Task 2: Create database migration for sessions table
- [ ] Task 3: Set up Redis connection for token store
- [ ] Task 4: Create User model with password hashing

## Phase 2: Core Auth (depends on Phase 1)
- [ ] Task 5: Implement POST /auth/register with email validation
- [ ] Task 6: Implement POST /auth/login with JWT generation
- [ ] Task 7: Implement POST /auth/refresh with token rotation
- [ ] Task 8: Implement POST /auth/logout with token blacklisting

## Phase 3: Session Management (depends on Phase 2)
- [ ] Task 9: Implement GET /auth/sessions
- [ ] Task 10: Implement DELETE /auth/sessions/:id
- [ ] Task 11: Implement account locking after failed attempts

## Phase 4: Email & MFA (depends on Phase 2)
- [ ] Task 12: Set up email service (verification emails)
- [ ] Task 13: Implement POST /auth/verify-email
- [ ] Task 14: Implement MFA setup (TOTP secret + QR)
- [ ] Task 15: Implement MFA verification flow

## Phase 5: Testing & Security
- [ ] Task 16: Write unit tests for auth service
- [ ] Task 17: Write integration tests for all endpoints
- [ ] Task 18: Security audit (rate limiting, input validation)
```

---

## Full Spec: Real-Time Notifications

*(Abbreviated for brevity — shows the pattern for event-driven features)*

### requirements.md

```markdown
# Requirements: Real-Time Notification System

## Overview
Deliver instant notifications to connected users via WebSocket. Support multiple notification types (info, warning, action-required) with read/unread tracking and persistence.

## User Stories

### US-1: Receive Notifications
As a logged-in user, I want to receive instant notifications without refreshing the page.

**Acceptance Criteria:**
- Notifications appear within 2 seconds of the triggering event
- Notification bell shows unread count badge
- Toast notification appears for high-priority items
- Works across multiple browser tabs (single WebSocket, SharedWorker)

### US-2: Notification History
As a user, I want to see my past notifications so I can review what I missed.

**Acceptance Criteria:**
- Notification drawer shows last 50 notifications
- Grouped by date (Today, Yesterday, This Week, Older)
- Mark individual or all as read
- Click notification navigates to relevant context

## Constraints
- WebSocket reconnection with exponential backoff
- Graceful degradation: polling fallback if WebSocket unavailable
- Maximum 100 concurrent WebSocket connections per user (prevent tab storms)
```

**Why this works:** Specific latency target (2 seconds). Addresses multi-tab edge case. Includes graceful degradation strategy. Constraints prevent resource exhaustion.
