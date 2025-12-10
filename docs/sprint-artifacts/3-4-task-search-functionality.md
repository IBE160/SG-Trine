# Story 3.4: Task Search Functionality

Status: drafted

## Story

As a user,
I want to search for tasks by keywords,
So that I can quickly find specific tasks within my list (Post-MVP).

## Acceptance Criteria

1.  **Frontend Search Request:**
    1.1. When I enter text into the search bar, the frontend sends a `GET` request to `/api/v1/tasks/search?q={query}`.

2.  **Backend Search Response:**
    2.1. Given the backend responds with tasks matching the search query using PostgreSQL FTS, the UI dynamically updates, displaying only relevant tasks. (Covers FR14)

3.  **Clear Search Functionality:**
    3.1. When a search query has been executed, and I clear the search bar, the full task list is restored by calling `/api/v1/tasks`.

## Tasks / Subtasks

- [ ] **Task 1: Implement Frontend Search Bar and Request Logic (AC 1.1, 3.1)**
  - [ ] Create a search input component in the frontend.
  - [ ] Implement debouncing for user input to avoid excessive API calls.
  - [ ] Send `GET` request to `/api/v1/tasks/search?q={query}` with the search term.
  - [ ] Implement logic to clear search results and restore full task list when search bar is cleared.

- [ ] **Task 2: Develop Backend Search Endpoint with PostgreSQL FTS (AC 2.1)**
  - [ ] Create `GET /api/v1/tasks/search` endpoint in FastAPI.
  - [ ] Leverage PostgreSQL's Full-Text Search (FTS) capabilities to search task titles/descriptions.
  - [ ] Ensure the `tasks` table has a `tsvector` column and a trigger to update it, as described in architecture.

- [ ] **Task 3: Display Search Results (AC 2.1)**
  - [ ] Update the frontend task list component to display the filtered search results dynamically.

- [ ] **Task 4: Conduct Testing (AC 1.1, 2.1, 3.1)**
  - [ ] Write unit tests for the backend search logic, including edge cases and various query types.
  - [ ] Write integration tests to verify frontend search bar functionality and dynamic display of results.
  - [ ] Conduct performance testing for search functionality with large datasets.
  - [ ] Manually test search functionality across different browsers and devices.

## Dev Notes

- **Architecture Patterns & Constraints:** This story requires both frontend UI and backend database integration for Full-Text Search. Performance of FTS needs to be considered.
- **Project Structure Notes:** This story impacts `nextjs-frontend/src/components/SearchBar.tsx` (new component), relevant task list component in `nextjs-frontend/src/app/page.tsx`, `api/app/main.py` (new search endpoint), and database migration for the `tasks` table.
- **Source Tree Components to Touch:**
    - `nextjs-frontend/src/components/SearchBar.tsx`: New search bar component.
    - `nextjs-frontend/src/app/page.tsx` or relevant task list component: Integration of search results.
    - `api/app/main.py`: New search endpoint.
    - Database migration for `tasks` table to add FTS capabilities.
- **Testing Standards Summary:** Unit tests for backend search logic. Integration tests for frontend search bar functionality and dynamic display of results. Performance testing for large datasets.

### Learnings from Previous Story

- From Story 3.3: Light/Dark Mode Themes, the importance of explicit citations for `architecture.md`, and `test-design-system-2025-11-28.md` was highlighted. Also, the need for explicit testing subtasks and a populated "Dev Agent Record" was identified.

### References

- [Source: `docs/epics.md` - Epic 3, Story 3.4]
- [Source: `docs/architecture-2025-11-28.md`]
- [Source: `docs/test-design-system-2025-11-28.md`]
- [Covers FR14]

## Dev Agent Record

### Context Reference

- docs/sprint-artifacts/3-4-task-search-functionality.context.xml

### Agent Model Used

{{agent_model_name_version}}

### Debug Log References

### Completion Notes List

### File List

## Change Log

- **YYYY-MM-DD:** Initial draft created by {{agent_model_name_version}}.
