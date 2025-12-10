# Story 4.6: Scheduled Task Management

Status: drafted

## Story

As a user,
I want to schedule tasks for specific days,
So that I can plan my workload and manage my commitments effectively (Post-MVP).

## Acceptance Criteria

1.  **Task Scheduling:**
    1.1. When editing a task, I can assign a specific `scheduled_date` to it via a UI date picker. (Covers FR20)

2.  **Display of Scheduled Tasks:**
    2.1. When tasks are scheduled, they are prominently displayed in relevant views (e.g., "Today" view on the "Proactive Dashboard") on their scheduled day.

## Tasks / Subtasks

- [ ] **Task 1: Add Date Picker to Task Editing UI (AC 1.1)**
  - [ ] Implement a date picker component (e.g., from `shadcn/ui`) in the task editing interface.
  - [ ] When a date is selected, the frontend will send the updated `scheduled_date` to the backend.

- [ ] **Task 2: Update Backend to Support Scheduled Dates (AC 1.1)**
  - [ ] Add a new nullable `scheduled_date` column (`timestamp with time zone`) to the `tasks` table.
  - [ ] The `PUT /api/v1/tasks/{task_id}` endpoint will be updated to handle the `scheduled_date` field.

- [ ] **Task 3: Filter Tasks by Scheduled Date (AC 2.1)**
  - [ ] The "Today" view will be updated to filter and display tasks based on their `scheduled_date`.
  - [ ] The `GET /api/v1/tasks` endpoint will be enhanced to filter by `scheduled_date`.

## Dev Notes

- **Architecture Patterns & Constraints:** This feature requires a database schema change and modifications to both frontend and backend to handle date-based scheduling.
- **Source Tree Components to Touch:**
    - `nextjs-frontend/src/components/TaskEditor.tsx`: Add date picker.
    - `nextjs-frontend/src/app/page.tsx`: Update "Today" view logic.
    - `api/app/main.py`: Update task update and retrieval endpoints.
    - Database migration to add the `scheduled_date` column to the `tasks` table.
- **Testing Standards Summary:** Unit tests for backend logic handling `scheduled_date`. Integration tests for the date picker functionality and the display of scheduled tasks.

### References

- [Source: `docs/epics.md` - Story 4.6]
- [Covers FR20]

## Change Log
