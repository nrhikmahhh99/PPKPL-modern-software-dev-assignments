# Version 3: Task Management App (Vanilla PHP + JSON + HTML)

## Overview
This version explores a lightweight, framework-less approach. It uses Vanilla PHP for the backend API and stores data in a simple local JSON file. The frontend uses plain HTML, Vanilla JavaScript (Fetch API), and Tailwind CSS via CDN to maintain a consistent UI across all versions.

## Prerequisites
- PHP (v7.4 or higher recommended)

## Installation & Setup
1. **Navigate to the project directory:**
   ```bash
   cd week8/versi3-php
2. **No additional installation (like npm or pip) is required since this relies entirely on Vanilla PHP and a CDN for styling.**

## How to Run
1. **Start the PHP built-in server by running the following command in your terminal:**
   ```bash
   php -S localhost:8002
2. **The server will start on http://localhost:8002.**
3. **Open your web browser and navigate to the local URL.**
4. **The application will automatically create a tasks.json file in the root directory to store your tasks persistently upon your first action.**