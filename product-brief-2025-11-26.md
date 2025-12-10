# Product Brief: Prioritize – AI-Enhanced Smart To-Do List

- **Author:** Analyst Agent
- **Date:** 2025-11-26
- **Source Documents:** `proposal.md`, `brainstorming-session-results-2025-11-26.md`, `research-technical-2025-11-26.md`

---

## 1. The Big Picture

### The Problem
Task management is a universal challenge. Many users, particularly those with executive function difficulties like ADHD, find traditional to-do lists overwhelming. These lists often become unstructured "brain dumps" that increase anxiety rather than productivity, making it difficult to prioritize and initiate tasks.

### Our Solution

**"Prioritize"** is an AI-enhanced smart to-do list application designed around a **"Proactive Dashboard"** that acts as the user's central hub. It leverages AI to transform chaotic task inputs into an organized, prioritized, and actionable daily plan, presented in a focused, single-task view. By providing intelligent sorting, time estimation, habit-based nudges, and collaborative tools, the app aims to significantly reduce overwhelm and help users achieve their goals more effectively and with greater clarity.

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
*   **Reducing Overwhelm:** The "Proactive Dashboard" provides a calm starting point, while the "Focused Task View" (showing only one task at a time) minimizes visual clutter and decision fatigue.
*   **Aiding Task Initiation:** The "Plan My Day" workflow removes the cognitive load of organizing and prioritizing. The app tells the user what to do next, making it easier to start.
*   **Addressing Time Blindness:** AI-generated time estimates and automated travel time calculations help users develop a more realistic perception of how long tasks will take.
*   **Enhancing Focus & Memory:** Smart, gentle nudges (e.g., for finished laundry or upcoming habits) act as an external working memory, helping users stay on track without being disruptive.

## 3. Core Features & Scope

## 3. Core Features & Scope

"Prioritize" is designed around an AI-enhanced **"Proactive Dashboard"** that serves as the user's central hub, seamlessly integrating advanced AI capabilities with intuitive controls and collaborative tools.

### Key Capabilities:

*   **AI-Powered "Plan My Day" Workflow:** The flagship feature that intelligently transforms a user's task input into an organized, prioritized, and time-estimated daily plan, presented in a focused, single-task view.
*   **Dynamic Dashboard Experience:** Features contextual widgets (e.g., Today's Progress, Next Calendar Event, Shared Activity) and proactive AI suggestions based on user habits.
*   **Smart Task Management:** Includes manual sub-task creation, AI Task Optimization (merging related tasks), AI Time Prediction, and intelligent sorting options (by importance, duration, energy, context).
*   **Smart Notifications & Nudges:** Time-based alerts for task dependencies (e.g., "laundry finished") and proactive habit-based reminders (e.g., "pack swimwear for tomorrow's swim").
*   **Collaboration Suite:** Enables sharing of task lists, assigning tasks to collaborators (or oneself), and tracking shared progress.
*   **Connectivity & Integrations:** Seamless integration with external calendars and optional location-based travel time calculations for tasks.
*   **Customization & Control:** Users have full flexibility to edit AI-generated plans, save and reuse list templates (limited in free version), attach photos to tasks, and customize app settings (including language selection).
*   **Motivation & Progress:** Visual "charging battery" progress indicators for individual tasks and overall daily goals.

### Monetization Strategy:

The app will operate on a **Freemium model** to maintain a calm, ad-free user experience. The free version will offer core "Plan My Day" functionality with limited saved templates. The premium subscription unlocks all advanced AI features, collaboration tools, calendar integration, photo attachments, and unlimited saved templates.

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
