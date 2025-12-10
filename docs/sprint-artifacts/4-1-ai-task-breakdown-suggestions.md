# Story 4.1: AI Task Breakdown Suggestions

Status: drafted

## Story

As a user,
I want the system to suggest breaking down large tasks into smaller sub-steps,
So that I can reduce overwhelm and make daunting tasks manageable (Post-MVP).

## Acceptance Criteria

1.  **AI Sub-step Generation:**
    1.1. Given an unstructured task (e.g., "Plan my vacation") and triggering the "Plan My Day" AI Workflow, the FastAPI backend orchestrates an AI call to Gemini 2.5 Pro, which generates a list of smaller, actionable sub-steps. (Covers FR15)

2.  **Sub-step Integration:**
    2.1. Given these sub-steps are presented to the user in the UI, and the user confirms them, they are added to the `tasks` table with their `parent_task_id` linked to the original larger task.

## Tasks / Subtasks

- [ ] **Task 1: Implement AI Task Decomposition Logic in Backend (AC 1.1)**
  - [ ] Create a dedicated endpoint (e.g., `POST /api/v1/tasks/{task_id}/breakdown`) in FastAPI.
  - [ ] This endpoint will construct a detailed prompt for Gemini 2.5 Pro to perform task decomposition as part of the "Plan My Day" AI Workflow.

- [ ] **Task 2: Handle AI Response and Database Integration (AC 2.1)**
  - [ ] The backend will process the list of sub-steps returned by the AI.
  - [ ] On user confirmation, the sub-steps will be saved to the `tasks` table with the correct `parent_task_id`.
  - [ ] Ensure the `tasks` table schema supports the `parent_task_id` for hierarchical relationships.

- [ ] **Task 3: Develop Frontend UI for Sub-step Confirmation (AC 2.1)**
  - [ ] Create a UI to present the suggested sub-steps to the user.
  - [ ] Implement a confirmation mechanism (e.g., a button) that triggers the backend to save the sub-steps.

- [ ] **Task 4: Conduct Testing (AC 1.1, 2.1)**
  - [ ] Write unit tests for the AI prompting logic to ensure accurate sub-step generation.
  - [ ] Write unit tests for database integration, verifying correct `parent_task_id` assignment.
  - [ ] Develop integration tests for the end-to-end flow from triggering breakdown to sub-step display and saving.

## Dev Notes

- **Architecture Patterns & Constraints:** This feature is a key part of the "Plan My Day" AI Workflow. It requires backend-heavy logic for AI prompting and database updates for hierarchical task structures.
- **Project Structure Notes:** This story impacts `api/app/main.py` (new endpoint), `api/app/services/ai_service.py` (AI interaction logic), `nextjs-frontend/src/components/TaskBreakdownView.tsx` (new component), and potentially a database migration to add `parent_task_id`.
- **Source Tree Components to Touch:**
    - `api/app/main.py`: New endpoint for task breakdown.
    - `api/app/services/ai_service.py`: Logic for interacting with the Gemini API.
    - `nextjs-frontend/src/components/TaskBreakdownView.tsx`: New component to display and confirm sub-steps.
    - Database migration to ensure `parent_task_id` exists on the `tasks` table.
- **Testing Standards Summary:** Unit tests for the AI prompting logic and the database integration. Integration tests for the end-to-end flow from the user triggering the breakdown to the sub-steps appearing in their task list.

### References

- [Source: `docs/epics.md` - Epic 4, Story 4.1]
- [Source: `docs/architecture-2025-11-28.md`]
- [Source: `docs/test-design-system-2025-11-28.md`]
- [Covers FR15]

## Dev Agent Record

### Context Reference

- docs/sprint-artifacts/4-1-ai-task-breakdown-suggestions.context.xml

### Agent Model Used

{{agent_model_name_version}}

### Debug Log References

### Completion Notes List

### File List

## Change Log

- **YYYY-MM-DD:** Initial draft created by {{agent_model_name_version}}.
