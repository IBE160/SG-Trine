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

**Given** a new project repository,
**When** the Next.js frontend is initialized using `npx create-next-app@latest`,
**And** a Python virtual environment is created in an `api/` directory with `FastAPI`, `uvicorn`, and `supabase-py` installed,
**Then** the monorepo structure is established locally.

**And** Given the project is pushed to a Git provider connected to Vercel,
**When** the Vercel deployment pipeline runs,
**Then** the Next.js frontend deploys successfully.
**And** the FastAPI app in the `api/` directory is successfully deployed as a serverless function.
**And** a "Hello World" endpoint on the FastAPI function is reachable.

**Prerequisites:** None

**Technical Notes (Enhanced):**
-   **Monorepo Structure:** The project will follow the structure defined in `architecture.md`, with a `nextjs-frontend` directory and a separate `api` directory for the FastAPI backend. For Vercel deployment, the `api` directory will be placed inside the Next.js project root.
-   **Frontend Setup:** Initialize using the command from the architecture doc: `npx create-next-app@latest nextjs-frontend --typescript --eslint --app --src-dir --import-alias "@/*"`.
-   **Backend Setup:** The FastAPI application will reside in the `/api` directory to leverage Vercel's serverless function deployment. It will have its own `requirements.txt` and virtual environment.
-   **Deployment:** Vercel project settings must include all necessary environment variables (Supabase URL/keys, Gemini API Key) as defined in the architecture.
-   **Verification:** The initial deployment should be a minimal 'hello world' style application to verify the end-to-end connection between the frontend and the deployed serverless backend function.

### Story 1.2: Secure User Task Data Storage

As a user,
I want my task data to be securely stored and managed in a backend,
So that my information is persistent and protected.

**Acceptance Criteria:**

**Given** a user is authenticated,
**When** a new task is created via a `POST /api/v1/tasks` request,
**Then** the task is saved to the `tasks` table in the Supabase database with the correct `user_id`.

**And** Given the `tasks` table has Row Level Security (RLS) enabled,
**When** a user requests their tasks,
**Then** they only receive tasks where `tasks.user_id` matches their authenticated user ID.

**And** Given a user is signed in on the frontend,
**When** their session JWT is sent to the backend,
**Then** the backend successfully validates the JWT to authorize the request.

**Prerequisites:** Story 1.1

**Technical Notes (Enhanced):**
-   **Database Schema:** Implements the `tasks` table as defined in the architecture document (section 4.1), with columns for `id`, `user_id`, `title`, `is_completed`, etc.
-   **Authentication:** The frontend uses `@supabase/supabase-js` to manage sessions. The backend FastAPI app includes a dependency that verifies the Bearer token (JWT) on protected routes.
-   **Security:** Row Level Security (RLS) policies MUST be enabled on the `tasks` table in Supabase to enforce data isolation between users at the database level.
-   **Data Flow:** The Next.js client sends the create/read request to the FastAPI backend, which then uses the `supabase-py` library to interact with the database.
-   Covers FR7.

### Story 1.3: Core Task CRUD Functionality (Create, Read)

As a user,
I want to create new tasks and view my existing tasks,
So that I can start organizing my responsibilities.

**Acceptance Criteria:**

**Given** I am on the "Proactive Dashboard" or any main view,
**When** I use the "Quick Add" (+) button to enter a task title and submit,
**Then** a `POST` request is sent to the `/api/v1/tasks` endpoint and the new task appears in my list. (Covers FR1)

**And** Given I navigate to a view that displays tasks,
**When** the component mounts,
**Then** a `GET` request is made to `/api/v1/tasks` to fetch and display all my tasks. (Covers FR2)

**And** Given the UI is displayed,
**When** I view the task list and input fields,
**Then** the interface adheres to the "Hyper-Minimalism" principle from the UX design. (Covers FR11 part)

**Prerequisites:** Story 1.2

**Technical Notes (Enhanced):**
-   **Frontend:** Implement `TaskInput` and `TaskList` components using `shadcn/ui`. The "Quick Add" button should be a persistent floating action button as per the UX spec.
-   **Backend:** Create the `POST /api/v1/tasks` and `GET /api/v1/tasks` endpoints in FastAPI. The `POST` endpoint will handle task creation and the `GET` endpoint will retrieve tasks for the authenticated user.
-   **State Management:** Use `Zustand` for global state or `React Query`/`SWR` to manage the fetching, caching, and updating of the task list.
-   Covers FR1, FR2, FR11, FR21, FR22.

### Story 1.4: Core Task CRUD Functionality (Update, Delete)

As a user,
I want to edit and delete my existing tasks,
So that I can maintain an accurate and clutter-free task list.

**Acceptance Criteria:**

**Given** I have an existing task,
**When** I activate the inline edit function and save,
**Then** a `PUT` request is sent to `/api/v1/tasks/{task_id}` and the task is updated. (Covers FR3)

**And** Given I am in the "Focused Task View",
**When** I swipe the task card away,
**Then** the task is marked for deletion.

**And** Given a task is marked for deletion,
**When** the action is confirmed,
**Then** a `DELETE` request is sent to `/api/v1/tasks/{task_id}` and the task is removed. (Covers FR4)

**And** Given a task is updated or deleted,
**When** another connected device is viewing the same list,
**Then** the change is reflected immediately without a manual refresh. (Covers FR23)

**Prerequisites:** Story 1.3

**Technical Notes (Enhanced):**
-   **Frontend:** Implement inline editing for task items. In the "Focused Task View", implement the swipe gesture for deletion as per the UX design.
-   **Backend:** Create the `PUT /api/v1/tasks/{task_id}` and `DELETE /api/v1/tasks/{task_id}` endpoints in FastAPI.
-   **Real-time:** The frontend will listen for database changes on the `tasks` table using `@supabase/supabase-js`'s realtime subscriptions. This will ensure that any change made on one client is immediately reflected on all other subscribed clients.
-   Covers FR3, FR4, FR23.

### Story 1.5: Task Completion and Reordering

As a user,
I want to mark tasks as complete and reorder them,
So that I can manage my progress and prioritize visually.

**Acceptance Criteria:**

**Given** I have an incomplete task,
**When** I click its checkbox,
**Then** the task's `is_completed` status is set to `true` via a `PUT` request, and the UI updates. (Covers FR5)
**And** The "charging battery" progress visualization for the list updates to reflect the completion.

**And** Given I have multiple tasks in a list,
**When** I drag and drop a task to a new position,
**Then** the new order is persisted in the backend. (Covers FR6)

**And** Given I am using a screen reader,
**When** I navigate to the task list,
**Then** all interactive elements (checkboxes, drag handles) are clearly labeled and keyboard-accessible. (Covers FR24)

**Prerequisites:** Story 1.4

**Technical Notes (Enhanced):**
-   **Backend:** The `is_completed` boolean field in the `tasks` table will be updated. A new column, e.g., `sort_order`, will be added to the `tasks` table to persist the user's custom ordering.
-   **Frontend:** Use a library like `react-beautiful-dnd` or `dnd-kit` to implement drag-and-drop reordering.
-   **UX:** The "charging battery" progress visualization, as defined in the UX spec, should be implemented as a key feedback mechanism for task completion.
-   **Accessibility:** Ensure all custom controls (like drag-and-drop handles) have proper ARIA attributes and are fully keyboard-operable to meet WCAG 2.1 AA standards.
-   Covers FR5, FR6, FR24.

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
**When** the backend saves the task,
**Then** it asynchronously calls the Gemini API with a structured prompt for label generation.

**And** Given the Gemini API returns valid labels,
**When** the backend processes the response,
**Then** it populates the `labels` and `task_labels` tables in the database. (Covers FR8)

**And** Given the Gemini API call fails or returns invalid data,
**When** the backend handles the error,
**Then** the task is still created successfully without any labels, and the error is logged.

**And** Given a task has labels,
**When** the frontend displays the task,
**Then** the labels are shown as distinct visual elements (e.g., tags or badges).

**Prerequisites:** Story 1.3 (Task Create/Read)

**Technical Notes (Enhanced):**
-   **AI Integration:** All calls to the Gemini 2.5 Pro API **MUST** be made from the FastAPI backend to protect the API key, as specified in the architecture (section 4.3).
-   **Database:** The schema will use a `labels` table for unique label names and a `task_labels` join table to create a many-to-many relationship with the `tasks` table, as per the architecture (section 4.1).
-   **Error Handling:** The backend service will implement the fallback strategy from the architecture doc. If the AI call fails, the task creation itself does not fail.
-   **Frontend:** The frontend should be able to gracefully handle tasks that do not have any labels.
-   Covers FR8.

### Story 2.2: AI-Suggested Priority Levels

As a user,
I want the system to automatically suggest a priority level for my tasks,
So that I can focus on what's most important and reduce decision fatigue.

**Acceptance Criteria:**

**Given** I create or edit a task,
**When** the backend saves the task,
**Then** it asynchronously calls the Gemini API with a structured prompt for priority suggestion.

**And** Given the Gemini API returns a valid priority level (e.g., an integer from 1 to 4),
**When** the backend processes the response,
**Then** the `priority` field is updated on the `tasks` table. (Covers FR9)

**And** Given a task has a suggested priority,
**When** the frontend displays the task,
**Then** the priority is clearly indicated (e.g., with a colored icon or border).

**Prerequisites:** Story 2.1

**Technical Notes (Enhanced):**
-   **AI Integration:** As with labels, priority suggestion calls to the Gemini API **MUST** originate from the FastAPI backend. The prompt should ask for a numerical value within a defined range.
-   **Database:** The `priority` column in the `tasks` table, defined as an `integer` in the architecture (section 4.1), will store the AI-suggested value.
-   **Frontend:** The UI should visually represent the priority levels (e.g., 4 = red, 3 = orange, etc.) to provide a quick visual cue to the user.
-   Covers FR9.

### Story 2.3: Filter Tasks by Smart Labels

As a user,
I want to filter my tasks by their smart labels,
So that I can quickly find and focus on specific categories of tasks.

**Acceptance Criteria:**

**Given** I have tasks with AI-generated labels,
**When** I click on a "work" label tag in the UI,
**Then** the frontend makes a `GET` request to `/api/v1/tasks?label=work`.

**And** Given the API returns a filtered list of tasks,
**When** the UI updates,
**Then** only tasks with the "work" label are displayed. (Covers FR10)

**And** Given a filter is active,
**When** I click a "Clear" or "All" button,
**Then** a `GET` request is made to `/api/v1/tasks` and all tasks are displayed again.

**Prerequisites:** Story 2.1

**Technical Notes (Enhanced):**
-   **Backend:** The `GET /api/v1/tasks` endpoint will be enhanced to accept an optional query parameter for `label`. The endpoint will perform a join with the `task_labels` and `labels` tables to filter the results.
-   **Frontend:** The UI will display a list of unique labels from the user's tasks. Clicking a label will trigger the API call with the appropriate query parameter. The state of the current filter must be managed in the frontend's state.
-   Covers FR10.

---

## Epic 3: Advanced Task Management & User Experience
Goal: Implement key UI/UX features and advanced task capabilities to enrich the user experience (Post-MVP).

### Story 3.1: Minimalist User Interface

As a user,
I want to interact with a clean, minimal, and intuitive user interface,
So that I can focus on my tasks without distractions.

**Acceptance Criteria:**

**Given** the application is loaded,
**When** I view the "Proactive Dashboard" and "Focused Task View",
**Then** the layout adheres to the principles of hyper-minimalism and calm aesthetics defined in the UX Design Specification. (Covers FR11)

**And** Given the application is using the "Refined Focus" theme,
**When** I interact with UI elements,
**Then** visual feedback is subtle and non-distracting, using the specified neutral palette and action colors.

**And** Given the UI is displayed on different screen sizes,
**When** I resize the window from mobile to desktop,
**Then** the layout adapts responsively as defined in the UX spec (e.g., widgets reflowing into a grid).

**Prerequisites:** Story 1.3

**Technical Notes (Enhanced):**
-   **UI/UX:** This story is the primary implementation of the visual and aesthetic goals of the project. It involves applying the "Refined Focus" color theme and the "Proactive Dashboard" design direction from the UX Design Specification.
-   **Technology:** Use `shadcn/ui` for core components and `Tailwind CSS` for all styling, as per the architecture and UX decisions.
-   **Responsiveness:** Pay close attention to the responsive layout definitions in the UX spec to ensure a consistent experience across devices.
-   Covers FR11.

### Story 3.2: "Today" View and Filtering

As a user,
I want to see a dedicated "Today" view as the default screen,
So that I can immediately focus on my most urgent daily tasks (Post-MVP).

**Acceptance Criteria:**

**Given** I open the application,
**When** it loads,
**Then** the default view presented is the "Proactive Dashboard" which contains the "Today" view. (Covers FR12)

**And** Given the "Today" view is active,
**When** I view the list of tasks,
**Then** it shows a curated list of tasks scheduled for the current day.

**And** Given I interact with the "Today" view,
**When** I add, edit, or complete a task,
**Then** all core task management functionalities are available.

**Prerequisites:** Story 3.1

**Technical Notes (Enhanced):**
-   **UX:** This feature implements a key part of the "Proactive Dashboard" design direction. The "Today" view is not just a filter, but the primary, curated command center for the user's daily activities.
-   **Backend:** The `GET /api/v1/tasks` endpoint should be enhanced to support a date-based filter, e.g., `GET /api/v1/tasks?date=today`, to fetch tasks scheduled for the current day.
-   **Frontend:** Create a main page component that serves as the "Proactive Dashboard" and fetches the "Today" tasks by default.
-   Covers FR12.

### Story 3.3: Light/Dark Mode Themes

As a user,
I want to switch between light and dark mode themes,
So that I can customize the application's appearance to my preference and reduce eye strain (Post-MVP).

**Acceptance Criteria:**

**Given** I am in the application,
**When** I activate the theme toggle,
**Then** the application's visual theme switches between the "Refined Focus" Light and Dark modes. (Covers FR13)

**And** Given the theme is switched,
**When** I close and reopen the application,
**Then** my chosen theme is remembered and applied automatically.

**And** Given the theme is changed,
**When** I view the UI,
**Then** all `shadcn/ui` components and `Tailwind CSS` styled elements adapt correctly to the selected theme.

**Prerequisites:** Story 3.1

**Technical Notes (Enhanced):**
-   **Frontend:** Implement theme toggling logic using Next.js context or a global state manager like Zustand. Persist theme preference in local storage.
-   **Styling:** Ensure the "Refined Focus" theme, as defined in the UX spec, has `@media (prefers-color-scheme: dark)` or similar CSS variables/classes configured for seamless transitions.
-   Covers FR13.

### Story 3.4: Task Search Functionality

As a user,
I want to search for tasks by keywords,
So that I can quickly find specific tasks within my list (Post-MVP).

**Acceptance Criteria:**

**Given** I am viewing my tasks,
**When** I enter text into the search bar,
**Then** the frontend sends a `GET` request to `/api/v1/tasks/search?q={query}`.

**And** Given the backend responds with tasks matching the search query using PostgreSQL FTS,
**When** the UI dynamically updates,
**Then** only relevant tasks are displayed. (Covers FR14)

**And** Given a search query has been executed,
**When** I clear the search bar,
**Then** the full task list is restored by calling `/api/v1/tasks`.

**Prerequisites:** Story 1.3 (Core Task CRUD)

**Technical Notes (Enhanced):**
-   **Backend:** Implement a dedicated `GET /api/v1/tasks/search` endpoint in FastAPI that leverages PostgreSQL's Full-Text Search (FTS) capabilities. The `tasks` table will need a `tsvector` column and a trigger to update it, as described in the architecture document (section 5.3).
-   **Frontend:** Implement a search input component that debounces user input to avoid excessive API calls. The search results should dynamically update the displayed task list.
-   Covers FR14.

---

## Epic 4: AI-Enhanced Productivity Tools (ADHD Focus - Post-MVP)
Goal: Deliver specialized AI-driven tools to directly address ADHD-related productivity challenges, providing targeted support.

### Story 4.1: AI Task Breakdown Suggestions

As a user,
I want the system to suggest breaking down large tasks into smaller sub-steps,
So that I can reduce overwhelm and make daunting tasks manageable (Post-MVP).

**Acceptance Criteria:**

**Given** I have an unstructured task (e.g., "Plan my vacation") and trigger the "Plan My Day" AI Workflow,
**When** the FastAPI backend orchestrates the AI call to Gemini 2.5 Pro,
**Then** Gemini generates a list of smaller, actionable sub-steps. (Covers FR15)

**And** Given these sub-steps are presented to me in the UI,
**When** I confirm them,
**Then** they are added to my `tasks` table with their `parent_task_id` linked to the original larger task.

**Prerequisites:** Story 2.1 (AI-Generated Smart Labels), Story 1.3 (Core Task CRUD)

**Technical Notes (Enhanced):**
-   **AI Integration:** This feature is a core component of the "Plan My Day" AI Workflow (architecture section 7). The FastAPI backend will construct a detailed prompt for Gemini 2.5 Pro to perform task decomposition.
-   **Database:** The `tasks` table schema supports `parent_task_id` for hierarchical task relationships (architecture section 4.1).
-   **Backend:** A dedicated endpoint (e.g., `POST /api/v1/tasks/{task_id}/breakdown`) will be responsible for sending the task to the AI and processing the response.
-   Covers FR15.

### Story 4.2: AI-Generated Time Estimates

As a user,
I want the system to provide AI-generated time estimates for my tasks,
So that I can better plan my day and manage my time blindness (Post-MVP).

**Acceptance Criteria:**

**Given** I create or edit a task, or trigger the "Plan My Day" AI Workflow,
**When** the FastAPI backend calls the Gemini API for task analysis,
**Then** Gemini provides an approximate time estimate (e.g., "15 minutes," "1 hour"). (Covers FR16)

**And** Given a task has a time estimate,
**When** the task is displayed in the UI,
**Then** the estimate is clearly displayed alongside the task title.

**Prerequisites:** Story 2.1 (AI-Generated Smart Labels)

**Technical Notes (Enhanced):**
-   **AI Integration:** Time estimation will be integrated into the Gemini API calls made from the FastAPI backend as part of the "Plan My Day" AI Workflow. The prompt should request time estimates in a structured format.
-   **Database:** A new nullable column (e.g., `estimated_time_minutes` as an `integer`) will be added to the `tasks` table to store this estimate.
-   **Frontend:** The UI will display this estimated time for each task, potentially using a simple visual cue.
-   Covers FR16.

### Story 4.3: "Just Start Here" Button

As a user,
I want to click a "Just Start Here" button to be directed to the single most important task,
So that I can overcome decision paralysis and initiate work immediately (Post-MVP).

**Acceptance Criteria:**

**Given** I am on the "Proactive Dashboard" or any task view,
**When** I click the prominent "Just Start Here" button,
**Then** the frontend makes a `GET` request to a backend endpoint (e.g., `/api/v1/tasks/next-priority`).

**And** Given the backend applies AI logic to identify the highest priority, most actionable task (considering various factors like deadline, estimated time, and current context),
**When** the frontend receives this task,
**Then** the UI transitions to a "Focused Task View" for that specific task. (Covers FR17)

**Prerequisites:** Story 2.2 (AI-Suggested Priority Levels), Story 3.2 ("Today" View)

**Technical Notes (Enhanced):**
-   **Backend:** A new FastAPI endpoint (`GET /api/v1/tasks/next-priority`) will implement the AI logic to determine the "best" task. This logic will consider factors like `priority`, `due_date`, `estimated_time_minutes`, and potentially user habits.
-   **Frontend:** The "Just Start Here" button will be a prominent feature on the "Proactive Dashboard". Clicking it will trigger the API call and the UI transition.
-   **UX:** The transition to the "Focused Task View" should be smooth and calming, minimizing distractions.
-   Covers FR17.

### Story 4.4: Integrated Visual Timers

As a user,
I want to initiate integrated visual timers for my tasks,
So that I can maintain focus and manage my work sessions effectively (Post-MVP).

**Acceptance Criteria:**

**Given** I am in the "Focused Task View" for a specific task,
**When** I activate a Pomodoro timer (e.g., 25 minutes),
**Then** a subtle, visual countdown is displayed within the Focused Task View. (Covers FR18)

**And** Given the timer completes,
**When** the session ends,
**Then** a gentle, non-intrusive notification prompts me to take a break or extend the session.

**Prerequisites:** Story 4.2 (AI-Generated Time Estimates)

**Technical Notes (Enhanced):**
-   **Frontend:** Implement a client-side timer component that integrates seamlessly into the "Focused Task View". The timer should provide clear visual feedback without being distracting.
-   **UX:** Notifications upon timer completion should adhere to the "Notifications & Nudges" patterns from the UX Design Specification (section 7.1), being subtle and dismissible.
-   Covers FR18.

### Story 4.5: Smart, Gentle Nudge Reminders

As a user,
I want to receive smart, context-aware nudge reminders,
So that I can stay on track with my priorities without feeling overwhelmed (Post-MVP).

**Acceptance Criteria:**

**Given** a high-priority task is approaching its due time,
**When** I am not actively engaging with the application,
**Then** the FastAPI backend service, using AI logic, determines an appropriate moment to send a gentle, non-judgmental notification. (Covers FR19)

**And** Given a notification is received (e.g., a toast notification or push notification),
**When** I interact with it,
**Then** I am directed back to the relevant task within the application.

**Prerequisites:** Story 2.2 (AI-Suggested Priority Levels), Story 6.1 (Email Notifications or push notification setup from architecture)

**Technical Notes (Enhanced):**
-   **Backend:** This will likely require a dedicated background job or a scheduled task (potentially using `Inngest` as per architecture section 6.2) to periodically check task due dates and user activity. AI logic will be developed in the backend to determine "context-aware" triggers for nudges.
-   **Frontend/UX:** Notifications will adhere to the "Notifications & Nudges" patterns from the UX Design Specification (section 7.1), being subtle, dismissible, and informative without being distracting.
-   Covers FR19.

### Story 4.6: Scheduled Task Management

As a user,
I want to schedule tasks for specific days,
So that I can plan my workload and manage my commitments effectively (Post-MVP).

**Acceptance Criteria:**

**Given** I have a task,
**When** I edit it,
**Then** I can assign a specific `scheduled_date` (or `due_date`) to it via a UI date picker. (Covers FR20)

**And** Given tasks are scheduled,
**When** the scheduled day arrives,
**Then** these tasks are prominently displayed in relevant views (e.g., "Today" view on the "Proactive Dashboard").

**Prerequisites:** Story 1.3 (Core Task CRUD)

**Technical Notes (Enhanced):**
-   **Database:** A new nullable `scheduled_date` column (`timestamp with time zone`) will be added to the `tasks` table to support this feature. This date will be distinct from `due_date` if both are needed.
-   **Frontend:** Implement a date picker component (e.g., from `shadcn/ui`) for assigning dates. The "Today" view will need to filter and display tasks based on this new field.
-   Covers FR20.