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

## Dev Notes

- **Architecture Patterns & Constraints:** This is a complex story involving a background service, AI logic, and a notification system. The choice of notification system (e.g., push notifications vs. email) is a key decision.
- **Source Tree Components to Touch:**
    - `api/app/services/nudge_service.py`: New service for AI-powered nudge logic.
    - `api/app/background_jobs.py`: Background job for checking and sending nudges.
    - `nextjs-frontend/src/app/sw.js`: Service worker for push notifications (if applicable).
    - `nextjs-frontend/src/utils/notification_handler.ts`: Logic for handling notification interactions.
- **Testing Standards Summary:** Unit tests for the AI nudge logic. Integration tests for the background job and notification delivery. E2E tests for the full user experience of receiving and interacting with a nudge.

### References

- [Source: `docs/epics.md` - Story 4.5]
- [Covers FR19]

## Change Log
