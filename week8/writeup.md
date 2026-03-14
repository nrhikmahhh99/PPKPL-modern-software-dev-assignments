# Week 8 Write-up
Tip: To preview this markdown file
- On Mac, press `Command (⌘) + Shift + V`
- On Windows/Linux, press `Ctrl + Shift + V`

## Instructions

Fill out all of the `TODO`s in this file.

## Submission Details

Name: **Nur Hikmah** \
SUNet ID: **2310817120010** \
Citations: **Google AI Studio (Gemini 1.5 Flash), React Docs, Node.js Docs, Tailwind CSS Docs**

This assignment took me about **5-7** hours to do. 


## App Concept 
```
Build a full-stack Task Management application for my software development assignment.
Features: > 1. User can create, read, update, and delete tasks (CRUD).
2. Each task should have a title, description, and status (todo, in progress, done).
Tech Stack: > Use React for frontend and Node.js/Express for backend.
Persistence: > For the database, use a simple local JSON file storage or SQLite so it's easy to run locally without complex setup.
UI/UX: > Make the UI clean and modern using Tailwind CSS. Include basic validation for the task title (cannot be empty)
```


## Version #1 Description
```
APP DETAILS:
===============
Folder name: versi1-aistudio
AI app generation platform: Google AI Studio (Gemini 1.5 Flash)
Tech Stack: React (Frontend) and Node.js/Express (Backend)
Persistence: SQLite Database (local tasks.db file)
Frameworks/Libraries Used: React, Vite, Tailwind CSS (v3), Axios, Express, SQLite3, CORS
(Optional but recommended) Screenshots of core flows: TODO

REFLECTIONS:
===============
a. Issues encountered per stack and how you resolved them: 
- Encountered a persistent 'Server Error: Invalid model selected / AI_APICallError' when trying to use the Bolt.diy platform locally. I resolved this by bypassing the local tool and using the Gemini 1.5 Flash model directly via the Google AI Studio interface.
- Encountered a package version mismatch where 'npx tailwindcss init -p' failed because npm installed Tailwind v4 by default, which conflicted with the generated code structure. Resolved by explicitly installing Tailwind v3 ('npm install -D tailwindcss@3').

b. Prompting (e.g. what required additional guidance; what worked poorly/wel): Prompting for a complete full-stack app in one go worked surprisingly well when I clearly separated the requirements into Features, Tech Stack, Persistence, and UI/UX. Specifying SQLite for the database was a good move as it required zero manual configuration compared to setting up a MongoDB or PostgreSQL instance.

c. Approximate time-to-first-run and time-to-feature metrics: 
- Time-to-first-run: ~50 minutes (mostly spent troubleshooting the Bolt.diy connection errors).
- Time-to-feature: ~15 minutes (after switching to Google AI Studio, the code generation and folder setup were very rapid).
```

## Version #2 Description
```
APP DETAILS:
===============
Folder name: versi2-flask
AI app generation platform: Manual prompt generation via Gemini (No specific app generation platform used for this version)
Tech Stack: Python / Flask (Backend), HTML + Vanilla JavaScript + Tailwind CSS via CDN (Frontend)
Persistence: SQLite Database (local tasks.db file)
Frameworks/Libraries Used: Flask, SQLite3 (Python built-in)
(Optional but recommended) Screenshots of core flows: TODO

REFLECTIONS:
===============
a. Issues encountered per stack and how you resolved them:
- For this version, the challenge was ensuring the UI/UX remained consistent (a Kanban Board) with Version 1 without using React. I resolved this by utilizing Tailwind CSS via CDN directly in the HTML file and writing vanilla JavaScript functions (using Fetch API) to manipulate the DOM and handle the status updates.
- Ensured there were no port conflicts with Version 1 by setting the Flask server to explicitly run on port 5001 instead of the default port 5000.

b. Prompting (e.g. what required additional guidance; what worked poorly/wel): Generating the Python/Flask backend was very straightforward. The AI understood the requirement to use a non-JavaScript language perfectly. I had to provide additional guidance to the AI to update the initial simple list UI into a full 3-column Kanban board to maintain feature parity (CRUD with status updates) across the different application versions.

c. Approximate time-to-first-run and time-to-feature metrics: 
- Time-to-first-run: ~15 minutes. It was very fast because I was able to reuse an existing Anaconda environment ('cs146s') that already had most Python dependencies installed.
- Time-to-feature: ~20 minutes. The additional time was spent refining the HTML template to support the 'Update' functionality via a dropdown menu for the task statuses.
```

## Version #3 Description
```
APP DETAILS:
===============
Folder name: versi3-php
AI app generation platform: Manual prompt generation via Gemini (No specific app generation platform used)
Tech Stack: Vanilla PHP (Backend), HTML + Vanilla JavaScript + Tailwind CSS via CDN (Frontend)
Persistence: File-based storage (tasks.json)
Frameworks/Libraries Used: None for backend (Vanilla PHP). Tailwind CSS (via CDN) for frontend styling.
(Optional but recommended) Screenshots of core flows: TODO

REFLECTIONS:
===============
a. Issues encountered per stack and how you resolved them:
- Using a file-based JSON approach for the database in PHP meant I had to ensure the file was created automatically if it didn't exist to prevent read/write errors. I resolved this by adding a simple file_exists check in the PHP script that initializes an empty array if the file is missing.
- Keeping the UI strictly identical to Version 2 was very easy since I could reuse the HTML and Vanilla JS structure, only needing to change the API endpoint in the fetch requests from the Flask route to api.php.

b. Prompting (e.g. what required additional guidance; what worked poorly/wel): Prompting for Vanilla PHP with JSON storage was extremely effective and produced working code on the first try. The AI understood the instruction to avoid complex frameworks and provided a clean, single-file API solution.

c. Approximate time-to-first-run and time-to-feature metrics: 
- Time-to-first-run: ~5-7 minutes. It was incredibly fast because there were no environments to set up and no packages to install via npm or pip.
- Time-to-feature: ~10 minutes. The only time spent was merging the PHP backend logic with the Kanban Board frontend template created in Version 2.
```
