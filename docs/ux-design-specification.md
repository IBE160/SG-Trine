# ibe160 UX Design Specification

_Created on 2025-11-26 by Trine_
_Generated using BMad Method - Create UX Design Workflow v1.0_

---

## Executive Summary

**Vision:** "Prioritize" is an AI-enhanced smart to-do list application designed to reduce overwhelm and boost productivity.
**Users:** It's for anyone who feels swamped by traditional to-do lists, with a special focus on supporting users with ADHD.
**Core Experience:** The core experience is effortlessly adding tasks and letting the AI intelligently sort, break down, and prioritize them.
**Desired Feeling:** The app should make users feel calm, in control, and motivated.
**Platform:** It will be a responsive web app that works beautifully on both desktop and mobile browsers.
**Inspiration:** We're creating a unique experience inspired by the simplicity of a basic notes app but with powerful AI intelligence.
**UX Complexity:** The app will be simple to use, but the AI features are novel, so we will design them carefully together.

---

## 1. Design System Foundation

### 1.1 Design System Choice

**Chosen Design System:** shadcn/ui

**Rationale:** shadcn/ui is an ideal choice for this project due to its modern approach, seamless integration with Tailwind CSS and Next.js, and strong focus on accessibility. Its "copy-paste" philosophy grants full control over component customization, allowing for a unique brand identity while leveraging high-quality, pre-built components. This accelerates development while ensuring a clean, minimal, and highly functional user interface that aligns with the project's goal of reducing overwhelm and fostering a sense of calm and control. It provides an excellent balance of speed and customizability, making it perfect for creating a distinct and user-friendly application.

---

## 2. Core User Experience

### 2.1 Defining Experience

The defining experience of "Prioritize" is the feeling of **manageability**. Users should feel that their daily tasks are not only organized but are truly manageable, making the app an essential and desired tool for their daily lives.

This is achieved through a core interaction loop centered on the effortless addition of tasks, with the AI intelligently understanding, deconstructing, and prioritizing them. The user simply adds a task (e.g., "wash clothes"), and the application automatically recognizes its sub-steps, dependencies, and time-based nature. The most critical user action is this seamless translation of a complex mental task into a manageable, prioritized workflow, removing the user's cognitive load.

The application will be a web application, accessible and responsive across both desktop and mobile browsers, providing a consistent experience on any device.

### 2.2 Desired Emotional Response

Users should feel calm and in control when using the application, which will result in them feeling motivated and efficient. The design should actively combat feelings of overwhelm and inability to act.

### 2.3 Inspiration Analysis

No specific applications were provided for inspiration. This presents a unique opportunity to create a novel and highly focused user experience, free from preconceived notions from existing apps. The primary inspiration is the user's current method of using simple notes, which highlights the need for a solution that is just as easy to use but far more intelligent and supportive.

### 2.4 Novel UX Patterns

**Pattern Name:** "Plan My Day" (Core Workflow)

**User Goal:** To transform a chaotic brain-dump of tasks into a manageable, optimized, and actionable plan for the day, with minimal effort.

**Trigger:** The user selects the primary "Plan My Day" action from the dashboard. This can be initiated from a blank slate, a saved template, or a photo of a list.

**Feedback:** The app provides a simple interface for the user to list all their tasks. Once they are done and press "Go," the app provides clear feedback that the AI is working (e.g., "Organizing your day..."). The view then transforms into the "Focused Task View," showing the first prioritized task.

**Success:** The result is a single, chronological, and manageable to-do list, presented one task at a time. The user has the ability to edit, reorder, or remove any AI-generated sub-steps, and the AI learns from these changes.

**Errors:** If the AI encounters a task it doesn't understand, it will place it in the list with a prompt for the user to clarify. It will not invent incorrect sub-steps, ensuring the user is never blocked. The rest of the list will be organized as expected.

#### 2.4.1 Deep Dive

*   **Speed & Feedback:** The AI processing should feel as fast as possible (target: <5 seconds). During this time, a simple, unobtrusive animation or a clear message (e.g., "Your tasks are now prioritized") will be displayed. The feedback should be "down-to-earth" and not waste the user's time.
*   **Delight:** Delight comes from the cleverness of the AI's output, not from sounds or flashy animations. The satisfying moment is seeing the well-organized list and discovering sub-tasks the user hadn't thought of.
*   **Platform Consistency:** The experience and functionality will be consistent across both desktop and mobile web platforms.
*   **Future Enhancement Idea (Shareability):** A powerful future enhancement would be the ability to invite other users to a collaborative list for shared planning (e.g., "planning a surprise party").

### 2.5 Core Experience Principles

*   **Speed:** Interactions will feel immediate and effortless. The AI-powered organization, while complex, will complete in under 5 seconds to maintain a sense of momentum and not feel like a roadblock.
*   **Guidance:** The application will provide gentle, intelligent guidance. It will proactively organize the user's day but always allow the user to override or edit the AI's suggestions. The goal is to be a helpful assistant, not a rigid commander.
*   **Flexibility:** The user has ultimate control. While the AI provides a strong default, the user must be able to easily edit, add, remove, and reorder tasks and sub-tasks. The app must be flexible enough to accommodate the user's changing plans.
*   **Feedback:** Feedback will be subtle, calm, and informative. It will confirm that an action has been taken without being distracting. No celebratory or loud notifications. The focus is on maintaining a calm and controlled environment.

### 2.6 Feature Enhancements

Based on our brainstorming session, the following features will be incorporated into the "Proactive Dashboard" design:

#### AI-Powered Assistance
*   **AI Task Optimization:** The AI will identify opportunities for efficiency. For example, if "Walk the dog" and "Take out the trash" are on the list, it might suggest doing them at the same time.
*   **AI Time Prediction:** The AI will provide an estimated time to complete for both individual tasks and the entire list.
*   **AI Habit Learning & Guided Routines:** Over time, the AI will learn the user's habits. This powers three key features:
    *   **AI Task Suggestion:** By recognizing patterns in the user's task input, the AI can proactively suggest common tasks or next logical steps (e.g., if "clean kitchen" is common, suggest "tidy up apartment").
    *   **Proactive Suggestions:** The dashboard will proactively suggest tasks or lists (e.g., "It's Tuesday, time for laundry?").
    *   **Guided Sessions:** A "Morning Briefing" will guide the user through the "Plan My Day" process, while an "Evening Review" will help them reflect on their accomplishments.
*   **Smart Sorting Options:** While the AI has a default sorting logic, the user can re-sort their list at any time based on:
    *   **Importance:** Deadlines, appointments, etc.
    *   **Duration:** Longest or shortest tasks first.
    *   **Energy Level:** High-focus vs. low-focus tasks.
    *   **Context:** Location-based tasks (e.g., "at home," "errands").

#### Smart Notifications & Nudges
*   **Time-Based Notifications:** The app understands tasks with a duration. If a task like "laundry" is running in the background, the app will send a gentle notification when the time is up, so the user doesn't forget the next step.
*   **Proactive Habit-Based Nudges:** The AI anticipates user needs based on their habits. For example, if the user swims every Monday, the app will send a reminder on Sunday to pack their swimwear.

#### Control and Customization
*   **Manual Sub-task Creation:** Users can always add their own sub-tasks to any item.
*   **Saved List Templates:** Users can save a list of tasks as a reusable template.
*   **Photo Attachments:** Users can attach photos to tasks for context or as a reminder.

#### Motivation and Progress
*   **Task Progress Visualization:** A "charging battery" visual for both the overall list and individual tasks provides a clear and satisfying visualization of progress.

#### Connectivity and Collaboration
*   **Calendar Integration:** Sync tasks with deadlines to an external calendar.
*   **Collaboration Suite:**
    *   **Share Lists:** Easily share any task list with other users.
    *   **Assign Tasks:** In a shared list, assign specific tasks to different people.
    *   **Invite Users:** A simple mechanism to invite friends or colleagues to the app.

---

## 3. Visual Foundation

### 3.1 Color System

**Chosen Theme:** Refined Focus (Working Direction)

This theme has been selected as the preliminary visual foundation. It is subject to refinement as the design progresses into mockups and prototypes.

*   **Palette:** The core of this theme is a professional, neutral grayscale foundation, which creates a calm, distraction-free environment. A muted, trustworthy blue is used as the primary action color to guide the user, while a reassuring green is reserved exclusively for success and completion feedback.
*   **Light/Dark Mode:** The application will support both Light and Dark modes to accommodate user preference and reduce eye strain.
*   **Typography:** The typography will be clean, simple, and highly readable, leveraging the default font system provided by the chosen design system (shadcn/ui) which is optimized for UI clarity.
*   **Spacing:** A consistent spacing system (based on a 4px or 8px grid) will be used to create a sense of order and rhythm, reducing visual clutter and enhancing the feeling of calm and control.

**Interactive Visualizations:**

- Color Theme Explorer: [ux-color-themes.html](./ux-color-themes.html)

---

## 4. Design Direction

### 4.1 Chosen Design Approach

### 4.1 Chosen Design Approach

**Design Direction: The Proactive Dashboard**

This design direction centers on a smart dashboard that acts as the user's command center, combined with a focused, single-task view to minimize overwhelm. It is designed to be proactive, guiding the user rather than waiting for them to act.

**1. The Dashboard (Main View):**
Upon opening the app, the user is greeted with a calm, clean dashboard featuring dynamic "widgets" that provide an at-a-glance overview of their day.
*   **Core Actions:** Prominent but minimal buttons for primary actions like **"Plan My Day"**, "View My Lists," and "Use a Template."
*   **Proactive AI Suggestions:** The dashboard will feature a section for proactive suggestions from the AI. For example: "It's Monday, time for your weekly review?" or "You have a quiet afternoon, want to tackle this task?".
*   **Dynamic Widgets:**
    *   **Today's Progress:** A "charging battery" visual showing the overall completion percentage for the day's tasks.
    *   **Next Calendar Event:** A small widget that syncs with the user's calendar to show their next appointment.
    *   **Shared With You:** An activity feed highlighting tasks recently assigned to the user on collaborative lists.

**2. "Plan My Day" (Core Workflow):**
This is the app's primary and default feature.
*   **Guided Input:** The user is guided to input all their tasks for the day in a simple, unstructured way. This can be from a blank list, a saved template, or even imported from a photo of a handwritten list.
*   **AI-Powered Sorting:** After the user is done, the AI automatically sorts the tasks, breaks them down into sub-tasks, adds time estimates, and presents a fully organized plan.
*   **Smart Sorting Options:** The AI uses a holistic default sorting logic, but the user can choose to re-sort the list by:
    *   **Importance:** (e.g., deadlines, appointments).
    *   **Duration:** Longest or shortest tasks first.
    *   **Energy Level:** Grouping high-focus and low-focus tasks.
    *   **Context:** Grouping tasks by location (e.g., "at home," "errands").

**3. The Focused Task View:**
After the plan is created, the app transitions to a focused view, showing only the single, most important task.
*   **One Task at a Time:** This view is designed to be minimal and calming, helping the user focus on what's next without the distraction of a long list.
*   **Gesture-Based Navigation:** The user can swipe the task away to mark it as complete and reveal the next one. They can also scroll down to see the full, de-emphasized list if needed.
*   **"Power-Up" Details:** This view also contains:
    *   The AI's **time estimate** for the task.
    *   The task-specific **"charging battery"** progress bar.
    *   Quick-access buttons to **"add sub-task"** or **"attach photo"**.

**4. Guided Routines:**
*   **"Morning Briefing":** A daily notification or dashboard state that guides the user through the "Plan My Day" process.
*   **"Evening Review":** A similar routine in the evening to help the user review their accomplishments and plan for the next day.

**Interactive Mockups:**

- Design Direction Showcase: [ux-design-directions.html](./ux-design-directions.html)

---

## 5. User Journey Flows

### 5.1 Critical User Paths

{{user_journey_flows}}

---

## 6. Component Library

### 6.1 Component Strategy

{{component_library_strategy}}

---

## 7. UX Pattern Decisions

### 7.1 Consistency Rules

{{ux_pattern_decisions}}

---

## 8. Responsive Design & Accessibility

### 8.1 Responsive Strategy

{{responsive_accessibility_strategy}}

---

## 9. Implementation Guidance

### 9.1 Completion Summary

{{completion_summary}}

---

## Appendix

### Related Documents

- Product Requirements: `{{prd_file}}`
- Product Brief: `{{brief_file}}`
- Brainstorming: `{{brainstorm_file}}`

### Core Interactive Deliverables

This UX Design Specification was created through visual collaboration:

- **Color Theme Visualizer**: docs/ux-color-themes.html
  - Interactive HTML showing all color theme options explored
  - Live UI component examples in each theme
  - Side-by-side comparison and semantic color usage

- **Design Direction Mockups**: docs/ux-design-directions.html
  - Interactive HTML with 6-8 complete design approaches
  - Full-screen mockups of key screens
  - Design philosophy and rationale for each direction

### Optional Enhancement Deliverables

_This section will be populated if additional UX artifacts are generated through follow-up workflows._

<!-- Additional deliverables added here by other workflows -->

### Next Steps & Follow-Up Workflows

This UX Design Specification can serve as input to:

- **Wireframe Generation Workflow** - Create detailed wireframes from user flows
- **Figma Design Workflow** - Generate Figma files via MCP integration
- **Interactive Prototype Workflow** - Build clickable HTML prototypes
- **Component Showcase Workflow** - Create interactive component library
- **AI Frontend Prompt Workflow** - Generate prompts for v0, Lovable, Bolt, etc.
- **Solution Architecture Workflow** - Define technical architecture with UX context

### Version History

| Date | Version | Changes | Author |
| -------- | ------- | ------------------------------- | ------ |
| 2025-11-26 | 1.0 | Initial UX Design Specification | Trine |

---

_This UX Design Specification was created through collaborative design facilitation, not template generation. All decisions were made with user input and are documented with rationale._
