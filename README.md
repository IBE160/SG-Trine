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

## Core Functionality (MVP)

### Must Have
- Create, edit, and delete tasks
- Tasks stored locally or in a simple backend
- AI-generated smart labels (e.g., “urgent”, “work”, “personal”)
- AI-generated priority suggestions
- Filter tasks by smart labels
- Clean, minimal UI

### Should Have (if time allows)
- Light/Dark mode
- Ability to mark tasks as complete
- Reorder tasks
- Task search

### Nice to Have (optional)
- AI suggestions for breaking down tasks into steps
- Daily summary (“Here are your top 3 tasks today…”)
- Scheduling tasks for specific days
- Reminders

## Technical Scope
For MVP, keep the scope simple. Suggested stack:
- Frontend: Next.js or simple React
- Backend: Node.js or Python FastAPI
- Database: Simple JSON file, Supabase, or in-repo storage
- AI Integration: GPT model for classification and prioritization

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
