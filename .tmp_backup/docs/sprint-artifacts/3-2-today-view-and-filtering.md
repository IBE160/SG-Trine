# Story 3.2: "Today" View and Filtering

Status: drafted

## Story

As a user,
I want to see a dedicated "Today" view as the default screen,
So that I can immediately focus on my most urgent daily tasks (Post-MVP).

## Acceptance Criteria

1.  **Default View:**
    1.1. When the application loads, the default view presented is the "Proactive Dashboard" which contains the "Today" view. (Covers FR12)

2.  **Curated Task List:**
    2.1. When the "Today" view is active, the list of tasks shown is a curated list of tasks scheduled for the current day.

3.  **Core Functionality Availability:**
    3.1. When interacting with the "Today" view, all core task management functionalities (add, edit, complete a task) are available.

## Tasks / Subtasks

- [ ] **Task 1: Implement "Today" View as Default (AC 1.1)**
  - [ ] Configure the main application route to display the "Proactive Dashboard" containing the "Today" view by default.
  - [ ] Ensure initial data fetch for tasks is filtered for the current day.

- [ ] **Task 2: Develop Task Filtering for "Today" (AC 2.1)**
  - [ ] Enhance the `GET /api/v1/tasks` endpoint to support a date-based filter (e.g., `?date=today`).
  - [ ] Implement frontend logic to call the filtered API endpoint for the "Today" view.

- [ ] **Task 3: Ensure Core Task Management in "Today" View (AC 3.1)**
  - [ ] Verify that adding new tasks from the "Today" view correctly saves them with the current day's schedule.
  - [ ] Confirm that editing and completing tasks within the "Today" view updates the backend correctly and reflects in the UI.

- [ ] **Task 4: Conduct Testing (AC 1.1, 2.1, 3.1)**
  - [ ] Write unit tests for the backend API endpoint for date-based filtering.
  - [ ] Write integration tests to ensure the frontend correctly displays filtered tasks.
  - [ ] Manually test all core task management functionalities (add, edit, complete) within the "Today" view.

## Dev Notes

- **Architecture Patterns & Constraints:** This story involves both frontend and backend changes. The backend needs to support date-based filtering for tasks, and the frontend needs to integrate this filtering into the default view.
- **Project Structure Notes:** This story impacts `nextjs-frontend/src/app/page.tsx`, `nextjs-frontend/src/components/TodayView.tsx`, and `api/app/main.py`.
- **Source Tree Components to Touch:**
    - `nextjs-frontend/src/app/page.tsx`: The main page component for the "Proactive Dashboard".
    - `nextjs-frontend/src/components/TodayView.tsx`: New component for rendering today's tasks.
    - `api/app/main.py`: Modifications to the task retrieval endpoint.
- **Testing Standards Summary:** Unit tests for backend filtering logic. Integration tests to ensure frontend correctly displays filtered tasks and core functionalities work.

### Learnings from Previous Story

- From Story 3.1: Minimalist User Interface, the importance of explicit citations for `epics.md`, `architecture.md`, and `test-design-system-2025-11-28.md` was highlighted. Also, the need for explicit testing subtasks and a populated "Dev Agent Record" was identified.

### References

- [Source: `docs/epics.md` - Epic 3, Story 3.2]
- [Source: `docs/architecture-2025-11-28.md`]
- [Source: `docs/test-design-system-2025-11-28.md`]
- [Covers FR12]

## Dev Agent Record

### Context Reference

- docs/sprint-artifacts/3-2-today-view-and-filtering.context.xml

### Agent Model Used

{{agent_model_name_version}}

### Debug Log References

### Completion Notes List

### File List


- **YYYY-MM-DD:** Initial draft created by {{agent_model_name_version}}.
