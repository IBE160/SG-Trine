# ibe160 - System-Level Test Design

**Date:** 2025-11-28
**Scope:** System-Level (Phase 3 - Testability Review)

## 1. Testability Assessment

The architecture provides a strong foundation for comprehensive testing.

*   **Controllability:** **PASS**
    *   The FastAPI backend provides API endpoints suitable for data seeding and state manipulation for tests.
    *   FastAPI's dependency injection allows for easy mocking of external services like Supabase and Gemini.
    *   Error conditions from external APIs (e.g., Gemini) can be triggered through backend mocking.
*   **Observability:** **PASS**
    *   A logging strategy is defined for both frontend (remote logging) and backend (structured JSON logs).
    *   The use of clear Acceptance Criteria and established test quality rules (e.g., explicit assertions) promotes deterministic test results.
    *   NFRs are tied to measurable criteria, facilitating their validation.
*   **Reliability:** **PASS**
    *   The monorepo structure and clear API boundaries between frontend and backend encourage isolated testing.
    *   Emphasis on deterministic waits (e.g., `waitForResponse` in Playwright) and data factories supports reproducible failures.

## 2. Architecturally Significant Requirements (ASRs) and Risk Assessment

Key quality requirements and potential risks, scored using a Probability (1-3) x Impact (1-3) matrix.

| Risk ID | Category | Description                                   | Probability | Impact | Score | Mitigation                                                                                                                                                                                                            |
| :------ | :------- | :-------------------------------------------- | :---------- | :----- | :---- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ASR-S01 | SEC      | Secure User Task Data (Auth, Authz, RLS, JWT) | 3 (Likely)  | 3 (Critical) | 9     | Comprehensive security testing including RLS validation, JWT expiry checks, and API authorization for all endpoints. Use security linters/scanners in CI.                                                                 |
| ASR-P01 | PERF     | Fast and responsive UI/API (<500ms p95 API)   | 2 (Possible) | 2 (Degraded) | 4     | Implement caching strategies (FastAPI), optimize database queries. Perform load testing with k6 for API endpoints and Lighthouse for frontend performance.                                                               |
| ASR-R01 | REL      | Graceful Error Handling (API failures)        | 2 (Possible) | 2 (Degraded) | 4     | Implement robust error handling and fallback mechanisms for Gemini API calls. Test frontend resilience to backend errors (e.g., showing user-friendly messages). Implement backend retry logic for transient issues.   |
| ASR-M01 | MAINT    | Code Quality (coverage, duplication, security) | 1 (Unlikely) | 1 (Minor) | 1     | Enforce code quality gates in CI (coverage thresholds, static analysis, vulnerability scanning).                                                                                                                     |
| ASR-AI1 | TECH/BUS | AI-Powered Task Breakdown/Prioritization      | 3 (Likely)  | 3 (Critical) | 9     | Implement comprehensive testing of AI prompts, model responses, and data consistency. Focus on diverse user inputs and edge cases. Ensure fallback mechanisms are robust. Version control prompts.                      |

## 3. Test Levels Strategy

A layered testing approach to optimize confidence, feedback speed, and maintainability.

*   **Unit Tests (60%):**
    *   **Focus:** Isolated business logic (e.g., AI prompt construction, data transformation, utility functions), individual React components without dependencies.
    *   **Tools:** Jest (Frontend), Pytest (Backend).
    *   **Rationale:** Fastest feedback loop for developers, identifies bugs early at the lowest level.
*   **Integration Tests (25%):**
    *   **Focus:** API endpoint contracts (FastAPI), database interactions (Supabase data access), authentication/authorization logic, FastAPI-Gemini API communication.
    *   **Tools:** Pytest (Backend), `playwright.request` for API testing.
    *   **Rationale:** Verifies interactions between components without full UI overhead.
*   **End-to-End (E2E) Tests (15%):**
    *   **Focus:** Critical user journeys (e.g., "Plan My Day" workflow, task CRUD), cross-system interactions (Frontend -> Backend -> Supabase -> Gemini -> Frontend), NFR validation for Security and Reliability (as described below).
    *   **Tools:** Playwright (Frontend/Backend E2E).
    *   **Rationale:** Highest confidence for user-facing flows, validates the entire system from the user's perspective.
*   **Component Tests (UI):** (As needed, integrated into Unit Test percentage)
    *   **Focus:** Isolated UI components (`shadcn/ui`), visual states, accessibility.
    *   **Tools:** Playwright Component Testing, Jest + React Testing Library.
    *   **Rationale:** Fast UI feedback, visual regression for key components.

## 4. NFR Testing Approach

Automated validation for Non-Functional Requirements.

*   **Security (ASR-S01):**
    *   **Approach:** Playwright E2E tests for authentication/authorization flows (unauthenticated access, JWT validation, RLS enforcement). Backend integration tests for input sanitization (SQL injection, XSS).
    *   **Tools:** Playwright, Pytest.
*   **Performance (ASR-P01):**
    *   **Approach:** Load testing with `k6` for critical API endpoints (`/api/v1/tasks`, `/api/v1/plan-my-day`), especially endpoints involving Gemini AI calls. Frontend performance monitored via Lighthouse (Playwright) to validate Core Web Vitals.
    *   **Tools:** k6, Playwright (for Lighthouse integration).
*   **Reliability (ASR-R01):**
    *   **Approach:** Playwright E2E tests simulating API failures (mocking 500s) and network disconnections to validate graceful degradation and user feedback. Backend integration tests for retry mechanisms and fallback strategies for external APIs.
    *   **Tools:** Playwright, Pytest.
*   **Maintainability (ASR-M01):**
    *   **Approach:** Integrated into CI/CD. Code coverage thresholds (Jest, Pytest), static analysis (ESLint, Ruff). Playwright E2E tests for observability (e.g., checking for Sentry logs in console/network).
    *   **Tools:** GitHub Actions, Jest, Pytest, ESLint, Ruff.

## 5. Test Environment Requirements

*   **Local Development:** Developers can run all unit and component tests instantly. Integration tests for FastAPI can use local Supabase containers (`supabase/supabase`) or mocked services. E2E tests against local stack.
*   **CI/CD Pipeline:** Automated execution of all test levels on every `git push`/`Pull Request`. Dedicated test databases/environments.
*   **Staging Environment:** E2E and NFR (Security, Performance, Reliability) tests executed against a production-like staging environment to validate real-world behavior and deployments.

## 6. Testability Concerns

None of the current architecture decisions (monorepo, Next.js, FastAPI, Supabase, Vercel) pose active testability concerns. The chosen stack and patterns generally support robust testing.

## 7. Recommendations for Sprint 0

*   **Implement Core Test Framework:** Set up Jest/React Testing Library for frontend, Pytest for backend, and Playwright for E2E.
*   **Data Factories:** Create comprehensive data factories (e.g., using Faker) for generating unique, realistic test data for users, tasks, and labels.
*   **CI Integration:** Integrate test execution and quality gates into the CI/CD pipeline (e.g., GitHub Actions).
*   **NFR Test Scaffolding:** Begin scaffolding tests for high-risk ASRs, especially for Security (ASR-S01) and AI Workflow (ASR-AI1).
*   **Prompt Versioning:** Implement a strategy to version control AI prompts to ensure test repeatability and track changes.

---

## 8. Test Design Complete

**Epic**: N/A (System-Level)
**Scope**: full (System-Level)

**Risk Assessment**:

- Total risks identified: 5
- High-priority risks (≥6): 2 (ASR-S01, ASR-AI1)
- Categories: SEC, PERF, REL, MAINT, TECH/BUS

**Coverage Plan**:

- This is a system-level design; specific scenario counts are not applicable here.

**Test Levels**:

- E2E: 15%
- API: 25%
- Component: As needed
- Unit: 60%

**Quality Gate Criteria**:

- All P0 tests pass (100%)
- P1 tests pass rate ≥95%
- No high-risk (score ≥6) items unmitigated
- Test coverage ≥80% for critical paths

**Output File**: docs/test-design-system-2025-11-28.md

**Next Steps**:

1. Review risk assessment with team
2. Prioritize mitigation for high-risk items (score ≥6)
3. Run `atdd` workflow to generate failing tests for P0 scenarios
4. Allocate resources per effort estimates
5. Set up test data factories and fixtures
