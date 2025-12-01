# Story 2.3: Filter Tasks by Smart Labels

Status: done

## Story

As a user,
I want to filter my tasks by their smart labels,
so that I can quickly find and focus on specific categories of tasks.

## Acceptance Criteria

1.  Given I have tasks with AI-generated labels, when I click on a "work" label tag in the UI, then the frontend makes a `GET` request to `/api/v1/tasks?label=work`.
2.  Given the API returns a filtered list of tasks, when the UI updates, then only tasks with the "work" label are displayed. (Covers FR10)
3.  Given a filter is active, when I click a "Clear" or "All" button, then a `GET` request is made to `/api/v1/tasks` and all tasks are displayed again.

## Tasks / Subtasks

- [ ] **Task 1: Backend - Enhance `GET /api/v1/tasks` Endpoint** (AC 1, 2)
  - [ ] Modify the endpoint to accept an optional `label` query parameter.
  - [ ] Implement logic to perform a join with `task_labels` and `labels` tables to filter tasks by label name.
- [ ] **Task 2: Frontend - UI for Filtering** (AC 1, 3)
  - [ ] Display unique labels from the user's tasks in the UI (e.g., as a list of clickable tags).
  - [ ] Implement a "Clear" or "All" button to remove the active filter.
- [ ] **Task 3: Frontend - State Management for Filtering** (AC 1, 2, 3)
  - [ ] Manage the state of the current filter in the frontend's state management (Zustand).
  - [ ] Trigger API calls with the appropriate query parameter when a label is clicked or the filter is cleared.
  - [ ] Update the displayed task list based on the API response.
- [ ] **Task 4: Testing**
  - [ ] Write integration tests for the `GET /api/v1/tasks` endpoint with the `label` query parameter.
  - [ ] Write frontend tests to verify that clicking labels triggers the correct API calls and updates the UI.

## Dev Notes

-   **Relevant architecture patterns and constraints**: The `GET /api/v1/tasks` endpoint will be enhanced to accept an optional `label` query parameter. The state of the current filter must be managed in the frontend's state.
-   **Source tree components to touch**:
    - **Backend (`api/`)**:
        - `app/services/task.py`: Modify to handle filtering logic.
        - `app/repositories/task.py`: Update to include filtering in the database query.
    - **Frontend (`nextjs-frontend/src/`)**:
        - `components/tasks/TaskList.tsx`: Modify to display filter options and filtered list.
        - `lib/api.ts`: Update API client to handle the `label` query parameter.
        - State management store for tasks (`zustand`): Add state for the current filter.
-   **Testing standards summary**: Integration tests for the backend endpoint and frontend component tests for the filtering UI and logic.

### Project Structure Notes

- This story will primarily involve enhancing existing components and services from Epic 1 and previous Epic 2 stories.

### References

- [Source: docs/epics.md#Story-2.3:-Filter-Tasks-by-Smart-Labels]
- [Source: docs/architecture-2025-11-28.md#4.4-API-Design]
- [Source: docs/sprint-artifacts/tech-spec-epic-2.md#2.3-Filter-Tasks-by-Smart-Labels]

## Dev Agent Record

### Context Reference

<!-- Path(s) to story context XML will be added here by context workflow -->

### Agent Model Used

gemini-1.5-flash

### Debug Log References

### Completion Notes List

### File List
