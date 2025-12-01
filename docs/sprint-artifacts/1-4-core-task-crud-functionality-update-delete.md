# Story 1.4: Core Task CRUD Functionality (Update, Delete)

Status: done

## Story

As a user,
I want to edit and delete my existing tasks,
so that I can maintain an accurate and clutter-free task list.

## Acceptance Criteria

1.  **Given** I have an existing task,
    **When** I activate the inline edit function and save,
    **Then** a `PUT` request is sent to `/api/v1/tasks/{task_id}` and the task is updated. (Covers FR3)
2.  **And** Given I am in the "Focused Task View",
    **When** I swipe the task card away,
    **Then** the task is marked for deletion.
3.  **And** Given a task is marked for deletion,
    **When** the action is confirmed,
    **Then** a `DELETE` request is sent to `/api/v1/tasks/{task_id}` and the task is removed. (Covers FR4)
4.  **And** Given a task is updated or deleted,
    **When** another connected device is viewing the same list,
    **Then** the change is reflected immediately without a manual refresh. (Covers FR23)

## Tasks / Subtasks

- [ ] **Frontend: Implement Inline Edit Functionality**
  - [ ] Develop UI components for inline editing of task titles.
  - [ ] Integrate save/cancel actions for inline edit.
- [ ] **Frontend: Implement Swipe-to-Delete Gesture (Focused Task View)**
  - [ ] Develop UI/UX for swiping a task card to mark for deletion.
  - [ ] Implement visual feedback for deletion state.
- [ ] **Frontend: Implement Delete Confirmation Dialog**
  - [ ] Create a confirmation dialog for task deletion.
- [ ] **Frontend: Integrate API Calls for Update**
  - [ ] Send `PUT /api/v1/tasks/{task_id}` with updated data (`title`, `is_completed`, `sort_order`).
  - [ ] Handle API response and update UI state.
- [ ] **Frontend: Integrate API Calls for Delete**
  - [ ] Send `DELETE /api/v1/tasks/{task_id}` upon confirmation.
  - [ ] Handle API response and remove task from UI state.
- [ ] **Frontend: Implement Real-time Updates via Supabase Subscriptions**
  - [ ] Subscribe to Supabase Realtime changes for the `tasks` table.
  - [ ] Update local task list state when `UPDATE` or `DELETE` events are received.
- [ ] **Backend: Implement `PUT /api/v1/tasks/{task_id}` Endpoint**
  - [ ] Create FastAPI endpoint to handle task updates.
  - [ ] Validate request body using Pydantic `TaskUpdate` model.
  - [ ] Update task in Supabase, ensuring user ownership.
- [ ] **Backend: Implement `DELETE /api/v1/tasks/{task_id}` Endpoint**
  - [ ] Create FastAPI endpoint to handle task deletions.
  - [ ] Delete task from Supabase, ensuring user ownership.
- [ ] **Testing:** Write unit/integration tests for frontend components.
- [ ] **Testing:** Write unit/integration tests for backend API endpoints.
- [ ] **Testing:** Write E2E tests for update and delete user flows.

## Dev Notes

-   **Relevant architecture patterns and constraints:**
    *   API design (`PUT /api/v1/tasks/{task_id}`, `DELETE /api/v1/tasks/{task_id}`) as defined in `docs/architecture-2025-11-28.md` and `docs/sprint-artifacts/tech-spec-epic-1.md`.
    *   Real-time updates via Supabase subscriptions as outlined in `docs/architecture-2025-11-28.md` (3.1. Supabase Integration).
    *   Frontend state management with Zustand for task list updates.
-   **Source tree components to touch:**
    *   `nextjs-frontend/src/components/tasks/*`: Task display components for inline editing.
    *   `nextjs-frontend/src/lib/api/*`: API client for PUT/DELETE calls.
    *   `api/app/api/v1/endpoints/tasks.py`: FastAPI endpoints for update and delete.
    *   `api/app/services/task_service.py`: Backend logic for interacting with Supabase.
-   **Testing standards summary:** Follow `pytest` for backend unit/integration tests, `Jest`/`React Testing Library` for frontend unit/integration tests, and `Playwright` for E2E tests, as per `docs/architecture-2025-11-28.md`.

### Project Structure Notes

-   Alignment with unified project structure: The `nextjs-frontend` and `api` directories will contain the respective codebase components.
-   Frontend components will follow `PascalCase` for files and components. Python backend will use `snake_case` for variables.

### References

-   [Source: docs/epics.md#Story-1.4:-Core-Task-CRUD-Functionality-(Update,-Delete)]
-   [Source: docs/architecture-2025-11-28.md#3.1.-Critical-Architectural-Decisions]
-   [Source: docs/sprint-artifacts/tech-spec-epic-1.md#APIs-and-Interfaces]

## Dev Agent Record

### Context Reference

<!-- Path(s) to story context XML will be added here by context workflow -->

### Agent Model Used

gemini-1.5-flash

### Debug Log References

### Completion Notes List

### File List
