# Story 4.2: AI-Generated Time Estimates

Status: drafted

## Story

As a user,
I want the system to provide AI-generated time estimates for my tasks,
So that I can better plan my day and manage my time blindness (Post-MVP).

## Acceptance Criteria

1.  **AI Time Estimation:**
    1.1. When a task is created or edited, or when the "Plan My Day" AI Workflow is triggered, the FastAPI backend calls the Gemini API for task analysis, and Gemini provides an approximate time estimate (e.g., "15 minutes," "1 hour"). (Covers FR16)

2.  **Display Time Estimate:**
    2.1. Given a task has a time estimate, the estimate is clearly displayed alongside the task title in the UI.

## Tasks / Subtasks

- [ ] **Task 1: Integrate Time Estimation into AI Workflow (AC 1.1)**
  - [ ] Update the AI prompting logic in the backend to request time estimates in a structured format as part of the "Plan My Day" AI Workflow.
  - [ ] Add a new nullable column (e.g., `estimated_time_minutes` as an `integer`) to the `tasks` table to store the estimate.

- [ ] **Task 2: Store and Retrieve Time Estimates (AC 1.1)**
  - [ ] The backend will process the time estimate from the AI response and save it to the new database column.
  - [ ] The main task retrieval endpoint (`GET /api/v1/tasks`) will include the time estimate data.

- [ ] **Task 3: Display Time Estimates in Frontend (AC 2.1)**
  - [ ] Update the frontend task components to display the estimated time for each task, potentially with a simple visual cue.

- [ ] **Task 4: Conduct Testing (AC 1.1, 2.1)**
  - [ ] Write unit tests for the updated AI service to ensure correct time estimate generation and format.
  - [ ] Write integration tests to verify that the estimated time is correctly saved to the database.
  - [ ] Develop integration tests to confirm the frontend accurately retrieves and displays the estimated time.

## Dev Notes

- **Architecture Patterns & Constraints:** This feature extends the existing AI integration. It requires a database schema change and modifications to both the AI service and the frontend components.
- **Project Structure Notes:** This story impacts `api/app/services/ai_service.py` (AI prompting and response), `api/app/main.py` (endpoints), `nextjs-frontend/src/components/TaskList.tsx` (UI display), and a database migration for `estimated_time_minutes` column.
- **Source Tree Components to Touch:**
    - `api/app/services/ai_service.py`: Update AI prompting and response handling.
    - `api/app/main.py`: Ensure endpoints include the new time estimate data.
    - `nextjs-frontend/src/components/TaskList.tsx` or similar: Update UI to display the estimate.
    - Database migration to add the `estimated_time_minutes` column to the `tasks` table.
- **Testing Standards Summary:** Unit tests for the updated AI service. Integration tests to verify the estimate is correctly saved and displayed.

### Learnings from Previous Story

- From Story 4.1: AI Task Breakdown Suggestions, the importance of explicit citations for `architecture.md`, and `test-design-system-2025-11-28.md` was highlighted. Also, the need for explicit testing subtasks and a populated "Dev Agent Record" was identified.

### References

- [Source: `docs/epics.md` - Epic 4, Story 4.2]
- [Source: `docs/architecture-2025-11-28.md`]
- [Source: `docs/test-design-system-2025-11-28.md`]
- [Covers FR16]

## Dev Agent Record

### Context Reference

- docs/sprint-artifacts/4-2-ai-generated-time-estimates.context.xml

### Agent Model Used

{{agent_model_name_version}}

### Debug Log References

### Completion Notes List

### File List

## Change Log

- **YYYY-MM-DD:** Initial draft created by {{agent_model_name_version}}.
