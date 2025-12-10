# Story 4.4: Integrated Visual Timers

Status: drafted

## Story

As a user,
I want to initiate integrated visual timers for my tasks,
So that I can maintain focus and manage my work sessions effectively (Post-MVP).

## Acceptance Criteria

1.  **Timer Activation:**
    1.1. When in the "Focused Task View" for a specific task, I can activate a Pomodoro timer (e.g., 25 minutes), which displays a subtle, visual countdown. (Covers FR18)

2.  **Timer Completion Notification:**
    2.1. When the timer session ends, a gentle, non-intrusive notification prompts me to take a break or extend the session.

## Tasks / Subtasks

- [ ] **Task 1: Implement Client-Side Timer Component (AC 1.1)**
  - [ ] Create a client-side timer component in the frontend.
  - [ ] Integrate this timer component seamlessly into the "Focused Task View".
  - [ ] Ensure the timer provides clear visual feedback without being distracting.

- [ ] **Task 2: Develop Timer Completion Notifications (AC 2.1)**
  - [ ] Implement a notification system for when the timer completes.
  - [ ] Notifications should adhere to the "Notifications & Nudges" patterns from the UX Design Specification (subtle and dismissible).

- [ ] **Task 3: Conduct Testing (AC 1.1, 2.1)**
  - [ ] Write unit tests for the client-side timer component logic (start, stop, reset, pause).
  - [ ] Manually test the user experience for starting a timer, observing the countdown, and receiving notifications upon completion.
  - [ ] Verify notification appearance and behavior (subtlety, dismissibility) according to UX specifications.

## Dev Notes

- **Architecture Patterns & Constraints:** This is a frontend-focused story. The timer will be managed client-side.
- **Project Structure Notes:** This story impacts `nextjs-frontend/src/components/VisualTimer.tsx` (new component), `nextjs-frontend/src/app/[taskId]/page.tsx` (integration into focused view), and `nextjs-frontend/src/components/Notification.tsx` (for timer completion notifications).
- **Source Tree Components to Touch:**
    - `nextjs-frontend/src/components/VisualTimer.tsx`: New component for the timer.
    - `nextjs-frontend/src/app/[taskId]/page.tsx`: The "Focused Task View" to integrate the timer into.
    - `nextjs-frontend/src/components/Notification.tsx`: Component for displaying notifications.
- **Testing Standards Summary:** Unit tests for the timer component logic (start, stop, reset). Manual testing of the user experience for starting a timer and receiving notifications.

### Learnings from Previous Story

- From Story 4.3: "Just Start Here" Button, the importance of explicit citations for `architecture.md`, and `test-design-system-2025-11-28.md` was highlighted. Also, the need for explicit testing subtasks and a populated "Dev Agent Record" was identified.

### References

- [Source: `docs/epics.md` - Epic 4, Story 4.4]
- [Source: `docs/architecture-2025-11-28.md`]
- [Source: `docs/test-design-system-2025-11-28.md`]
- [Covers FR18]

## Dev Agent Record

### Context Reference

- docs/sprint-artifacts/4-4-integrated-visual-timers.context.xml

### Agent Model Used

{{agent_model_name_version}}

### Debug Log References

### Completion Notes List

### File List

## Change Log

- **YYYY-MM-DD:** Initial draft created by {{agent_model_name_version}}.
