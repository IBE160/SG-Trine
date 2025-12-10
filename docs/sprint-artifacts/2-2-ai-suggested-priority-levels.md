# Story 2.2: AI-Suggested Priority Levels

Status: done

## Story

As a user,
I want the system to automatically suggest a priority level for my tasks,
so that I can focus on what's most important and reduce decision fatigue.

## Acceptance Criteria

1.  **Given** I create or edit a task, when the backend saves the task, then it asynchronously calls the Gemini API with a structured prompt for priority suggestion.
2.  **And** Given the Gemini API returns a valid priority level (e.g., an integer from 1 to 4), when the backend processes the response, then the `priority` field is updated on the `tasks` table.
3.  **And** Given a task has a suggested priority, when the frontend displays the task, then the priority is clearly indicated (e.g., with a colored icon or border).

## Tasks / Subtasks

- [ ] **Task 1: Backend - Database Schema Update** (AC 2)
  - [ ] Add `priority` column (`INTEGER`) to the `tasks` table.
  - [ ] Create and run Supabase migration script if necessary.
- [ ] **Task 2: Backend - AI Integration Service Enhancement** (AC 1, 2)
  - [ ] Enhance `AIService` to include a function that takes task details and returns a suggested priority level using the Gemini API.
  - [ ] Ensure the prompt asks for a numerical priority within a defined range (e.g., 1-4).
  - [ ] Implement error handling and fallbacks for the Gemini API call for priority suggestions.
- [ ] **Task 3: Backend - Task Creation/Update Workflow Enhancement** (AC 1, 2)
  - [ ] Modify the existing task creation/update logic (from Story 2.1) to asynchronously call the `AIService` for priority suggestions.
  - [ ] On successful priority generation, save the priority to the `tasks` table.
- [ ] **Task 4: Frontend - Display Priority** (AC 3)
  - [ ] Modify the `Task` component to display the priority level.
  - [ ] Style the priority using visual cues (e.g., colored icons or borders) to represent different priority levels.
- [ ] **Task 5: Testing**
  - [ ] Write unit tests for the enhanced `AIService` priority suggestion functionality.
  - [ ] Write integration tests to verify that priority is correctly generated and saved when a task is created or updated.
  - [ ] Write frontend tests to verify that priority is displayed correctly.

## Dev Notes

-   **Relevant architecture patterns and constraints**: All calls to the Gemini 2.5 Pro API **MUST** be made from the FastAPI backend to protect the API key. The `priority` column in the `tasks` table will store the AI-suggested value (integer from 1 to 4).
-   **Source tree components to touch**:
    - **Backend (`api/`)**:
        - `app/models/task.py`: Update Task model to include `priority` field.
        - `app/services/ai_service.py`: Enhance for priority suggestion.
        - `app/services/task.py`: Modify to integrate priority suggestion.
        - `app/repositories/task.py`: Update for saving priority.
    - **Frontend (`nextjs-frontend/src/`)**:
        - `components/tasks/TaskCard.tsx`: Modify to display priority.
-   **Testing standards summary**: Unit tests for backend AI service, integration tests for task creation with priority generation, and frontend component tests for priority display.

### Project Structure Notes

- This story will enhance existing AI integration services and task models established in Epic 1 and Story 2.1.

### References

- [Source: docs/epics.md#Story-2.2:-AI-Suggested-Priority-Levels]
- [Source: docs/architecture-2025-11-28.md#3.1.-Critical-Architectural-Decisions] (AI Integration)
- [Source: docs/sprint-artifacts/tech-spec-epic-2.md#2.2.-AI-Suggested-Priority-Levels]

## Dev Agent Record

### Context Reference

<!-- Path(s) to story context XML will be added here by context workflow -->

### Agent Model Used

gemini-1.5-flash

### Debug Log References

### Completion Notes List

### File List
