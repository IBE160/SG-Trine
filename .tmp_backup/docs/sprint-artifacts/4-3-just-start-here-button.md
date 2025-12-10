# Story 4.3: "Just Start Here" Button

Status: drafted

## Story

As a user,
I want to click a "Just Start Here" button to be directed to the single most important task,
So that I can overcome decision paralysis and initiate work immediately (Post-MVP).

## Acceptance Criteria

1.  **"Just Start Here" Request:**
    1.1. When I click the prominent "Just Start Here" button on the "Proactive Dashboard," the frontend makes a `GET` request to a backend endpoint (e.g., `/api/v1/tasks/next-priority`).

2.  **Transition to Focused Task View:**
    2.1. Given the backend applies AI logic to identify the highest priority task, the frontend receives this task and the UI transitions to a "Focused Task View" for that specific task. (Covers FR17)

## Tasks / Subtasks

- [ ] **Task 1: Develop Backend Logic for Next Priority Task (AC 2.1)**
  - [ ] Create a new FastAPI endpoint (`GET /api/v1/tasks/next-priority`).
  - [ ] Implement AI logic in this endpoint to determine the "best" task to work on, considering factors like `priority`, `due_date`, and `estimated_time_minutes`.

- [ ] **Task 2: Implement "Just Start Here" Button in Frontend (AC 1.1)**
  - [ ] Create a prominent "Just Start Here" button on the "Proactive Dashboard".
  - [ ] When clicked, this button will trigger the API call to the `/api/v1/tasks/next-priority` endpoint.

- [ ] **Task 3: Implement UI Transition to Focused Task View (AC 2.1)**
  - [ ] Upon receiving the next priority task from the backend, the frontend will smoothly transition the UI to the "Focused Task View" for that specific task.

- [ ] **Task 4: Conduct Testing (AC 1.1, 2.1)**
  - [ ] Write unit tests for the backend logic that determines the next priority task.
  - [ ] Develop E2E tests for the full user flow: clicking the "Just Start Here" button, transitioning to the focused view, and verifying the correct task is displayed.

## Dev Notes

- **Architecture Patterns & Constraints:** This feature combines frontend UI/UX with backend AI logic. The core challenge is defining the algorithm for "most important task."
- **Project Structure Notes:** This story impacts `api/app/main.py` (new endpoint for `next-priority`), `nextjs-frontend/src/app/page.tsx` (for the button), and `nextjs-frontend/src/app/[taskId]/page.tsx` (for the focused view).
- **Source Tree Components to Touch:**
    - `api/app/main.py`: New endpoint for identifying the next priority task.
    - `nextjs-frontend/src/app/page.tsx`: To host the "Just Start Here" button.
    - `nextjs-frontend/src/app/[taskId]/page.tsx`: The "Focused Task View" to transition to.
- **Testing Standards Summary:** Unit tests for the backend "next priority" logic. E2E tests for the full user flow: clicking the button, transitioning to the focused view, and verifying the correct task is displayed.

### Learnings from Previous Story

- From Story 4.2: AI-Generated Time Estimates, the importance of explicit citations for `architecture.md`, and `test-design-system-2025-11-28.md` was highlighted. Also, the need for explicit testing subtasks and a populated "Dev Agent Record" was identified.

### References

- [Source: `docs/epics.md` - Epic 4, Story 4.3]
- [Source: `docs/architecture-2025-11-28.md`]
- [Source: `docs/test-design-system-2025-11-28.md`]
- [Covers FR17]

## Dev Agent Record

### Context Reference

- docs/sprint-artifacts/4-3-just-start-here-button.context.xml

### Agent Model Used

{{agent_model_name_version}}

### Debug Log References

### Completion Notes List

### File List


- **YYYY-MM-DD:** Initial draft created by {{agent_model_name_version}}.
