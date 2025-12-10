# Story 3.3: Light/Dark Mode Themes

Status: drafted

## Story

As a user,
I want to switch between light and dark mode themes,
So that I can customize the application's appearance to my preference and reduce eye strain (Post-MVP).

## Acceptance Criteria

1.  **Theme Toggle Functionality:**
    1.1. When I activate the theme toggle, the application's visual theme switches between the "Refined Focus" Light and Dark modes. (Covers FR13)

2.  **Theme Persistence:**
    2.1. When the theme is switched, and I close and reopen the application, my chosen theme is remembered and applied automatically.

3.  **Component Adaptability:**
    3.1. When the theme is changed, all `shadcn/ui` components and `Tailwind CSS` styled elements adapt correctly to the selected theme.

## Tasks / Subtasks

- [ ] **Task 1: Implement Theme Toggling Logic (AC 1.1)**
  - [ ] Use Next.js context or a global state manager (e.g., Zustand) for theme management.
  - [ ] Create a theme toggle UI component.

- [ ] **Task 2: Persist Theme Preference (AC 2.1)**
  - [ ] Store the user's chosen theme preference in local storage.
  - [ ] Load the stored theme preference on application startup.

- [ ] **Task 3: Configure Styling for Light/Dark Modes (AC 3.1)**
  - [ ] Ensure "Refined Focus" theme styles in `Tailwind CSS` are configured for dark mode using `prefers-color-scheme` or theme classes.
  - [ ] Verify `shadcn/ui` components correctly respond to theme changes.

- [ ] **Task 4: Conduct UI Testing (AC 1.1, 2.1, 3.1)**
  - [ ] Manually test theme switching functionality and persistence across sessions.
  - [ ] Visually inspect all UI components in both light and dark modes for correct styling and adaptability.
  - [ ] Test on different browsers to ensure consistent theme application.

## Dev Notes

- **Architecture Patterns & Constraints:** This is primarily a frontend UI/UX story. It involves state management for theme preference and careful configuration of CSS frameworks.
- **Project Structure Notes:** This story impacts `nextjs-frontend/src/app/layout.tsx` (for theme provider), `nextjs-frontend/src/components/ThemeToggle.tsx` (for the toggle component), and styling configuration files (`tailwind.config.js`, `globals.css`).
- **Source Tree Components to Touch:**
    - `nextjs-frontend/src/app/layout.tsx`: Root layout for theme provider.
    - `nextjs-frontend/src/components/ThemeToggle.tsx`: New component for switching themes.
    - `nextjs-frontend/tailwind.config.js` and `nextjs-frontend/src/app/globals.css`: Theme-related styling.
- **Testing Standards Summary:** Manual testing for theme switching and persistence. Visual inspection of all UI components in both light and dark modes.

### Learnings from Previous Story

- From Story 3.2: "Today" View and Filtering, the importance of explicit citations for `architecture.md`, and `test-design-system-2025-11-28.md` was highlighted. Also, the need for explicit testing subtasks and a populated "Dev Agent Record" was identified.

### References

- [Source: `docs/epics.md` - Epic 3, Story 3.3]
- [Source: `docs/architecture-2025-11-28.md`]
- [Source: `docs/test-design-system-2025-11-28.md`]
- [Covers FR13]

## Dev Agent Record

### Context Reference

- docs/sprint-artifacts/3-3-light-dark-mode-themes.context.xml

### Agent Model Used

{{agent_model_name_version}}

### Debug Log References

### Completion Notes List

### File List

## Change Log

- **YYYY-MM-DD:** Initial draft created by {{agent_model_name_version}}.
