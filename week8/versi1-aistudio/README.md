# Version 1: Task Management App (React + Node.js + SQLite)

## Note on Deviation
As permitted by the assignment guidelines, this version was generated using **Google AI Studio (Gemini 1.5 Flash)** instead of `bolt.new`. I initially attempted to use `bolt.diy` (the open-source local alternative to `bolt.new`) but encountered persistent API/Model connection errors (`AI_APICallError: models/gemini-1.5-flash is not found for API version v1beta`). To ensure timely completion and a fully functional app, I directly utilized the same underlying AI model via Google AI Studio.

## Prerequisites
- Node.js (v18 or higher recommended)
- npm (Node Package Manager)

## Installation & Setup

1. **Clone/Download the repository** and navigate to this folder (`versi1-aistudio`).
2. **Setup Backend:**
   - Open a terminal and navigate to the `backend` folder: `cd backend`
   - Install dependencies: `npm install`
3. **Setup Frontend:**
   - Open a new terminal and navigate to the `frontend` folder: `cd frontend`
   - Install dependencies: `npm install`

## How to Run

You need to run both the backend and frontend simultaneously in separate terminals.

**1. Start the Backend Server**
- In the `backend` terminal, run:
  ```bash
  node server.js
- The server will start on http://localhost:5000 and automatically create the SQLite database file (tasks.db).
**2. Start the Frontend**
- In the frontend terminal, run:
    ```bash
    npm run dev
- Open your browser and navigate to the local URL provided (usually http://localhost:5173/).