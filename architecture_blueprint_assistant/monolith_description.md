# Monolithic Architecture – CodeQuest

This monolithic architecture centralizes all business logic into a single codebase and deployment unit. While this approach simplifies cross-module communication, it creates tight coupling between the components.

## Components & Responsibilities
- **Web & Mobile Frontend**: The primary interface for users to interact with quests, write code, and view rankings.
- **Auth & Session Module**: Manages secure access, verifying identity before any other module is engaged.
- **Gamification Engine**: The core logic for tracking user progress, distributing rewards (XP/Gems), and maintaining streaks.
- **AI Adaptive Learning Path**: Evaluates user performance history to dynamically update the difficulty of the next curriculum task.
- **Code Execution Sandbox**: A secure environment that executes user code and sends pass/fail signals to the gamification engine.
- **Curriculum Manager**: Acts as the content repository, delivering tasks and projects to the user via the Sandbox.
- **Peer Review System**: Allows users to validate each other's code, triggering rewards in the Gamification Engine upon successful review.
- **Battle Arena Module**: Facilitates real-time logic competitions, updating scores directly in the central database.
- **Central Database**: A shared Relational Database (PostgreSQL) where all modules store and retrieve persistent data.

## System Interactions
- **Authentication Flow**: Users must be verified by the **Auth Module** before the **Curriculum Manager** serves any content.
- **Learning Cycle**: The **AI Path** analyzes data in the **DB**, then tells the **Curriculum Manager** which task to provide.
- **Execution & Reward**: When a user runs code in the **Sandbox**, the result is sent to the **Gamification Engine** to update XP and Streaks in the **DB**.
- **Social Loop**: Completed tasks in the **Review System** or **Battle Arena** notify the **Gamification Engine** to adjust user levels and leaderboard standings.
