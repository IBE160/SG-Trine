# Story 1.1: Project Setup and Initial Deployment

Status: done

## Story

As a developer,
I want to set up the project infrastructure (Next.js, FastAPI, Supabase, Vercel),
So that I can begin developing and deploying the application efficiently.

## Acceptance Criteria

1.  **Project Setup & Deployment:**
    1.1. The monorepo structure (Next.js frontend, FastAPI backend in `api/`) is established locally after initial setup commands.
    1.2. The Next.js frontend successfully deploys to Vercel.
    1.3. The FastAPI app in the `api/` directory successfully deploys as a Vercel serverless function.
    1.4. A "Hello World" endpoint on the deployed FastAPI function is reachable.

## Tasks / Subtasks

- [ ] **Task 1: Establish Monorepo Structure Locally (AC 1.1)**
  - [ ] Initialize Next.js frontend: `npx create-next-app@latest nextjs-frontend --typescript --eslint --app --src-dir --import-alias "@/*"` [Source: `architecture-2025-11-28.md#2.-Starter-Template-Decision`]
  - [ ] Create `api/` directory at the project root level
  - [ ] Set up Python virtual environment in `api/`: `python -m venv venv`
  - [ ] Activate venv and install FastAPI dependencies: `pip install fastapi uvicorn[standard] supabase-py pydantic-settings`
  - [ ] Create `main.py` in `api/` with a basic FastAPI app.

- [ ] **Task 2: Configure Vercel Deployment (AC 1.2, 1.3, 1.4)**
  - [ ] Push local monorepo to a Git provider (e.g., GitHub).
  - [ ] Connect repository to Vercel.
  - [ ] Configure Vercel project settings for monorepo (specify `nextjs-frontend` as root).
  - [ ] Configure Vercel to detect FastAPI app in `api/` as a serverless function.
  - [ ] Add necessary environment variables to Vercel (e.g., placeholder Supabase URL/keys, Gemini API Key if required for initial build). [Source: `architecture-2025-11-28.md#Technical-Notes-Enhanced`]

- [ ] **Task 3: Verify End-to-End Deployment (AC 1.4)**
  - [ ] Implement a minimal "Hello World" endpoint in the FastAPI app (`api/main.py`).
  - [ ] Make a basic fetch request from the Next.js frontend to the FastAPI "Hello World" endpoint.
  - [ ] Deploy to Vercel.
  - [ ] Verify that the Next.js frontend deploys successfully.
  - [ ] Verify that the FastAPI serverless function deploys successfully.
  - [ ] Access the frontend in a browser and verify the "Hello World" message from the backend is displayed.

- [ ] **Task 4: Basic Testing Setup**
  - [ ] Set up basic `Jest` / `React Testing Library` for frontend. [Source: `architecture-2025-11-28.md#4.-Cross-Cutting-Concerns`]
  - [ ] Set up basic `pytest` for backend. [Source: `architecture-2025-11-28.md#4.-Cross-Cutting-Concerns`]
  - [ ] Write a simple unit test for one frontend component.
  - [ ] Write a simple unit test for one backend endpoint.


## Dev Notes

- **Architecture Patterns & Constraints:** This story focuses on implementing the "monorepo" project structure as defined in the Architecture Document (Section 5). Frontend-backend communication will adhere to the specified API design (`/api/v1` RESTful, Pydantic validation) and deployment strategy on Vercel.
- **Source Tree Components to Touch:**
    - `nextjs-frontend/`: Initial Next.js application, including `src/app`, `src/components`, `package.json`.
    - `api/`: Initial FastAPI application, including `app/main.py`, `requirements.txt`.
    - `.env.local`: Environment variable configuration for both frontend and backend.
    - Vercel project settings (via UI or `vercel.json` if needed).
- **Testing Standards Summary:** Unit testing with `Jest` and `React Testing Library` for frontend, `pytest` for backend. E2E testing with `Playwright`. Initial tests will focus on verifying project setup and "Hello World" deployment.

### References

- [Source: `architecture-2025-11-28.md#2.-Starter-Template-Decision`]
- [Source: `architecture-2025-11-28.md#3.1.-Critical-Architectural-Decisions`]
- [Source: `architecture-2025-11-28.md#5.-Project-Structure`]
- [Source: `architecture-2025-11-28.md#8.-Implementation-Patterns`]
- [Source: `tech-spec-epic-1.md#1.-Project-Setup-&-Deployment`]

## Dev Agent Record

### Context Reference

- docs/sprint-artifacts/1-1-project-setup-and-initial-deployment.context.xml

### Agent Model Used

{{agent_model_name_version}}

### Debug Log References

### Completion Notes List

### File List

## Change Log

