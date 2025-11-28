# ibe160 - Epic Breakdown

**Author:** BIP
**Date:** 2025-11-26
**Project Level:** {{project_level}}
**Target Scale:** {{target_scale}}

---

## Overview

This document provides the complete epic and story breakdown for ibe160, decomposing the requirements from the [PRD](./PRD.md) into implementable stories.

**Living Document Notice:** This is the initial version. It will be updated after UX Design and Architecture workflows add interaction and technical details to stories.

---

## Workflow Status (2025-11-28)

**Mode:** UPDATE
**Context Analysis:**
✅ UX Design found - I will add interaction details to your stories.
✅ Architecture found - I will add technical implementation notes to your stories.

---

## Epics Summary

This project will be organized into the following epics, designed to deliver incremental user value and build upon a solid foundation.

-   **Epic 1: Foundation & Core Task Management**
    -   Goal: Establish the basic application infrastructure and enable users to perform essential task management (CRUD, reorder, mark complete).
    -   Covers FRs: FR1, FR2, FR3, FR4, FR5, FR6, FR7, FR21, FR22, FR23, FR24

-   **Epic 2: AI-Powered Task Intelligence**
    -   Goal: Integrate AI to provide smart categorization and prioritization, enhancing task clarity and reducing overwhelm.
    -   Covers FRs: FR8, FR9, FR10

-   **Epic 3: Advanced Task Management & User Experience**
    -   Goal: Implement key UI/UX features and advanced task capabilities to enrich the user experience (Post-MVP).
    -   Covers FRs: FR11, FR12, FR13, FR14

-   **Epic 4: AI-Enhanced Productivity Tools (ADHD Focus - Post-MVP)**
    -   Goal: Deliver specialized AI-driven tools to directly address ADHD-related productivity challenges, providing targeted support.
    -   Covers FRs: FR15, FR16, FR17, FR18, FR19, FR20

---

## Functional Requirements Inventory

- FR1: Users can create new tasks.
- FR2: Users can view their list of tasks.
- FR3: Users can edit existing tasks.
- FR4: Users can delete tasks.
- FR5: Users can mark tasks as complete.
- FR6: Users can reorder tasks in their list.
- FR7: The application stores task data securely in a backend (Supabase).
- FR8: The system automatically generates smart labels (e.g., "work," "personal," "urgent") for tasks using AI.
- FR9: The system automatically suggests priority levels for tasks using AI.
- FR10: Users can filter their tasks based on AI-generated smart labels.
- FR11: The application provides a clean, minimal, and intuitive user interface.
- FR12: The application displays a "Today" view as the default screen (Post-MVP).
- FR13: Users can switch between Light and Dark mode themes (Post-MVP).
- FR14: Users can search for tasks within the application (Post-MVP).
- FR15: The system provides AI suggestions for breaking down large tasks into smaller sub-steps.
- FR16: The system provides AI-generated time estimates for tasks (e.g., "Approx. 15 mins").
- FR17: The application provides a "Just Start Here" button to initiate the single most important task.
- FR18: The application integrates visual timers (e.g., Pomodoro) for focused work.
- FR19: The application provides smart, context-aware nudge reminders.
- FR20: Users can schedule tasks for specific days.
- FR21: The application functions as a Single Page Application (SPA).
- FR22: The application is compatible with modern, evergreen web browsers.
- FR23: The application provides real-time updates for task changes.
- FR24: The application incorporates basic accessibility principles to ensure usability.

---

## FR Coverage Map

- FR1: Users can create new tasks. → Epic 1
- FR2: Users can view their list of tasks. → Epic 1
- FR3: Users can edit existing tasks. → Epic 1
- FR4: Users can delete tasks. → Epic 1
- FR5: Users can mark tasks as complete. → Epic 1
- FR6: Users can reorder tasks in their list. → Epic 1
- FR7: The application stores task data securely in a backend (Supabase). → Epic 1
- FR8: The system automatically generates smart labels (e.g., "work," "personal," "urgent") for tasks using AI. → Epic 2
- FR9: The system automatically suggests priority levels for tasks using AI. → Epic 2
- FR10: Users can filter their tasks based on AI-generated smart labels. → Epic 2
- FR11: The application provides a clean, minimal, and intuitive user interface. → Epic 3
- FR12: The application displays a "Today" view as the default screen (Post-MVP). → Epic 3
- FR13: Users can switch between Light and Dark mode themes (Post-MVP). → Epic 3
- FR14: Users can search for tasks within the application (Post-MVP). → Epic 3
- FR15: The system provides AI suggestions for breaking down large tasks into smaller sub-steps. → Epic 4
- FR16: The system provides AI-generated time estimates for tasks (e.g., "Approx. 15 mins"). → Epic 4
- FR17: The application provides a "Just Start Here" button to initiate the single most important task. → Epic 4
- FR18: The application integrates visual timers (e.g., Pomodoro) for focused work. → Epic 4
- FR19: The application provides smart, context-aware nudge reminders. → Epic 4
- FR20: Users can schedule tasks for specific days. → Epic 4
- FR21: The application functions as a Single Page Application (SPA). → Epic 1
- FR22: The application is compatible with modern, evergreen web browsers. → Epic 1
- FR23: The application provides real-time updates for task changes. → Epic 1
- FR24: The application incorporates basic accessibility principles to ensure usability. → Epic 1

---

<!-- Repeat for each epic (N = 1, 2, 3...) -->

## Epic 1: Foundation & Core Task Management
Goal: Establish the basic application infrastructure and enable users to perform essential task management (CRUD, reorder, mark complete).

### Story 1.1: Project Setup and Initial Deployment

As a developer,
I want to set up the project infrastructure (Next.js, FastAPI, Supabase, Vercel),
So that I can begin developing and deploying the application efficiently.

**Acceptance Criteria:**

**Given** a new project,
**When** the setup script is executed,
**Then** the Next.js frontend, FastAPI backend, and Supabase integration are configured.

**And** Given a code push to the main branch,
**When** the CI/CD pipeline runs on Vercel,
**Then** the application is deployed successfully to a staging environment.

**And** Given the project structure,
**When** core dependencies are installed,
**Then** the project is ready for local development.

**Prerequisites:** None

**Technical Notes:** Includes repository setup, build system configuration, Vercel deployment pipeline basics, and core dependency installation. Focus on getting a minimal 'hello world' style application deployed end-to-end.

### Story 1.2: Secure User Task Data Storage

As a user,
I want my task data to be securely stored and managed in a backend,
So that my information is persistent and protected.

**Acceptance Criteria:**

**Given** a user creates a task,
**When** the task is saved,
**Then** it is securely persisted in the Supabase database.

**And** Given a user retrieves their tasks,
**When** the tasks are loaded,
**Then** they are securely fetched from Supabase.

**And** Given Supabase is configured,
**When** user authentication is managed,
**Then** basic user authentication functions correctly.

**Prerequisites:** Story 1.1

**Technical Notes:** Implement Supabase integration for task data persistence (PostgreSQL) and user authentication. Focus on secure data handling. Covers FR7.

### Story 1.3: Core Task CRUD Functionality (Create, Read)

As a user,
I want to create new tasks and view my existing tasks,
So that I can start organizing my responsibilities.

**Acceptance Criteria:**

**Given** I am logged in,
**When** I navigate to the task list,
**Then** I see an input field to add a new task.

**And** Given I enter text in the input field and submit,
**Then** a new task appears in my list. (Covers FR1)

**And** Given I have existing tasks,
**When** I view my task list,
**Then** all my tasks are displayed in an organized manner. (Covers FR2)

**And** Given the application is running in a modern browser,
**When** I access the task list,
**Then** the UI is clean and minimal. (Covers FR11 part)

**Prerequisites:** Story 1.2

**Technical Notes:** Implement frontend components for task input and display. Connect to backend API for creating and reading tasks. Ensure SPA architecture responsiveness and basic browser compatibility. Covers FR1, FR2, FR11, FR21, FR22.

### Story 1.4: Core Task CRUD Functionality (Update, Delete)

As a user,
I want to edit and delete my existing tasks,
So that I can maintain an accurate and clutter-free task list.

**Acceptance Criteria:**

**Given** I have a task,
**When** I activate the edit function,
**Then** I can modify its description. (Covers FR3)

**And** Given I have modified a task,
**When** I save the changes,
**Then** the task updates in my list and in the backend.

**And** Given I have a task,
**When** I activate the delete function and confirm,
**Then** the task is removed from my list and the backend. (Covers FR4)

**And** Given task changes are made,
**When** I view my list across devices,
**Then** changes reflect immediately due to real-time updates. (Covers FR23)

**Prerequisites:** Story 1.3

**Technical Notes:** Implement frontend UI for editing and deleting tasks. Connect to backend API. Leverage Supabase real-time capabilities. Covers FR3, FR4, FR23.

### Story 1.5: Task Completion and Reordering

As a user,
I want to mark tasks as complete and reorder them,
So that I can manage my progress and prioritize visually.

**Acceptance Criteria:**

**Given** I have a task,
**When** I mark it as complete,
**Then** its visual status changes to indicate completion. (Covers FR5)

**And** Given I have completed a task,
**When** I unmark it,
**Then** its status reverts.

**And** Given I have multiple tasks,
**When** I drag and drop a task,
**Then** its position in the list updates visually and in the backend. (Covers FR6)

**And** Given the application aims for broad usability,
**When** I interact with task elements,
**Then** basic accessibility principles are applied. (Covers FR24)

**Prerequisites:** Story 1.4

**Technical Notes:** Implement UI/UX for task completion toggling and drag-and-drop reordering. Update backend models accordingly. Covers FR5, FR6, FR24.

---

<!-- End epic repeat -->

---

## FR Coverage Matrix

- FR1: Users can create new tasks. → Epic 1, Story 1.3
- FR2: Users can view their list of tasks. → Epic 1, Story 1.3
- FR3: Users can edit existing tasks. → Epic 1, Story 1.4
- FR4: Users can delete tasks. → Epic 1, Story 1.4
- FR5: Users can mark tasks as complete. → Epic 1, Story 1.5
- FR6: Users can reorder tasks in their list. → Epic 1, Story 1.5
- FR7: The application stores task data securely in a backend (Supabase). → Epic 1, Story 1.2
- FR8: The system automatically generates smart labels (e.g., "work," "personal," "urgent") for tasks using AI. → Epic 2, Story 2.1
- FR9: The system automatically suggests priority levels for tasks using AI. → Epic 2, Story 2.2
- FR10: Users can filter their tasks based on AI-generated smart labels. → Epic 2, Story 2.3
- FR11: The application provides a clean, minimal, and intuitive user interface. → Epic 3, Story 3.1
- FR12: The application displays a "Today" view as the default screen (Post-MVP). → Epic 3, Story 3.2
- FR13: Users can switch between Light and Dark mode themes (Post-MVP). → Epic 3, Story 3.3
- FR14: Users can search for tasks within the application (Post-MVP). → Epic 3, Story 3.4
- FR15: The system provides AI suggestions for breaking down large tasks into smaller sub-steps. → Epic 4, Story 4.1
- FR16: The system provides AI-generated time estimates for tasks (e.g., "Approx. 15 mins"). → Epic 4, Story 4.2
- FR17: The application provides a "Just Start Here" button to initiate the single most important task. → Epic 4, Story 4.3
- FR18: The application integrates visual timers (e.g., Pomodoro) for focused work. → Epic 4, Story 4.4
- FR19: The application provides smart, context-aware nudge reminders. → Epic 4, Story 4.5
- FR20: Users can schedule tasks for specific days. → Epic 4, Story 4.6
- FR21: The application functions as a Single Page Application (SPA). → Epic 1, Story 1.3
- FR22: The application is compatible with modern, evergreen web browsers. → Epic 1, Story 1.3
- FR23: The application provides real-time updates for task changes. → Epic 1, Story 1.4
- FR24: The application incorporates basic accessibility principles to ensure usability. → Epic 1, Story 1.5

---

## Summary

This epic breakdown meticulously translates the strategic requirements from the Product Requirements Document (PRD) into a structured, actionable plan for development. Organized into four distinct epics, it ensures that each delivers incremental user value, starting with foundational task management and progressing to AI-powered features, advanced UI/UX, and specialized ADHD-focused productivity tools. Each functional requirement from the PRD is traceable to specific user stories, complete with detailed acceptance criteria, prerequisites, and technical notes, preparing the project for efficient implementation. This document serves as a living guide, ready to be enhanced with further details from UX Design and Architecture workflows.

---

_For implementation: Use the `create-story` workflow to generate individual story implementation plans from this epic breakdown._

_This document will be updated after UX Design and Architecture workflows to incorporate interaction details and technical decisions._

---

## Epic 2: AI-Powered Task Intelligence
Goal: Integrate AI to provide smart categorization and prioritization, enhancing task clarity.

### Story 2.1: AI-Generated Smart Labels

As a user,
I want the system to automatically generate smart labels for my tasks,
So that I can quickly categorize and understand my tasks at a glance.

**Acceptance Criteria:**

**Given** I create or edit a task,
**When** the task is saved,
**Then** the system sends the task description to the AI service.

**And** Given the AI service processes the task,
**When** it returns relevant keywords,
**Then** these keywords are saved as smart labels (e.g., "work," "personal," "urgent") for the task. (Covers FR8)

**And** Given a task has smart labels,
**When** I view the task,
**Then** the labels are prominently displayed.

**Prerequisites:** Story 1.3 (Task Create/Read), Backend AI service implemented.

**Technical Notes:** Implement AI service endpoint (FastAPI) that calls Gemini 2.5 Pro for label generation. Integrate frontend to display labels.

### Story 2.2: AI-Suggested Priority Levels

As a user,
I want the system to automatically suggest a priority level for my tasks,
So that I can focus on what's most important and reduce decision fatigue.

**Acceptance Criteria:**

**Given** I create or edit a task,
**When** the task is saved,
**Then** the system sends the task description to the AI service.

**And** Given the AI service processes the task,
**When** it returns a suggested priority level (e.g., 1-4 or high/medium/low),
**Then** this priority is saved for the task. (Covers FR9)

**And** Given a task has a suggested priority,
**When** I view the task,
**Then** the priority is clearly indicated.

**Prerequisites:** Story 2.1

**Technical Notes:** Enhance AI service endpoint to include priority suggestion. Integrate frontend to display priority.

### Story 2.3: Filter Tasks by Smart Labels

As a user,
I want to filter my tasks by their smart labels,
So that I can quickly find and focus on specific categories of tasks.

**Acceptance Criteria:**

**Given** I have tasks with smart labels,
**When** I select a specific label (e.g., "work"),
**Then** only tasks associated with that label are displayed. (Covers FR10)

**And** Given I have selected a filter,
**When** I clear the filter,
**Then** all tasks are displayed again.

**And** Given the filtering mechanism is present,
**When** I interact with it,
**Then** it is intuitive and responsive.

**Prerequisites:** Story 2.1

**Technical Notes:** Implement frontend filtering logic based on task smart labels.

---

## Epic 3: Advanced Task Management & User Experience
Goal: Implement key UI/UX features and advanced task capabilities to enrich the user experience (Post-MVP).

### Story 3.1: Minimalist User Interface

As a user,
I want to interact with a clean, minimal, and intuitive user interface,
So that I can focus on my tasks without distractions.

**Acceptance Criteria:**

**Given** the application is loaded,
**When** I view the UI,
**Then** it adheres to hyper-minimalism design principles. (Covers FR11)

**And** Given I am interacting with the UI,
**When** elements are clicked or hovered,
**Then** visual feedback is subtle and non-distracting.

**And** Given the UI is displayed,
**When** I resize the window,
**Then** it remains responsive and usable across various screen sizes.

**Prerequisites:** Story 1.3 (Core Task CRUD)

**Technical Notes:** Apply Shadcn UI and Tailwind CSS for minimalist aesthetic. Ensure responsive design implementation.

### Story 3.2: "Today" View and Filtering

As a user,
I want to see a dedicated "Today" view as the default screen,
So that I can immediately focus on my most urgent daily tasks (Post-MVP).

**Acceptance Criteria:**

**Given** I open the application,
**When** it loads,
**Then** the "Today" view is presented by default, showing a curated list of tasks. (Covers FR12)

**And** Given the "Today" view is active,
**When** I interact with tasks,
**Then** all core task management functionalities (CRUD, complete, reorder) are available.

**And** Given the "Today" view is active,
**When** tasks are assigned to "Today" (manually or via AI),
**Then** they appear in this view.

**Prerequisites:** Story 1.3 (Core Task CRUD)

**Technical Notes:** Implement a new frontend view component for "Today." Integrate with existing task data and filtering mechanisms.

### Story 3.3: Light/Dark Mode Themes

As a user,
I want to switch between light and dark mode themes,
So that I can customize the application's appearance to my preference and reduce eye strain (Post-MVP).

**Acceptance Criteria:**

**Given** I am in the application,
**When** I activate the theme toggle,
**Then** the application's visual theme switches between light and dark modes. (Covers FR13)

**And** Given the theme is switched,
**When** I close and reopen the application,
**Then** my chosen theme is remembered and applied.

**And** Given the theme is changed,
**When** I view the UI,
**Then** all UI components adapt correctly to the selected theme.

**Prerequisites:** Story 3.1

**Technical Notes:** Implement theme toggling logic using Tailwind CSS and Next.js. Persist theme preference (e.g., via local storage or user settings).

### Story 3.4: Task Search Functionality

As a user,
I want to search for tasks by keywords,
So that I can quickly find specific tasks within my list (Post-MVP).

**Acceptance Criteria:**

**Given** I am viewing my tasks,
**When** I enter text into the search bar,
**Then** the task list dynamically filters to show only tasks matching the search query. (Covers FR14)

**And** Given I have a long list of tasks,
**When** I search for a keyword,
**Then** relevant tasks appear within a reasonable time frame.

**And** Given the search functionality is active,
**When** I clear the search bar,
**Then** the full task list is restored.

**Prerequisites:** Story 1.3 (Core Task CRUD)

**Technical Notes:** Implement frontend search component and client-side (or server-side for larger datasets) filtering logic.

---

## Epic 4: AI-Enhanced Productivity Tools (ADHD Focus - Post-MVP)
Goal: Deliver specialized AI-driven tools to directly address ADHD-related productivity challenges, providing targeted support.

### Story 4.1: AI Task Breakdown Suggestions

As a user,
I want the system to suggest breaking down large tasks into smaller sub-steps,
So that I can reduce overwhelm and make daunting tasks manageable (Post-MVP).

**Acceptance Criteria:**

**Given** I input a task identified as complex by the AI,
**When** I request a breakdown,
**Then** the system uses AI to generate a list of smaller, actionable sub-steps. (Covers FR15)

**And** Given sub-steps are generated,
**When** I accept them,
**Then** they are added as new sub-tasks linked to the main task.

**Prerequisites:** Story 2.1 (AI-Generated Smart Labels)

**Technical Notes:** Extend AI service to include task decomposition logic. Implement UI for displaying and accepting sub-step suggestions.

### Story 4.2: AI-Generated Time Estimates

As a user,
I want the system to provide AI-generated time estimates for my tasks,
So that I can better plan my day and manage my time blindness (Post-MVP).

**Acceptance Criteria:**

**Given** I create or edit a task,
**When** the task is saved,
**Then** the AI service provides an approximate time estimate (e.g., "Approx. 15 mins," "Approx. 1 hour"). (Covers FR16)

**And** Given a task has a time estimate,
**When** I view the task,
**Then** the estimate is clearly displayed.

**Prerequisites:** Story 2.1 (AI-Generated Smart Labels)

**Technical Notes:** Further enhance AI service to include time estimation logic. Integrate frontend to display estimates.

### Story 4.3: "Just Start Here" Button

As a user,
I want to click a "Just Start Here" button to be directed to the single most important task,
So that I can overcome decision paralysis and initiate work immediately (Post-MVP).

**Acceptance Criteria:**

**Given** I am on my task list,
**When** I click the "Just Start Here" button,
**Then** the system identifies and presents the highest priority, most actionable task. (Coverts FR17)

**And** Given a task is presented,
**When** I engage with it,
**Then** the application provides a focused view for that task.

**Prerequisites:** Story 2.2 (AI-Suggested Priority Levels), Story 3.2 ("Today" View)

**Technical Notes:** Implement AI logic to select the "best" task considering priority, estimated time, and context. Implement UI for the button and focused task view.

### Story 4.4: Integrated Visual Timers

As a user,
I want to initiate integrated visual timers for my tasks,
So that I can maintain focus and manage my work sessions effectively (Post-MVP).

**Acceptance Criteria:**

**Given** I am working on a task,
**When** I activate a timer,
**Then** a visual countdown (e.g., Pomodoro) starts. (Covers FR18)

**And** Given the timer is running,
**When** the session ends,
**Then** I am notified and prompted to take a break or continue.

**Prerequisites:** Story 4.2 (AI-Generated Time Estimates)

**Technical Notes:** Implement frontend timer components. Integrate with task context for time tracking.

### Story 4.5: Smart, Gentle Nudge Reminders

As a user,
I want to receive smart, context-aware nudge reminders,
So that I can stay on track with my priorities without feeling overwhelmed (Post-MVP).

**Acceptance Criteria:**

**Given** a high-priority task is approaching its due time,
**When** I am not actively engaging with the application,
**Then** the system sends a gentle, non-judgmental notification. (Covers FR19)

**And** Given a notification is received,
**When** I interact with it,
**Then** I am directed back to the relevant task.

**Prerequisites:** Story 2.2 (AI-Suggested Priority Levels)

**Technical Notes:** Implement backend service for sending contextual notifications. Define AI logic for determining appropriate nudge timing and content.

### Story 4.6: Scheduled Task Management

As a user,
I want to schedule tasks for specific days,
So that I can plan my workload and manage my commitments effectively (Post-MVP).

**Acceptance Criteria:**

**Given** I have a task,
**When** I edit it,
**Then** I can assign a specific due date or scheduled date. (Covers FR20)

**And** Given tasks are scheduled,
**When** the scheduled day arrives,
**Then** these tasks are prominently displayed in relevant views (e.g., "Today" view).

**Prerequisites:** Story 1.3 (Core Task CRUD)

**Technical Notes:** Extend task data model to include scheduled dates. Implement UI for date selection and filtering.