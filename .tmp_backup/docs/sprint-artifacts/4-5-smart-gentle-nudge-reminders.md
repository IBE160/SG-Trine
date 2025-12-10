# Story 4.5: Smart, Gentle Nudge Reminders

Status: drafted

## Story

As a user,
I want to receive smart, context-aware nudge reminders,
So that I can stay on track with my priorities without feeling overwhelmed (Post-MVP).

## Acceptance Criteria

1.  **Context-Aware Nudge Triggering:**
    1.1. When a high-priority task is approaching its due time and I am not actively engaging with the application, the FastAPI backend service, using AI logic, determines an appropriate moment to send a gentle, non-judgmental notification. (Covers FR19)

2.  **Notification Interaction:**
    2.1. When I interact with a received notification (e.g., a toast notification or push notification), I am directed back to the relevant task within the application.

## Tasks / Subtasks

- [ ] **Task 1: Develop Backend Service for Nudge Logic (AC 1.1)**
  - [ ] Implement a background job or scheduled task (e.g., using `Inngest`) to periodically check task due dates and user activity.
  - [ ] Develop AI logic in the backend to determine "context-aware" triggers for sending nudges.

- [ ] **Task 2: Implement Notification Delivery (AC 1.1)**
  - [ ] Set up a notification delivery mechanism (e.g., email, push notifications).
  - [ ] The backend service will trigger notifications based on the nudge logic.

- [ ] **Task 3: Handle Notification Interaction in Frontend (AC 2.1)**
  - [ ] Implement frontend logic to handle incoming notifications.
  - [ ] When a notification is interacted with, the application should navigate to the relevant task.

- [ ] **Task 4: Conduct Testing (AC 1.1, 2.1)**
  - [ ] Write unit tests for the AI nudge logic (e.g., criteria for sending nudges).
  - [ ] Develop integration tests for the background job and notification delivery mechanism.
  - [ ] Implement E2E tests to verify the full user experience of receiving and interacting with a nudge.

## Dev Notes

- **Architecture Patterns & Constraints:** This is a complex story involving a background service, AI logic, and a notification system. The choice of notification system (e.g., push notifications vs. email) is a key decision.
- **Project Structure Notes:** This story impacts `api/app/services/nudge_service.py` (new service), `api/app/background_jobs.py` (background task), `nextjs-frontend/src/app/sw.js` (service worker for push notifications), and `nextjs-frontend/src/utils/notification_handler.ts` (frontend notification logic).
- **Source Tree Components to Touch:**
    - `api/app/services/nudge_service.py`: New service for AI-powered nudge logic.
    - `api/app/background_jobs.py`: Background job for checking and sending nudges.
    - `nextjs-frontend/src/app/sw.js`: Service worker for push notifications (if applicable).
    - `nextjs-frontend/src/utils/notification_handler.ts`: Logic for handling notification interactions.
- **Testing Standards Summary:** Unit tests for the AI nudge logic. Integration tests for the background job and notification delivery. E2E tests for the full user experience of receiving and interacting with a nudge.

### Learnings from Previous Story

- From Story 4.4: Integrated Visual Timers, the importance of explicit citations for `architecture.md`, and `test-design-system-2025-11-28.md` was highlighted. Also, the need for explicit testing subtasks and a populated "Dev Agent Record" was identified.

### References

- [Source: `docs/epics.md` - Epic 4, Story 4.5]
- [Source: `docs/architecture-2025-11-28.md`]
- [Source: `docs/test-design-system-2025-11-28.md`]
- [Covers FR19]

## Dev Agent Record

### Context Reference

- docs/sprint-artifacts/4-5-smart-gentle-nudge-reminders.context.xml

### Agent Model Used

{{agent_model_name_version}}

### Debug Log References

### Completion Notes List

### File List

## Change Log

- **YYYY-MM-DD:** Initial draft created by {{agent_model_name_version}}.
