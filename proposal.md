# SG-Trine
# Prioritize – AI-Enhanced Smart To-Do List Application

## Project Title
Prioritize – AI-Enhanced Smart To-Do List Application

## Background
Task management apps are common, but many users still struggle with overwhelm, poor prioritization, and unclear goals. Traditional to-do lists tend to become long, unstructured “brain dumps” instead of effective productivity tools. With the rise of AI-assisted workflows, there is an opportunity to create a smarter, more intuitive task management experience that helps users stay focused, organized, and goal-oriented.

“Prioritize” aims to solve this by combining a simple interface with AI-generated task categorization, priority suggestions, and smart labels. This makes the app accessible for everyday users while demonstrating how AI can act as multiple development roles in the software process, as required in this course.

## Purpose
The purpose of the application is to develop a clean, minimal, easy-to-use to-do list tool that uses AI to improve productivity. The system will allow users to enter tasks normally, while an AI agent will automatically classify them (e.g., “Work”, “Home”, “Urgent”, “Low Effort”, etc.) and suggest priority levels. This creates a more structured overview without requiring additional effort from the user.

The project’s goal is not to compete with large commercial apps, but to implement a realistic, functioning AI-supported software product within the scope of the course and demonstrate understanding of agent-based development, BMAD-framework usage, and the collaboration between human and AI agents.

## Target Users
**Primary users**
- Students
- Everyday individuals managing daily tasks
- People who want a simple, structured to-do system without unnecessary complexity

**Secondary users**
- Anyone curious about AI-supported productivity tools
- Beginners who need an intuitive interface

Users do not need technical experience. The interface must be simple enough for anyone to use without a tutorial.

### Designing for ADHD Users
In addition to being a general-purpose to-do app, "Prioritize" will be specifically designed to be helpful for users with ADHD. Many of its core AI features directly address challenges with executive functions like task initiation, prioritization, and time perception. The goal is to create a tool that reduces overwhelm and provides a clear, focused path forward.

### Core Functionality

*   **AI-Powered "Plan My Day":** The core feature where users input tasks and the AI automatically organizes, prioritizes, and breaks them down into a manageable, focused plan.
*   **Focused Task View:** A minimalist, single-task view designed to reduce overwhelm, with gesture-based navigation.
*   **Proactive Dashboard:** A "command center" main view with dynamic widgets for progress, calendar events, and proactive AI suggestions.
*   **Smart Sorting Options:** The ability to re-sort tasks by importance, duration, energy level, or context.
*   **Collaboration Suite:** Share lists, assign tasks, and track progress with other users.
*   **Advanced AI Assistance:** Includes AI Habit Learning, Time Prediction, Task Optimization, and Smart Notifications.
*   **Customization & Control:** Manual sub-task creation, saved list templates, and photo attachments.
*   **Calendar & Location Integration:** Sync with external calendars and use location services for automatic travel time calculation.

## Technical Scope

 
### Frontend Specification
- **Framework**: Next.js 14+ with App Router for server-side rendering and optimal performance
- **Language**: TypeScript for type safety and better AI-assisted development
- **Styling**: Tailwind CSS for rapid, responsive UI development
- **State Management**: Zustand for lightweight, scalable global state management
- **Data Visualization**: Recharts for interactive, customizable supply chain visualization
- **Shadcn UI**: Shadcn UI for rapid, responsive UI development
- **Forms**: React Hook Form with Zod validation for robust form handling
- **Authentication UI**: Supabase Auth UI components + custom styling
- **Real-time Updates**: Supabase Realtime client for live game monitoring and multiplayer
- **API Communication**: Axios with interceptors for authenticated requests
- **Deployment**: Vercel for frontend hosting with automatic CI/CD

**Architecture Pattern**: Component-based architecture with clear separation between presentation components, container components, and business logic hooks.

### Backend Specification
- **Framework**: FastAPI (Python) for high-performance RESTful API development
- **Language**: Python for AI integration compatibility and rapid development
- **Database**: Supabase (PostgreSQL) for managed database and real-time capabilities
- **Authentication**: Supabase Auth for built-in user management, JWT tokens, and email verification
- **Authorization**: Row Level Security (RLS) policies in Supabase + role-based middleware (student/instructor/admin roles)
- **ORM**: SQLAlchemy for database operations and type safety
- **Database Migrations**: Alembic for version-controlled schema changes
- **AI Integration**:
  - Gemini 2.5 pro for AI-powered task categorization and priority suggestions
  - Custom prompt engineering for consistent AI behavior
  - Fallback logic for API failures
- **API Documentation**: FastAPI automatic OpenAPI/Swagger documentation
- **Testing**: Pytest for unit and integration tests
- **Build Tool**: UV for fast Python package management
- **Deployment**: Vercel (FastAPI supports Vercel deployment)

**API Architecture**: RESTful API design with versioning (/api/v1/) and clear resource-oriented endpoints. Supabase Realtime for live game updates instead of WebSockets.

### Data Model
- **Task**: 
  - `id`: string (UUID)
  - `description`: string
  - `is_completed`: boolean
  - `ai_labels`: string[] (e.g., ["work", "urgent"])
  - `ai_priority`: number (e.g., 1-4)
  - `created_at`: timestamp


Complex features like user authentication or multi-user systems are out of scope for the MVP.

## Success Criteria
- A clean, functional to-do application that runs without errors
- AI successfully generates smart labels and priorities
- The app demonstrates agent-based development as taught in the course
- Documentation (planning, architecture, prompts, reflections) included
- Project can be shown and explained during oral exam

## Risks and Limitations
- Over-engineering: keep the project simple
- Time pressure: scope must stay realistic
- AI consistency: classification may vary, acceptable for the course
- Prioritization: avoid scope creep

## User Flows
### User Flow 1: Add a New Task
1. User opens the application.
2. User clicks “Add task”.
3. User types in a task description.
4. AI suggests labels and priority.
5. User accepts or adjusts suggestions.
6. Task is added to the list and shown in overview.

### User Flow 2: View and Filter Tasks
1. User opens the task list.
2. User selects a filter (e.g., “Urgent”, “Work”).
3. Application displays filtered tasks.
4. User clicks a task to view details or update it.

### User Flow 3: Edit or Complete a Task
1. User clicks on an existing task.
2. AI updates labels/priority if text is changed.
3. User edits or marks task as completed.
4. Updated task appears in the list.

## How to get started (local prototype)
1. Install Python 3.10+.
2. Get an OpenAI API key if you want to use GPT locally and set it as `OPENAI_API_KEY`.
3. Install dependencies: `pip install -r requirements.txt`.
4. Run the simple prototype: `python agent_simple.py` and enter tasks to see AI labels/priorities.

## Next steps
- Build a simple frontend (React/Next) that calls an API endpoint to create tasks and request AI labels.
- Implement a small backend (FastAPI or Express) to store tasks and call the AI.
- Add tests and CI (workflow provided).
- Add documentation about agent roles, prompts, and the BMAD approach for the course deliverable.
