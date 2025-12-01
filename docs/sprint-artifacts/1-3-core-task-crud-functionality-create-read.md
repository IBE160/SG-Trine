# Story 1.3: core-task-crud-functionality-create-read

Status: done

## Story

As a user,
I want to create new tasks and view my existing tasks,
so that I can start organizing my responsibilities.

## Acceptance Criteria

1.  Given I am on the "Proactive Dashboard" or any main view, When I use the "Quick Add" (+) button to enter a task title and submit, Then a `POST` request is sent to the `/api/v1/tasks` endpoint and the new task appears in my list. (Covers FR1)
2.  Given I navigate to a view that displays tasks, When the component mounts, Then a `GET` request is made to `/api/v1/tasks` to fetch and display all my tasks. (Covers FR2)
3.  Given the UI is displayed, When I view the task list and input fields, Then the interface adheres to the "Hyper-Minimalism" principle from the UX design. (Covers FR11 part)

## Tasks / Subtasks

- [ ] Backend: Create `POST /api/v1/tasks` endpoint in FastAPI. (AC: #1)
  - [ ] The endpoint should receive the task details from the request body.
  - [ ] It should save the new task to the database using the `supabase-py` library.
- [ ] Backend: Create `GET /api/v1/tasks` endpoint in FastAPI. (AC: #2)
  - [ ] The endpoint should retrieve all tasks for the authenticated user from the database.
- [ ] Frontend: Implement `TaskInput` and `TaskList` components using `shadcn/ui`. (AC: #1, #2, #3)
  - [ ] The components should follow the "Hyper-Minimalism" principle.
- [ ] Frontend: Implement the "Quick Add" (+) floating action button. (AC: #1)
  - [ ] Clicking the button should trigger the display of the `TaskInput` component.
- [ ] Frontend: Implement state management for the task list. (AC: #1, #2)
  - [ ] Use `Zustand` for global state or `React Query`/`SWR` for data fetching and caching.

## Dev Notes

- **API Naming**: Endpoints should be `kebab-case` and plural (e.g., `/api/v1/tasks`). JSON properties must be `snake_case`. [Source: docs/architecture-2025-11-28.md#Implementation-Patterns-Consistency-Rules]
- **Component Naming**: React components and their files should be `PascalCase` (e.g., `TaskCard.tsx`). [Source: docs/architecture-2025-11-28.md#Implementation-Patterns-Consistency-Rules]
- **Variable Naming**: Use `camelCase` for TypeScript/JS variables and `snake_case` for Python variables. [Source: docs/architecture-2025-11-28.md#Implementation-Patterns-Consistency-Rules]
- **State Management**: Use `Zustand` for managing global state. [Source: docs/architecture-2025-11-28.md#Implementation-Patterns-Consistency-Rules]
- **Styling**: All styling will be done using `Tailwind CSS` utility classes. `shadcn/ui` components will be the default. [Source: docs/architecture-2025-11-28.md#Implementation-Patterns-Consistency-Rules]
- **Project Structure**: The `TaskInput` and `TaskList` components should be placed in `src/components/tasks/`. [Source: docs/architecture-2025-11-28.md#Project-Structure]

### Project Structure Notes

- No conflicts detected. The components for this story fit well within the defined project structure.

### References

- [docs/epics.md#Story-1.3](docs/epics.md#Story-1.3)
- [docs/architecture-2025-11-28.md](docs/architecture-2025-11-28.md)
- [docs/ux-design-specification.md](docs/ux-design-specification.md)

## Dev Agent Record

### Context Reference

<!-- Path(s) to story context XML will be added here by context workflow -->

### Agent Model Used

{{agent_model_name_version}}

### Debug Log References

### Completion Notes List

### File List
