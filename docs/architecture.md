# ibe160 - Scale Adaptive Architecture

## 1. Project Context Understanding

I'm reviewing your project documentation for ibe160 - Prioritize.
I see 4 epics with 18 total stories, alongside a detailed UX specification.

**Key aspects I notice:**
-   **Core Functionality:** A comprehensive to-do list, with robust backend storage.
-   **AI Integration:** Central to intelligent task categorization, priority suggestions, and future productivity enhancements leveraging Gemini 2.5 Pro.
-   **ADHD-Centric Design:** Focused on a hyper-minimalist UI, intuitive guidance, and features specifically designed to reduce overwhelm and enhance focus.
-   **Technology Stack:** Next.js frontend, FastAPI backend, Supabase for database, authentication, and real-time updates, deployed via Vercel.
-   **Non-Functional Requirements:** High performance, strong security, inherent scalability, and adherence to WCAG AA accessibility standards.
-   **UX Principles:** Emphasizes calm, control, and a novel "Plan My Day" workflow.

This understanding will help me guide you through the architectural decisions needed to ensure AI agents implement this consistently.

Does this match your understanding of the project?

## 2. Starter Template Decision

You have approved the use of a Next.js/FastAPI boilerplate. While a single CLI command for a complete monorepo setup is not universally standardized, a typical setup involves initializing Next.js and FastAPI projects separately and configuring them to work together.

Here are the recommended initialization steps to create your project's foundation:

```bash
# 1. Create Next.js Frontend
npx create-next-app@latest nextjs-frontend --typescript --eslint --app --src-dir --import-alias "@/*"
cd nextjs-frontend
# (Further frontend setup will be done here)
cd .. # Go back to project root

# 2. Create FastAPI Backend
mkdir fastapi-backend
cd fastapi-backend
python -m venv venv
# On Windows, use `venv\Scripts\activate` or `.\venv\Scripts\Activate.ps1`
# source venv/bin/activate
pip install fastapi uvicorn[standard]
# Create fastapi-backend/main.py with initial setup as described in search results.
# cd .. # Go back to project root
```

These initial commands establish the following architectural decisions, which are considered 'PROVIDED BY STARTER':

*   **Frontend Framework:** Next.js (App Router), TypeScript, React, ESLint.
*   **Backend Framework:** FastAPI, Python.
*   **Styling Foundation:** Tailwind CSS (to be integrated), for use with `shadcn/ui`.
*   **Project Structure:** A monorepo approach with `nextjs-frontend` and `fastapi-backend` directories.
*   **Type Safety:** End-to-end type safety through TypeScript on the frontend and FastAPI's Pydantic models on the backend.
*   **CORS Configuration:** Initial CORS setup will be included in the FastAPI backend to allow communication with the Next.js frontend.

Further decisions regarding database integration (Supabase), authentication, and specific tooling will be made explicitly during this architecture workflow.

**Note for First Implementation Story:**
The very first implementation story should involve executing these commands, setting up the basic project structure, and deploying a minimal 'Hello World' style application to verify the end-to-end connection between the Next.js frontend and FastAPI backend, deployed on Vercel. This will establish the foundational technical environment.

## 3. Decision Identification and Facilitation Plan

Great! I've analyzed your project's requirements and identified the key technical decisions we need to make. Don't worry – I'll guide you through each one and explain why it matters.

Many foundational decisions are already set by your project's Product Requirements (PRD) and chosen starter template, which is fantastic! For example, we know we're using Next.js for the frontend, FastAPI for the backend, Supabase for the database and authentication, and Vercel for deployment.

Now, we'll focus on the remaining architectural decisions. I've grouped them into three levels of importance:

**Critical Decisions:** These are the absolute must-haves that form the core of our application. We need to define how our database will be structured, how our Next.js frontend and FastAPI backend will talk to Supabase and the Gemini AI, and how everything will communicate and be deployed.

**Important Decisions:** These will shape how our application works, covering things like how users log in, where files are stored, how search functions, and strategies to keep the app fast.

**Nice-to-Have Decisions:** These are features we can consider later, like email notifications or more complex AI processing, once the core is solid.

Are you ready to start tackling these decisions, one by one?

## 4. Critical Architectural Decisions

The following critical decisions have been made to establish the core architecture.

### Decision Record: `decision_record`

#### 4.1. Database Schema Design (Supabase/PostgreSQL)

The database schema is designed to be simple and effective for the application's needs.

*   **`users`**: This table is provided by Supabase Auth and stores user information.
*   **`tasks`**: Stores the core task data.
    *   `id`: `uuid`, primary key
    *   `user_id`: `uuid`, foreign key to `users.id`
    *   `title`: `text`, not null
    *   `description`: `text`, nullable
    *   `is_completed`: `boolean`, default `false`
    *   `due_date`: `timestamp with time zone`, nullable
    *   `priority`: `integer`, nullable (e.g., 1-4)
    *   `created_at`: `timestamp with time zone`, default `now()`
    *   `updated_at`: `timestamp with time zone`, default `now()`
    *   `parent_task_id`: `uuid`, foreign key to `tasks.id` (for sub-tasks)
*   **`labels`**: Stores AI-generated labels.
    *   `id`: `uuid`, primary key
    *   `name`: `text`, unique, not null
*   **`task_labels`**: A join table for the many-to-many relationship between tasks and labels.
    *   `task_id`: `uuid`, foreign key to `tasks.id`
    *   `label_id`: `uuid`, foreign key to `labels.id`

#### 4.2. Supabase Integration Strategy

*   **Data Access:** The frontend interacts with the database primarily through the FastAPI backend to centralize data logic. The backend will use `supabase-py` to communicate with the database.
*   **Authentication:** The Next.js frontend uses `@supabase/supabase-js` for user authentication and session management. JWTs from Supabase are sent in the `Authorization` header to the FastAPI backend, which validates them to authorize requests.
*   **Real-time:** The frontend subscribes to `tasks` table changes using `@supabase/supabase-js` for live UI updates.
*   **Row Level Security (RLS):** Policies are enabled on all user data tables to ensure users can only access and modify their own data.

#### 4.3. AI Integration Strategy (Gemini 2.5 Pro)

*   **API Calls:** All Gemini API calls are made from the FastAPI backend to protect the API key.
*   **Prompt Management:** Prompts are constructed and managed in the backend, stored in a configuration file for consistency.
*   **Error Handling & Fallback:** Backend services wrap Gemini API calls in `try...except` blocks, logging errors and returning a graceful response to the frontend (e.g., without AI data) if an API call fails.

#### 4.4. API Design (FastAPI)

*   **Endpoint Structure:** A RESTful API design is used for clear and predictable endpoints (e.g., `POST /api/v1/tasks`, `GET /api/v1/tasks/{task_id}`).
*   **Data Validation:** Pydantic models are used for robust request and response validation, ensuring end-to-end type safety.
*   **Authentication:** Endpoints use FastAPI's dependency injection system to verify the Supabase JWT from the `Authorization` header before allowing access.

#### 4.5. Frontend/Backend Communication

*   **API Client:** The Next.js frontend uses a dedicated API client (e.g., `axios` or a `fetch` wrapper) to communicate with the FastAPI backend, configured via a `NEXT_PUBLIC_API_URL` environment variable.
*   **Data Transfer:** JSON is the standard format for data exchange.
*   **Authentication:** The frontend includes the Supabase JWT in the `Authorization: Bearer <token>` header on every request.

#### 4.6. Deployment Strategy (Vercel)

*   **Monorepo Deployment:** The project is deployed as a monorepo on Vercel.
*   **Next.js Frontend:** Deployed as a standard Next.js application.
*   **FastAPI Backend:** The FastAPI application is placed inside an `api/` directory within the Next.js project, allowing Vercel to automatically deploy it as serverless functions.
*   **Environment Variables:** All secrets (Supabase keys, Gemini API key, etc.) are stored as environment variables in the Vercel project settings.

## 5. Important Architectural Decisions

The following important decisions have been made to shape the architecture.

#### 5.1. Authentication Details (Supabase Auth & RLS)

*   **Authentication Flow:** The frontend, using `@supabase/supabase-js`, handles user sign-up/in and stores the resulting JWT securely in a browser cookie. This JWT is sent in the `Authorization` header for all API requests.
*   **Backend Authorization:** A FastAPI dependency verifies the JWT signature using Supabase's public key (which will be cached) and extracts the user ID. This confirms the user's identity for the API.
*   **RLS Policies:** As established, Row Level Security policies will be strictly enforced at the database level, providing a final layer of security to ensure users can only access their own data.

#### 5.2. File Storage (Supabase Storage)

*   **Strategy:** Supabase Storage is the designated solution for storing user-uploaded photos for tasks.
*   **Upload Flow:** The frontend requests a signed upload URL from the FastAPI backend. The backend generates this URL, specifying the allowed file type, size, and a path that includes the `user_id` (e.g., `user_uploads/{user_id}/{file_name}`). The frontend then uploads the file directly to Supabase Storage.
*   **Access Control:** RLS policies on Supabase Storage buckets will ensure users can only access files they own.

#### 5.3. Search Functionality (PostgreSQL FTS)

*   **Initial Approach:** For the MVP, the architecture will utilize PostgreSQL's built-in Full-Text Search (FTS), available through Supabase.
*   **Implementation:** A `tsvector` column will be added to the `tasks` table, automatically updated by a database trigger. A FastAPI endpoint (`GET /api/v1/tasks/search`) will use `to_tsquery` to search against this column.
*   **Rationale:** This approach is efficient and avoids the complexity of adding an external search service for initial requirements.

#### 5.4. Caching Strategy (FastAPI)

*   **Strategy:** A simple in-memory cache will be used in the FastAPI backend to improve performance for frequently accessed, non-user-specific data (e.g., public labels).
*   **Implementation:** The `fastapi-cache2` library is a suitable choice for this purpose. User-specific data will not be cached to avoid complexity and potential data leakage.

#### 5.5. Configuration Management

*   **Secrets Management:** All secrets (API keys, database URLs, JWT secrets) will be managed exclusively as environment variables and will never be hardcoded.
*   **Local Development:** A `.env.local` file (listed in `.gitignore`) will be used for both the Next.js and FastAPI applications.
*   **Production (Vercel):** All environment variables will be securely stored in the Vercel project settings.
*   **Configuration Loading:** Next.js automatically loads the environment variables. For FastAPI, `pydantic-settings` will be used to load and validate the configuration.

## 6. Future-Facing Architectural Decisions (Nice-to-Have)

The following decisions are documented to guide future development and can be implemented post-MVP.

#### 6.1. Email Notifications

*   **Strategy:** For future email needs (e.g., password resets), a transactional email service will be used.
*   **Recommendation:** `Resend` is a modern, developer-friendly choice that integrates well with React for templating (`react-email`).
*   **Implementation:** A dedicated endpoint in the FastAPI backend will handle sending emails via the Resend SDK.

#### 6.2. Background Task Processing

*   **Strategy:** For long-running or scheduled tasks, a dedicated background job processing system will be used.
*   **Recommendation:** `Inngest` is a strong choice due to its serverless-friendly architecture that works well with Vercel.
*   **Implementation:** Functions will be defined in the FastAPI backend and triggered by events, with Inngest managing execution, retries, and logging.

#### 6.3. Advanced AI Features (Vector Database)

*   **Strategy:** To support future features like semantic search, a vector database will be required.
*   **Recommendation:** `pgvector`, a PostgreSQL extension, is the ideal choice as it is supported by Supabase and minimizes architectural complexity.
*   **Implementation:** The `pgvector` extension will be enabled in Supabase. The FastAPI backend will generate embeddings (using a Gemini/Google model) and perform similarity searches.