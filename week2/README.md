# Action Item Extractor

A full-stack application that converts free-form notes into enumerated action item checklists. This project features a FastAPI backend, an SQLite database for storage, and a vanilla HTML/JS frontend. It supports both heuristic-based text extraction and advanced LLM-powered extraction using Ollama.

## Features
- **Create and Store Notes**: Save your raw notes into a local SQLite database.
- **Heuristic Extraction**: Quickly extract action items based on bullet points and keywords (`todo:`, `action:`).
- **LLM Extraction**: Use local LLMs (via Ollama) to intelligently parse complex text and extract actionable items.
- **Manage Action Items**: Mark action items as complete directly from the UI.

## Setup and Installation

1. **Activate the Environment**
   Make sure you have your Conda environment activated:
   ```bash
   conda activate cs146s
2. **Run Ollama (For LLM Extraction)**  
    Ensure Ollama is installed and running on your machine. Pull the required model:
    ```bash
    ollama pull llama3.1:8b
3. **Start the Backend Server**
    Start the FastAPI application using Uvicorn:
    ```bash
    poetry run uvicorn week2.app.main:app --reload
4. **Access the Application**
    Open your web browser and navigate to: http://127.0.0.1:8000/

**API Endpoints**
Notes
- POST /notes: Create a new note.
- GET /notes: Retrieve all saved notes.
- GET /notes/{note_id}: Retrieve a specific note by ID.

**Action Items**
- GET /action-items: List all action items (can be filtered by note_id).
- POST /action-items/extract: Extract action items using heuristic rules.
- POST /action-items/extract-llm: Extract action items using the Ollama LLM.
- POST /action-items/{id}/done: Mark a specific action item as done or undone.

5. **Running Tests**
    The project includes a comprehensive test suite written in pytest. To run the tests, execute the following command in your terminal:
    ```bash
    poetry run pytest week2/tests/ -v