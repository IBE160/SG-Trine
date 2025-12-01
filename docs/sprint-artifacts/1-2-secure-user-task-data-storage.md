# Story 1.2: Secure User Task Data Storage

Status: done

## Story

As a user,
I want my task data to be securely stored and managed in a backend,
so that my information is persistent and protected.

## Acceptance Criteria

1.  Given a user is authenticated, when a new task is created via a `POST /api/v1/tasks` request, then the task is saved to the `tasks` table in the Supabase database with the correct `user_id`. (Covers FR7)
2.  Given the `tasks` table has Row Level Security (RLS) enabled, when a user requests their tasks, then they only receive tasks where `tasks.user_id` matches their authenticated user ID. (Covers FR7)
3.  Given a user is signed in on the frontend, when their session JWT is sent to the backend, then the backend successfully validates the JWT to authorize the request. (Covers FR7)

## Tasks / Subtasks

- [ ] **Task 1: Implement Database Schema Changes** (AC 1)
  - [ ] Add `user_id` column (`UUID`, `NOT NULL`, `REFERENCES users(id) ON DELETE CASCADE`) to the `tasks` table. [Source: `epics.md#Story-1.2:-Secure-User-Task-Data-Storage`, `tech-spec-epic-1.md#Data-Models-and-Contracts`]
  - [ ] Ensure `user_id` is automatically populated from the authenticated user's ID during task creation.
  - [ ] (Optional) Create and run Supabase migration script for schema update.

- [ ] **Task 2: Configure Supabase Row Level Security (RLS)** (AC 2)
  - [ ] Enable RLS on the `tasks` table. [Source: `epics.md#Story-1.2:-Secure-User-Task-Data-Storage`, `tech-spec-epic-1.md#Security`]
  - [ ] Create RLS policy for `SELECT` operations: Allow `users` to `SELECT` `tasks` where `user_id = auth.uid()`.
  - [ ] Create RLS policy for `INSERT` operations: Allow `users` to `INSERT` `tasks` where `user_id = auth.uid()`.
  - [ ] Create RLS policy for `UPDATE` operations: Allow `users` to `UPDATE` `tasks` where `user_id = auth.uid()`.
  - [ ] Create RLS policy for `DELETE` operations: Allow `users` to `DELETE` `tasks` where `user_id = auth.uid()`.
  - [ ] Verify RLS policies (Dev Note: Unit test or manual verification).

- [ ] **Task 3: Implement Backend JWT Validation & User Extraction** (AC 3)
  - [ ] Create a FastAPI dependency (`get_current_user` or similar) that extracts the JWT from the `Authorization` header. [Source: `epics.md#Story-1.2:-Secure-User-Task-Data-Storage`, `architecture-2025-11-28.md#3.2.-Authentication-Flow`]
  - [ ] Use `supabase-py` to verify the JWT and extract the `user_id`. [Source: `epics.md#Story-1.2:-Secure-User-Task-Data-Storage`]
  - [ ] Apply this dependency to protected endpoints (e.g., `POST /api/v1/tasks`, `GET /api/v1/tasks`).

- [ ] **Task 4: Frontend Integration for Authentication**
  - [ ] Ensure `@supabase/supabase-js` is configured to manage user sessions and retrieve JWTs. [Source: `epics.md#Story-1.2:-Secure-User-Task-Data-Storage`, `architecture-2025-11-28.md#3.1.-Supabase-Integration`]
  - [ ] Configure the frontend's API client (e.g., Axios instance) to automatically include the valid JWT in the `Authorization` header for all requests to the FastAPI backend.

- [ ] **Task 5: Update `POST /api/v1/tasks` Endpoint** (AC 1)
  - [ ] Modify the `create_task` endpoint in FastAPI to receive `user_id` from the JWT validation dependency, not from the request body.
  - [ ] Ensure the `user_id` is passed correctly to the `TaskRepository` for task creation.

- [ ] **Task 6: Basic Testing**
  - [ ] Write unit tests for the FastAPI JWT validation dependency.
  - [ ] Write integration tests for `POST /api/v1/tasks` and `GET /api/v1/tasks` to verify tasks are saved with the correct `user_id` and retrieved only by the owning user.
  - [ ] Write E2E tests using `Playwright` to simulate a user logging in, creating a task, and then verifying that another (non-owner) user cannot view that task. [Source: `tech-spec-epic-1.md#Test-Strategy-Summary`]

## Dev Notes



-   **Relevant architecture patterns and constraints**: This story relies heavily on the Supabase integration model, particularly the enforcement of Row Level Security (RLS) on the `tasks` table to ensure data isolation. Backend JWT validation, as defined in the architecture, is critical for securely identifying the user and applying RLS.

-   **Source tree components to touch**:

    -   **Backend (`api/`)**:

        -   `app/main.py`: To register new authentication dependencies on task-related endpoints.

        -   `app/dependencies.py`: (New file or modification) To implement JWT extraction and validation.

        -   `app/models/task.py`: To add `user_id` to the `Task` model and define database schema changes.

        -   `app/services/task.py`: To ensure `user_id` is passed correctly to the repository during task creation/retrieval.

        -   `app/repositories/task.py`: (New file or modification) To handle direct database interactions.

        -   `api/` (root): For setting up the Python virtual environment and installing `supabase-py`.

    -   **Frontend (`nextjs-frontend/src/`)**:

        -   API client configuration (`lib/api.ts` or similar): To include JWT in `Authorization` headers.

        -   Authentication context/service: To manage user sessions and acquire JWT from `@supabase/supabase-js`.

        -   Task creation/listing components: To ensure tasks are only displayed/managed by the authenticated user.

-   **Testing standards summary**: Unit tests for FastAPI authentication dependencies and RLS policies (if possible via `supabase-py` or direct SQL). Integration tests for FastAPI endpoints to verify secure data storage and retrieval. E2E tests using `Playwright` to simulate user login, task creation, and data isolation.



### Project Structure Notes



-   **Alignment with unified project structure:** This story builds directly on the foundational work of Story 1.1, leveraging the established monorepo structure, FastAPI backend, and Supabase integration. The `api/` directory structure for services, models, and API routers (as defined in [Source: `architecture-2025-11-28.md#5.-Project-Structure`]) will be followed for implementing data storage and authentication logic. Frontend components will integrate with the backend via the established API communication patterns, using a type-safe API client.

-   **Detected conflicts or variances:** None. This story continues to build upon the existing framework.



### References



-   [Source: `architecture-2025-11-28.md#3.1.-Critical-Architectural-Decisions`] (Database Schema, Supabase Integration)

-   [Source: `architecture-2025-11-28.md#3.2.-Important-Architectural-Decisions`] (Authentication Flow)

-   [Source: `architecture-2025-11-28.md#4.-Cross-Cutting-Concerns`] (Testing Strategy, Error Handling)

-   [Source: `epics.md#Story-1.2:-Secure-User-Task-Data-Storage`]

-   [Source: `tech-spec-epic-1.md#2.-Secure-User-Task-Data-Storage`]

## Dev Agent Record

### Context Reference

- docs/sprint-artifacts/1-2-secure-user-task-data-storage.context.xml

### Agent Model Used

{{agent_model_name_version}}

### Debug Log References

### Completion Notes List

### File List
