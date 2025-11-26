# Product Brief: Prioritize – AI-Enhanced Smart To-Do List

- **Author:** Analyst Agent
- **Date:** 2025-11-26
- **Source Documents:** `proposal.md`, `brainstorming-session-results-2025-11-26.md`, `research-technical-2025-11-26.md`

---

## 1. The Big Picture

### The Problem
Task management is a universal challenge. Many users, particularly those with executive function difficulties like ADHD, find traditional to-do lists overwhelming. These lists often become unstructured "brain dumps" that increase anxiety rather than productivity, making it difficult to prioritize and initiate tasks.

### Our Solution
**"Prioritize"** is a minimal, easy-to-use to-do list application that leverages AI to transform a simple task list into a smart, actionable workflow. By automatically categorizing tasks, suggesting priorities, and providing focus-enhancing tools, the app aims to reduce overwhelm and help users achieve their goals more effectively.

For the purpose of the IBE160 course, this project will also serve as a practical demonstration of agent-based development methodologies using the BMAD framework.

### Success Metrics
- **Functional MVP:** A clean, stable application that runs without errors and delivers all "Must Have" features.
- **Effective AI:** The AI successfully and consistently generates relevant smart labels and priority levels for a wide range of user inputs.
- **Coursework Compliance:** The project clearly demonstrates the principles of agent-based development and is documented thoroughly for the oral exam.

## 2. Target Audience

### Primary Users
- Students and other individuals managing a mix of academic, personal, and professional tasks.
- Everyday users who feel overwhelmed by complex productivity software and desire a simple, structured system.

### ADHD User Focus
"Prioritize" is specifically designed to be helpful for users with ADHD. Features are tailored to address common challenges associated with executive dysfunction:
- **Reducing Overwhelm:** A "Today" view and AI-powered task "chunking" will make long lists manageable.
- **Aiding Task Initiation:** A "Just Start Here" button will remove decision paralysis.
- **Addressing Time Blindness:** AI-generated time estimates will help users realistically plan their time.
- **Enhancing Focus:** A minimalist UI and smart, gentle nudges will help users stay on track.

## 3. Core Features & Scope

### Must-Haves (MVP)
- Full CRUD (Create, Read, Edit, Delete) functionality for tasks.
- Ability to mark tasks as complete and reorder them.
- AI-generated smart labels (e.g., "work," "personal," "urgent").
- AI-generated priority suggestions.
- Ability to filter tasks by their smart labels.
- A clean, minimal, and intuitive user interface.
- All task data stored in a simple backend (Supabase).

### Should-Haves (Post-MVP)
- A "Today" view as the application's default screen.
- AI suggestions for breaking down large tasks into smaller sub-steps.
- AI-generated time estimates for tasks (e.g., "Approx. 15 mins").
- Light/Dark mode themes.
- Task search functionality.

### Nice-to-Haves (Future Iterations)
- A "Just Start Here" button to launch the single most important task.
- Integrated visual timers (e.g., Pomodoro).
- Smart, gentle nudge reminders.
- The ability to schedule tasks for specific days.

## 4. Technical Strategy

### Stack Overview
- **Frontend:** Next.js (TypeScript) with Tailwind CSS and Shadcn UI.
- **Backend:** FastAPI (Python) for the core API.
- **AI:** Gemini 2.5 Pro via the `google-generativeai` library.
- **Database & Auth:** Supabase (PostgreSQL) for data persistence, user authentication, and real-time updates.
- **Deployment:** Vercel for continuous integration and deployment of both frontend and backend.

### Efficient Implementation Plan
1.  **Develop the Core AI Logic:** Create a standalone Python script to validate the core AI prompt that takes a task description and returns categorized labels and a priority level.
2.  **Build a Vertical Slice:** Wrap the AI script in a FastAPI endpoint. Build a minimal Next.js page to hit this endpoint and display the result. This creates a full end-to-end test of the core functionality.
3.  **Implement the Full UI:** Use Shadcn UI to rapidly build out the full user interface around the working vertical slice, implementing all MVP features.
4.  **Integrate Database:** Connect the application to Supabase to persist tasks and user data.

## 5. Known Risks
- **Scope Creep:** The project has many "Should Have" and "Nice to Have" features. A disciplined focus on the "Must-Have" list is essential to ensure the MVP is delivered on time.
- **AI Consistency:** The quality of AI-generated suggestions may vary. Robust prompt engineering and clear error handling for API failures will be critical to mitigate this.
- **Time Pressure:** As with any academic project, the deadline is a key constraint. The efficient implementation plan is designed to manage this risk by prioritizing the most critical features first.
