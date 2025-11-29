# Epic Technical Specification: {{epic_title}}

Date: {{date}}
Author: {{user_name}}
Epic ID: {{epic_id}}
Status: Draft

---

## Overview

## Overview

This technical specification details Epic 1: "Foundation & Core Task Management" for the "Prioritize" application, as defined in the Product Requirements Document (PRD). The primary goal of this epic is to establish the fundamental application infrastructure and enable users to perform essential task management operations, including Create, Read, Update, Delete (CRUD), task reordering, and marking tasks as complete. This foundation is critical for the subsequent integration of AI-powered features and advanced user experience enhancements.

## Objectives and Scope

## Objectives and Scope

### In Scope:
- Establishment of core application infrastructure (Next.js frontend, FastAPI backend, Supabase).
- Implementation of full CRUD functionality for tasks (Create, Read, Update, Delete).
- Ability for users to mark tasks as complete.
- Functionality for users to reorder tasks.
- Secure storage and management of task data in Supabase.
- Basic user interface components for task interaction, adhering to hyper-minimalism.
- Initial project setup and deployment to Vercel.

### Out of Scope for this Epic:
- AI-powered features (smart labels, priority suggestions, task breakdown).
- Advanced UX features (Today view, light/dark mode, search).
- Specialized ADHD support tools (time estimates, "Just Start Here" button, timers, nudges).
- Complex authentication flows beyond basic Supabase integration.
- Collaboration features.

## System Architecture Alignment

## System Architecture Alignment

This epic's implementation is fundamentally aligned with the core architectural decisions of the "Prioritize" application. It leverages the chosen `Next.js` frontend and `FastAPI` backend structure for scalable and maintainable development. `Supabase` is central to this epic, providing robust data persistence, authentication management, and real-time update capabilities for user task data. The entire setup is designed for seamless deployment via `Vercel`, establishing the foundational CI/CD pipeline and deployment strategy. Constraints include adhering to the monorepo structure and utilizing Pydantic for data validation in the API.

## Detailed Design

### Services and Modules

### Services and Modules

**Frontend (Next.js Application)**
- **Module:** `nextjs-frontend`
- **Responsibility:** User interface rendering, user interaction handling, API calls to backend, state management, routing, client-side data validation.
- **Inputs:** User input (task creation, edits, reorders, deletions), API responses from FastAPI.
- **Outputs:** API requests to FastAPI, updated UI state.
- **Owner:** Frontend Team

**Backend (FastAPI Application)**
- **Module:** `api`
- **Responsibility:** API endpoint provision, business logic execution (task CRUD), data persistence via Supabase, authentication validation, AI integration orchestration (future epics).
- **Inputs:** HTTP requests from Next.js frontend (task data, user authentication tokens).
- **Outputs:** HTTP responses to Next.js frontend (task data, status codes, error messages), Supabase database operations.
- **Owner:** Backend Team

**Database (Supabase PostgreSQL)**
- **Module:** `Supabase Database`
- **Responsibility:** Secure and persistent storage of user and task data, Row Level Security (RLS) enforcement, real-time data change notifications.
- **Inputs:** SQL commands from FastAPI backend (via `supabase-py`).
- **Outputs:** Query results to FastAPI backend, real-time events to subscribed clients.
- **Owner:** Platform Team (Managed Service)


### Data Models and Contracts

### Data Models and Contracts

The core data model for Epic 1 revolves around `users` and `tasks`. These tables reside in the Supabase PostgreSQL database.

**Table: `users`**
- **Purpose:** Stores user authentication and profile information.
- **Fields:**
    - `id`: UUID (Primary Key, Supabase Auth User ID)
    - `email`: TEXT (Unique, User's email address)
    - `created_at`: TIMESTAMP WITH TIME ZONE (Automatically set on creation)
- **Relationships:** One-to-many with `tasks` (a user can have many tasks).

**Table: `tasks`**
- **Purpose:** Stores individual user tasks.
- **Fields:**
    - `id`: UUID (Primary Key, Auto-generated)
    - `user_id`: UUID (Foreign Key to `users.id`, links task to owner)
    - `title`: TEXT (The description of the task)
    - `is_completed`: BOOLEAN (Default: `FALSE`, indicates task completion status)
    - `sort_order`: INTEGER (Used for user-defined task reordering)
    - `created_at`: TIMESTAMP WITH TIME ZONE (Automatically set on creation)
    - `updated_at`: TIMESTAMP WITH TIME ZONE (Automatically updated on modification)
- **Relationships:** Many-to-one with `users` (many tasks belong to one user). Enforces Row Level Security (RLS) based on `user_id`.

### APIs and Interfaces

### APIs and Interfaces

All API endpoints will be exposed via a versioned RESTful API (`/api/v1`) using FastAPI. Pydantic models will be used for request and response data validation. Authentication will be handled via JWT validation, leveraging Supabase's authentication mechanism.

**1. Create Task**
- **Method:** `POST`
- **Path:** `/api/v1/tasks`
- **Description:** Creates a new task for the authenticated user.
- **Request Body:** `{ "title": "string" }` (Pydantic model: `TaskCreate`)
- **Response:** `{ "id": "uuid", "title": "string", "is_completed": "boolean", ... }` (Pydantic model: `TaskResponse`)
- **Error Codes:** 401 Unauthorized, 422 Unprocessable Entity (validation errors)

**2. Read Tasks**
- **Method:** `GET`
- **Path:** `/api/v1/tasks`
- **Description:** Retrieves all tasks for the authenticated user.
- **Request Query:** Optional filters (e.g., `?is_completed=false`).
- **Response:** `[ { "id": "uuid", "title": "string", "is_completed": "boolean", ... } ]` (List of `TaskResponse`)
- **Error Codes:** 401 Unauthorized

**3. Update Task**
- **Method:** `PUT`
- **Path:** `/api/v1/tasks/{task_id}`
- **Description:** Updates an existing task for the authenticated user.
- **Request Body:** `{ "title": "string", "is_completed": "boolean", "sort_order": "integer" }` (Pydantic model: `TaskUpdate`)
- **Response:** `{ "id": "uuid", "title": "string", "is_completed": "boolean", ... }` (Pydantic model: `TaskResponse`)
- **Error Codes:** 401 Unauthorized, 404 Not Found, 422 Unprocessable Entity

**4. Delete Task**
- **Method:** `DELETE`
- **Path:** `/api/v1/tasks/{task_id}`
- **Description:** Deletes a task for the authenticated user.
- **Response:** 204 No Content
- **Error Codes:** 401 Unauthorized, 404 Not Found

### Workflows and Sequencing

### Workflows and Sequencing

**1. Task Creation Workflow**

- **Actor:** User
- **Steps:**
    1. User interacts with the Next.js frontend to input a new task title.
    2. Frontend sends a `POST /api/v1/tasks` request to the FastAPI backend with the task title.
    3. FastAPI backend validates the request, extracts the authenticated `user_id` from the JWT.
    4. FastAPI backend inserts a new record into the `tasks` table in Supabase.
    5. Supabase returns the new task record to FastAPI.
    6. FastAPI returns the new task record (including `id` and default `is_completed: false`) to the Frontend.
    7. Frontend updates the UI to display the new task.
    8. Real-time: Supabase notifies all subscribed clients of the new task, ensuring immediate display on other devices.

**2. Task Viewing Workflow**

- **Actor:** User
- **Steps:**
    1. User navigates to a task list view on the Next.js frontend.
    2. Frontend sends a `GET /api/v1/tasks` request to the FastAPI backend.
    3. FastAPI backend validates the request, extracts `user_id`.
    4. FastAPI queries the `tasks` table in Supabase, filtered by `user_id` (enforced by RLS).
    5. Supabase returns the list of tasks to FastAPI.
    6. FastAPI returns the list of tasks to the Frontend.
    7. Frontend renders the tasks in the UI.

**3. Task Update / Deletion Workflow**

- **Actor:** User
- **Steps (Update):**
    1. User modifies a task (e.g., changes title, toggles completion, reorders) on the Next.js frontend.
    2. Frontend sends a `PUT /api/v1/tasks/{task_id}` request to the FastAPI backend with updated task data.
    3. FastAPI backend validates the request and `task_id`, ensures `user_id` ownership.
    4. FastAPI updates the corresponding record in the `tasks` table in Supabase.
    5. Supabase returns the updated record.
    6. FastAPI returns the updated task record to the Frontend.
    7. Frontend updates the UI.
    8. Real-time: Supabase notifies all subscribed clients of the task update.
- **Steps (Deletion):**
    1. User initiates a task deletion on the Next.js frontend.
    2. Frontend sends a `DELETE /api/v1/tasks/{task_id}` request to the FastAPI backend.
    3. FastAPI backend validates the request and `task_id`, ensures `user_id` ownership.
    4. FastAPI deletes the record from the `tasks` table in Supabase.
    5. Supabase confirms deletion.
    6. FastAPI returns a 204 No Content response to the Frontend.
    7. Frontend removes the task from the UI.
    8. Real-time: Supabase notifies all subscribed clients of the task deletion.


## Non-Functional Requirements

### Performance

### Performance

- **UI Responsiveness:** Task loading, creation, updates, and deletions in the user interface must occur near-instantaneously (target < 500ms for visual feedback after user action). This minimizes user frustration and cognitive load, especially for users with ADHD.
- **API Latency:** Backend API responses for core CRUD operations (`/api/v1/tasks`) must have an average latency of less than 100ms, excluding network transit time.
- **Real-time Updates:** Changes to tasks (e.g., completion, reordering) made on one client must be reflected on all other subscribed clients within 1 second.
- **Frontend Optimization:** Leverage Next.js features (SSR/SSG), efficient UI components (`shadcn/ui`), and optimized resource loading to ensure fast initial page load (target < 2 seconds for FCP on a 3G network) and smooth subsequent interactions.
- **Backend Optimization:** FastAPI endpoints will be optimized for low latency, utilizing efficient database queries and minimal processing overhead. (Reference: PRD - Non-Functional Requirements, Architecture - Cross-Cutting Concerns: Performance).

### Security

### Security

- **Authentication & Authorization:**
    - User authentication will be handled via `Supabase Auth`, utilizing a secure JWT-based flow.
    - The FastAPI backend will validate JWTs on protected routes to authorize user requests.
    - User registration and login mechanisms will adhere to industry best practices for secure credential handling. (Reference: Architecture - 3.2. Authentication Flow).
- **Data Persistence & Isolation:**
    - User task data will be stored securely in `Supabase PostgreSQL`.
    - `Row Level Security (RLS)` policies will be strictly enforced on the `tasks` table to ensure that users can only access and modify their own data. (Reference: Architecture - 3.1. Supabase Integration).
- **Data Confidentiality & Integrity:**
    - All data in transit between the frontend, backend, and Supabase will be encrypted (HTTPS/WSS).
    - Data integrity will be maintained through database constraints and application-level validation (Pydantic models in FastAPI).
- **Threat Model (Basic):**
    - Focus on preventing unauthorized access to user data and API abuse.
    - Mitigation: Strong authentication, RLS, input validation, rate limiting (future consideration).
- **No Sensitive Data Storage:** No highly sensitive personal data beyond basic user authentication (email) and task content will be stored. (Reference: PRD - Non-Functional Requirements: Security).

### Reliability/Availability

### Reliability/Availability

- **High Availability:** The application will leverage cloud-native services designed for high availability:
    - `Vercel` for frontend and serverless FastAPI backend deployment, providing inherent redundancy and automated scaling.
    - `Supabase` as a managed PostgreSQL service offers high availability and automated backups.
- **Error Handling & Degradation:**
    - **Frontend:** Implement `React Error Boundaries` to gracefully handle UI rendering errors, preventing critical application failures. User-facing errors will be communicated via non-intrusive toast notifications.
    - **Backend:** A global `FastAPI exception handler` will ensure that API errors are caught, logged, and returned as standardized JSON responses, preventing server crashes and providing clear error messages to the frontend.
    - **API Dependency:** The application's core functionality (task CRUD) relies on the Supabase API. Intermittent Supabase outages would lead to temporary unavailability of task management features, but the frontend will be designed to communicate this gracefully to the user.
- **Recovery:** Given the use of managed services, primary recovery mechanisms (e.g., database backups, service restoration) are handled by `Vercel` and `Supabase`. Application-level recovery focuses on error reporting and graceful degradation. (Reference: Architecture - Cross-Cutting Concerns: Error Handling, Deployment).

### Observability

### Observability

- **Logging:**
    - **Frontend:** `console.log` will be used for development debugging. For production environments, a remote logging service (e.g., Sentry, Logtail) will be integrated to capture and aggregate client-side errors and warnings.
    - **Backend:** `Python's built-in logging module` will be configured for structured JSON logging. Key events (e.g., API request/response, database operations, error occurrences, user authentication events) will be logged at appropriate levels.
- **Metrics (Future Consideration):**
    - While not part of the MVP for Epic 1, future iterations should consider collecting basic operational metrics such as API request rates, error rates, and latency for critical endpoints.
- **Tracing (Future Consideration):**
    - Distributed tracing for requests across the frontend, backend, and Supabase could be implemented in later stages to improve debugging and performance analysis.
- **Alerting (Future Consideration):**
    - Alerts based on critical error logs or performance deviations would be set up as part of a more mature observability stack. (Reference: Architecture - Cross-Cutting Concerns: Logging).

## Dependencies and Integrations

## Dependencies and Integrations

### Core Technologies

- **Frontend Framework:** Next.js (TypeScript)
    - Integration: `create-next-app@latest` for project scaffolding.
    - Key dependencies: `react`, `react-dom`, `next`.
- **UI Library:** `shadcn/ui` (built on Tailwind CSS)
    - Integration: Manual "copy-paste" integration, configured with `Tailwind CSS`.
- **Backend Framework:** FastAPI (Python)
    - Integration: `uvicorn[standard]` for ASGI server.
    - Key dependencies: `fastapi`, `uvicorn`, `pydantic`.
- **Database & Auth:** Supabase (PostgreSQL, Supabase Auth)
    - Integration (Frontend): `@supabase/supabase-js` for client-side authentication and real-time.
    - Integration (Backend): `supabase-py` for server-side database interaction and RLS enforcement.
- **Deployment:** Vercel
    - Integration: Monorepo deployment with automatic detection of Next.js and FastAPI serverless functions.
    - Version Control: Git (e.g., GitHub, GitLab) for CI/CD integration.

### Libraries & Tools

- **State Management (Frontend):** Zustand (for global state)
- **Styling:** Tailwind CSS (utility-first CSS framework)
- **Data Validation:** Pydantic (for FastAPI request/response models)
- **HTTP Client (Frontend):** Axios (or native `fetch` API)
- **Environment Variables:** `python-dotenv` for local development, Vercel environment variables for production.

### Future Integrations (Out of Scope for Epic 1)

- **AI Service:** Gemini 2.5 Pro API (via `google-generativeai` library in FastAPI)
- **Email Service:** Resend
- **Background Jobs:** Inngest
- **Vector Database:** `pgvector` extension for PostgreSQL


## Acceptance Criteria (Authoritative)

### Acceptance Criteria (Authoritative)

1.  **Project Setup & Deployment:**
    1.1. The monorepo structure (Next.js frontend, FastAPI backend in `api/`) is established locally after initial setup commands.
    1.2. The Next.js frontend successfully deploys to Vercel.
    1.3. The FastAPI app in the `api/` directory successfully deploys as a Vercel serverless function.
    1.4. A "Hello World" endpoint on the deployed FastAPI function is reachable.

2.  **Secure User Task Data Storage:**
    2.1. A new task created via `POST /api/v1/tasks` is saved to the Supabase `tasks` table with the correct `user_id`.
    2.2. When a user requests their tasks, they only receive tasks where `tasks.user_id` matches their authenticated user ID (via RLS).
    2.3. The backend successfully validates the user's session JWT to authorize requests.

3.  **Core Task CRUD - Create & Read:**
    3.1. Using the "Quick Add" (+) button and submitting a task title sends a `POST` request to `/api/v1/tasks` and the new task appears in the UI.
    3.2. Navigating to a task display view triggers a `GET` request to `/api/v1/tasks` to fetch and display all user tasks.
    3.3. The task list and input fields in the UI adhere to the "Hyper-Minimalism" UX principle.

4.  **Core Task CRUD - Update & Delete:**
    4.1. Activating inline edit on an existing task and saving sends a `PUT` request to `/api/v1/tasks/{task_id}` and the task is updated in the UI.
    4.2. Confirming deletion sends a `DELETE` request to `/api/v1/tasks/{task_id}` and the task is removed from the UI.
    4.3. Updates or deletions on one device are reflected immediately on other connected devices viewing the same list.

5.  **Task Completion & Reordering:**
    5.1. Clicking an incomplete task's checkbox sets its `is_completed` status to `true` via `PUT` and updates the UI (including "charging battery" visualization).
    5.2. Dragging and dropping a task to a new position persists the new order in the backend.
    5.3. All interactive elements (checkboxes, drag handles) are clearly labeled and keyboard-accessible for screen reader users.

## Traceability Mapping

### Traceability Mapping

| Acceptance Criteria (AC) | Spec Section(s)                                                                    | Component(s)/API(s)                                                        | Test Idea                                                                                                                                                             |
| :----------------------- | :--------------------------------------------------------------------------------- | :------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.1                      | `architecture-2025-11-28.md` (2. Starter Template, 5. Project Structure)           | Next.js, FastAPI, Python venv, `npx create-next-app`, `pip install`        | Verify monorepo setup locally after running commands.                                                                                                                 |
| 1.2                      | `architecture-2025-11-28.md` (3.1. Deployment)                                     | Vercel, Next.js, FastAPI (serverless)                                      | Deploy "Hello World" app to Vercel and check reachability of frontend and backend.                                                                                      |
| 2.1                      | `architecture-2025-11-28.md` (3.1. Supabase Integration), `prd.md` (FR7)           | FastAPI (`POST /api/v1/tasks`), Supabase (`tasks` table)                   | Create task with authenticated user; verify `user_id` in DB.                                                                                                          |
| 2.2                      | `architecture-2025-11-28.md` (3.1. Supabase Integration), `prd.md` (FR7)           | Supabase (RLS on `tasks` table)                                            | As User A, fetch tasks; verify no User B tasks are returned.                                                                                                            |
| 2.3                      | `architecture-2025-11-28.md` (3.2. Authentication Flow)                            | FastAPI (JWT validation)                                                   | Authenticate with valid JWT; attempt API call; verify success. Authenticate with invalid JWT; verify rejection.                                                         |
| 3.1                      | `prd.md` (FR1), `ux-design-specification.md` (5.1 Quick Task)                      | Frontend (Quick Add button), FastAPI (`POST /api/v1/tasks`)                | Add task via UI; verify `POST` request and task display.                                                                                                                |
| 3.2                      | `prd.md` (FR2)                                                                     | Frontend (Task list component), FastAPI (`GET /api/v1/tasks`)              | Navigate to task list; verify `GET` request and all user tasks are displayed.                                                                                           |
| 3.3                      | `ux-design-specification.md` (2.5. Core Experience Principles, 3.1. Color System)  | Frontend UI components (shadcn/ui, Tailwind CSS)                           | Visually inspect UI elements for adherence to hyper-minimalism.                                                                                                         |
| 4.1                      | `prd.md` (FR3)                                                                     | Frontend (inline edit), FastAPI (`PUT /api/v1/tasks/{task_id}`)            | Edit task title/status in UI; verify `PUT` request and update in DB/UI.                                                                                                 |
| 4.2                      | `prd.md` (FR4), `ux-design-specification.md` (5.1 Focused Task View)               | Frontend (swipe gesture/delete button), FastAPI (`DELETE /api/v1/tasks/{task_id}`) | Initiate task deletion in UI; confirm `DELETE` request and removal from DB/UI.                                                                                          |
| 4.3                      | `prd.md` (FR23), `architecture-2025-11-28.md` (3.1. Supabase Integration)          | Supabase (Realtime), Frontend (subscription logic)                         | Update task on Device A; verify immediate reflection on Device B.                                                                                                       |
| 5.1                      | `prd.md` (FR5)                                                                     | Frontend (checkbox), FastAPI (`PUT /api/v1/tasks/{task_id}`)               | Click checkbox; verify `is_completed` status update in DB/UI and battery visualization.                                                                                 |
| 5.2                      | `prd.md` (FR6)                                                                     | Frontend (drag-and-drop), FastAPI (`PUT /api/v1/tasks/{task_id}`)          | Reorder tasks in UI; verify `sort_order` update in DB.                                                                                                                  |
| 5.3                      | `prd.md` (FR24), `ux-design-specification.md` (8.1 Accessibility)                  | Frontend (ARIA attributes, keyboard navigation)                            | Use screen reader/keyboard to navigate task list; verify proper labeling and accessibility of interactive elements.                                                       |

## Risks, Assumptions, Open Questions

## Risks, Assumptions, Open Questions

**Risks:**
- **R1: Monorepo Setup Complexity:** The initial setup and configuration of the Next.js frontend and FastAPI backend within a Vercel-compatible monorepo might be complex, leading to delays.
    - **Mitigation:** Follow the provided architecture document's starter template decision and implementation patterns precisely. Prioritize verifying the "Hello World" deployment early.
- **R2: Row Level Security Misconfiguration:** Incorrect RLS policies in Supabase could lead to unauthorized data access.
    - **Mitigation:** Thorough testing of RLS (AC 2.2) is critical. Implement strict code reviews for all RLS policies.
- **R3: Real-time Update Performance:** Subscribing to Supabase Realtime might introduce unexpected performance overhead or latency issues under high load.
    - **Mitigation:** Monitor real-time performance. Implement throttling or debouncing if necessary. Optimize Supabase database schema and queries.

**Assumptions:**
- **A1: Supabase Service Availability:** Supabase's managed services (PostgreSQL, Auth, Realtime) will maintain high availability and performance throughout the project lifecycle.
- **A2: Third-Party Library Stability:** Key frameworks and libraries (Next.js, FastAPI, shadcn/ui, Supabase client libraries) will remain stable and well-supported.
- **A3: Vercel Deployment Reliability:** Vercel's platform will reliably deploy and host both the Next.js frontend and FastAPI serverless functions.

**Open Questions:**
- **Q1: Specific Dependency Versions:** While major frameworks are identified, exact dependency versions (e.g., `npx create-next-app@latest` might install a new version, specific Python library versions) need to be explicitly pinned before initial project setup to ensure consistency across development environments.
    - **Next Step:** Validate and pin all major library versions in `package.json` and `requirements.txt` before starting implementation.

## Test Strategy Summary

## Test Strategy Summary

The testing strategy for Epic 1 will focus on ensuring the foundational task management functionality is robust, secure, and performant.

- **Unit Testing:**
    - **Frontend:** Individual React components, utility functions, and API client logic will be tested using `Jest` and `React Testing Library`. Focus on isolated component behavior and pure function correctness.
    - **Backend:** Individual FastAPI endpoints, service functions, and Pydantic models will be tested using `pytest`. Focus on business logic correctness and data validation.
- **Integration Testing:**
    - **Frontend:** Test interactions between connected components and verify correct data flow from API client to UI state.
    - **Backend:** Test the interaction between FastAPI services, database operations (Supabase), and external dependencies (e.g., Supabase authentication). Verify RLS enforcement.
- **End-to-End (E2E) Testing:**
    - Critical user journeys (e.g., user login, task creation, update, deletion, reordering) will be tested using `Playwright`. These tests will simulate user interaction across the full stack (frontend to backend to database) and verify ACs are met.
    - Special attention will be given to real-time updates (AC 4.3) and ensuring changes propagate correctly across simulated clients.
- **Acceptance Criteria (AC) Coverage:** Every acceptance criterion defined in this document will have at least one corresponding test case (unit, integration, or E2E) to verify its implementation.
- **Edge Cases:** Consider testing:
    - Empty task lists, very long task titles.
    - Rapid consecutive updates/deletions.
    - Network connectivity issues (simulated).
    - Invalid authentication tokens.
- **Accessibility Testing:** Manual and automated checks will be performed to ensure adherence to AC 5.3 and other accessibility guidelines, focusing on keyboard navigation and screen reader compatibility. (Reference: Architecture - Cross-Cutting Concerns: Testing Strategy).
