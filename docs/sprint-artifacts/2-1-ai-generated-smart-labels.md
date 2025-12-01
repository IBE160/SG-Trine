# Story 2.1: AI-Generated Smart Labels

Status: done

## Story

As a user,
I want the system to automatically generate smart labels for my tasks,
so that I can quickly categorize and understand my tasks at a glance.

## Acceptance Criteria

1.  Given I create or edit a task, when the backend saves the task, then it asynchronously calls the Gemini API with a structured prompt for label generation.
2.  Given the Gemini API returns valid labels, when the backend processes the response, then it populates the `labels` and `task_labels` tables in the database. (Covers FR8)
3.  Given the Gemini API call fails or returns invalid data, when the backend handles the error, then the task is still created successfully without any labels, and the error is logged.
4.  Given a task has labels, when the frontend displays the task, then the labels are shown as distinct visual elements (e.g., tags or badges).

## Tasks / Subtasks

- [ ] **Task 1: Backend - Database Schema** (AC 2)
  - [ ] Create a `labels` table for unique label names.
  - [ ] Create a `task_labels` join table for the many-to-many relationship between tasks and labels.
  - [ ] Create and run Supabase migration script.
- [ ] **Task 2: Backend - AI Integration Service** (AC 1, 2, 3)
  - [ ] Create a service to communicate with the Gemini API.
  - [ ] Implement a function that takes task details and returns a list of suggested labels.
  - [ ] Implement robust error handling and fallbacks for the Gemini API call.
- [ ] **Task 3: Backend - Task Creation/Update Workflow** (AC 1, 2)
  - [ ] Modify the existing task creation/update logic to asynchronously call the new AI integration service.
  - [ ] On successful label generation, save the labels to the `labels` and `task_labels` tables.
- [ ] **Task 4: Frontend - Display Labels** (AC 4)
  - [ ] Modify the `Task` component to display a list of labels.
  - [ ] Style the labels as tags or badges.
- [ ] **Task 5: Testing**
  - [ ] Write unit tests for the AI integration service.
  - [ ] Write integration tests to verify that labels are correctly generated and saved when a task is created.
  - [ ] Write frontend tests to verify that labels are displayed correctly.

## Dev Notes

- **Relevant architecture patterns and constraints**: All calls to the Gemini 2.5 Pro API **MUST** be made from the FastAPI backend to protect the API key, as specified in the architecture (section 4.3). The database schema will use a `labels` table for unique label names and a `task_labels` join table.
- **Source tree components to touch**:
    - **Backend (`api/`)**:
        - `app/models/`: Add `label.py` and `task_label.py`.
        - `app/services/`: Create `ai_service.py` for Gemini integration. Modify `task.py` to call the AI service.
        - `app/repositories/`: Create `label_repository.py`.
    - **Frontend (`nextjs-frontend/src/`)**:
        - `components/tasks/TaskCard.tsx`: Modify to display labels.
- **Testing standards summary**: Unit tests for backend services, integration tests for the full task creation flow with label generation, and frontend component tests.

### Project Structure Notes

- This story will add new models and services to the `api/` directory, following the established structure.

### References

- [Source: `docs/epics.md#Story-2.1:-AI-Generated-Smart-Labels`]
- [Source: `docs/architecture-2025-11-28.md#3.1.-Critical-Architectural-Decisions`] (AI Integration)

## Dev Agent Record

### Context Reference

- docs/sprint-artifacts/2-1-ai-generated-smart-labels.context.xml

### Agent Model Used

{{agent_model_name_version}}

### Debug Log References

### Completion Notes List

### File List
