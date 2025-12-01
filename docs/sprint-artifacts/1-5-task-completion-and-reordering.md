# Story 1.5: Task Completion and Reordering

Status: done

## Story

As a user,
I want to mark tasks as complete and reorder them,
so that I can manage my progress and prioritize visually.

## Acceptance Criteria

1.  **Given** I have an incomplete task,
    **When** I click its checkbox,
    **Then** the task's `is_completed` status is set to `true` via a `PUT` request, and the UI updates. (Covers FR5)
    **And** The "charging battery" progress visualization for the list updates to reflect the completion.
2.  **And** Given I have multiple tasks in a list,
    **When** I drag and drop a task to a new position,
    **Then** the new order is persisted in the backend. (Covers FR6)
3.  **And** Given I am using a screen reader,
    **When** I navigate to the task list,
    **Then** all interactive elements (checkboxes, drag handles) are clearly labeled and keyboard-accessible. (Covers FR24)

## Tasks / Subtasks

- [ ] **Frontend: Implement Task Completion Checkbox**
  - [ ] Develop UI for a checkbox to toggle task `is_completed` status.
  - [ ] Integrate API call to `PUT /api/v1/tasks/{task_id}` for status update.
- [ ] **Frontend: Implement "Charging Battery" Visualization**
  - [ ] Develop UI component to visually represent task completion progress.
- [ ] **Frontend: Implement Drag-and-Drop Reordering**
  - [ ] Use a library like `react-beautiful-dnd` or `dnd-kit`.
  - [ ] Integrate API call to `PUT /api/v1/tasks/{task_id}` for `sort_order` update.
  - [ ] Handle optimistic UI updates during drag-and-drop.
- [ ] **Frontend: Ensure Accessibility for Reordering and Completion**
  - [ ] Add ARIA attributes to interactive elements (checkboxes, drag handles).
  - [ ] Ensure keyboard navigation and operation for task completion and reordering.
- [ ] **Backend: Enhance `PUT /api/v1/tasks/{task_id}` Endpoint**
  - [ ] Allow updating `is_completed` status.
  - [ ] Allow updating `sort_order`.
  - [ ] Add `sort_order` column to the `tasks` table if not already present.
- [ ] **Testing:** Write unit/integration tests for frontend components (checkbox, drag-and-drop).
- [ ] **Testing:** Write unit/integration tests for backend `PUT` endpoint functionality related to completion and reordering.
- [ ] **Testing:** Write E2E tests for task completion and reordering user flows.
- [ ] **Testing:** Conduct accessibility audit for completion and reordering features.

## Dev Notes

-   **Relevant architecture patterns and constraints:**
    *   API design (`PUT /api/v1/tasks/{task_id}`) for updating `is_completed` and `sort_order` as defined in `docs/architecture-2025-11-28.md` and `docs/sprint-artifacts/tech-spec-epic-1.md`.
    *   `sort_order` will be a new column in the `tasks` table for persisting user-defined order.
-   **Source tree components to touch:**
    *   `nextjs-frontend/src/components/tasks/*`: Task list components, individual task items.
    *   `nextjs-frontend/src/lib/api/*`: API client for PUT calls.
    *   `api/app/api/v1/endpoints/tasks.py`: FastAPI endpoint for task update.
    *   `api/app/services/task_service.py`: Backend logic for interacting with Supabase.
-   **Testing standards summary:** Follow `pytest` for backend, `Jest`/`React Testing Library` for frontend, and `Playwright` for E2E tests, including specific attention to accessibility testing (WCAG 2.1 AA standards).

### Project Structure Notes

-   Frontend components for drag-and-drop should be placed logically within the task components.
-   Backend schema migration for `sort_order` column will be required.

### References

-   [Source: docs/epics.md#Story-1.5:-Task-Completion-and-Reordering]
-   [Source: docs/architecture-2025-11-28.md#3.1.-Critical-Architectural-Decisions]
-   [Source: docs/sprint-artifacts/tech-spec-epic-1.md#APIs-and-Interfaces]
-   [Source: docs/epics.md#FR24]

## Dev Agent Record

### Context Reference

<!-- Path(s) to story context XML will be added here by context workflow -->

### Agent Model Used

gemini-1.5-flash

### Debug Log References

### Completion Notes List

### File List
