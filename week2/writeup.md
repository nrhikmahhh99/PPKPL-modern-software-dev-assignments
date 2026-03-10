# Week 2 Write-up
Tip: To preview this markdown file
- On Mac, press `Command (⌘) + Shift + V`
- On Windows/Linux, press `Ctrl + Shift + V`

## INSTRUCTIONS

Fill out all of the `TODO`s in this file.

## SUBMISSION DETAILS

Name: Nur Hikmah \
SUNet ID: 2310817120010 \
Citations: **TODO**

This assignment took me about **TODO** hours to do. 


## YOUR RESPONSES
For each exercise, please include what prompts you used to generate the answer, in addition to the location of the generated response. Make sure to clearly add comments in your code documenting which parts are generated.

### Exercise 1: Scaffold a New Feature
Prompt: 
```
I need to implement TODO 1. Please add a new function called extract_action_items_llm(text: str) -> list[str] in this file. This function should use the ollama python package to send the text to an LLM (use 'llama3.1:8b'). The prompt to the LLM should instruct it to extract a list of actionable items from the text and return ONLY a JSON array of strings. Parse the LLM response using the json module and return the python list. Include basic error handling for JSON decoding.
```

Generated Code Snippets:
```
`week2/app/services/extract.py`: Lines 21 - 56
```

### Exercise 2: Add Unit Tests
Prompt:
``` 
I need to implement TODO 2. Please write unit tests for the extract_action_items_llm() function that I just added in week2/app/services/extract.py. The tests should cover multiple inputs (e.g., bullet lists, keyword-prefixed lines, empty input). Since this uses an LLM, please use unittest.mock.patch to mock the ollama.chat call so the tests run quickly without needing the actual LLM 
```

Generated Code Snippets:
```
`week2/tests/test_extract.py`: Lines 3, 5, 22 - 116
```

### Exercise 3: Refactor Existing Code for Clarity
Prompt: 
```
I need to implement TODO 3: Refactor Existing Code for Clarity. Please refactor the backend code inside the week2/app/ folder. Do the following:
Create a new file week2/app/schemas.py and define strict Pydantic models for all API requests and responses (e.g., NoteCreate, NoteResponse, ActionItemExtractRequest, ActionItemResponse).
Update the routers (week2/app/routers/notes.py and week2/app/routers/action_items.py) to use these Pydantic schemas instead of Dict[str, Any]. Ensure proper HTTP error handling is in place (raising HTTPException).
Clean up week2/app/db.py to make the database layer more robust, add proper type hinting, and ensure connections are handled neatly.
Review week2/app/main.py for app lifecycle and configuration, ensuring routers are included cleanly.
``` 

Generated/Modified Code Snippets:
```
- `week2/app/schemas.py`: File baru dibuat, berisi Pydantic models
- `week2/app/routers/notes.py`: Dimodifikasi untuk menggunakan schemas dan HTTP exceptions
- `week2/app/routers/action_items.py`: Dimodifikasi untuk menggunakan schemas dan HTTP exceptions
- `week2/app/db.py`: Dimodifikasi dengan context manager untuk koneksi DB
- `week2/app/main.py`: Dimodifikasi app lifecycle startup event
```


### Exercise 4: Use Agentic Mode to Automate a Small Task
Prompt: 
```
I need to implement TODO 4: Use Agentic Mode to Automate Small Tasks. Please do the following fullstack changes:
In the backend, expose a new endpoint to retrieve all notes (e.g., GET /notes in week2/app/routers/notes.py). Update schemas.py and db.py if necessary to support fetching all notes.
In the backend, integrate the LLM-powered extraction as a new endpoint (e.g., POST /action-items/extract-llm in week2/app/routers/action_items.py) that uses the extract_action_items_llm function. Update schemas.py if needed.
In the frontend (week2/frontend/index.html and week2/frontend/app.js), add a 'List Notes' button that fetches and displays all notes.
In the frontend, add an 'Extract LLM' button next to the regular extract button that triggers the new /extract-llm endpoint.
``` 

Generated Code Snippets:
```
- `week2/app/routers/notes.py`: Added `list_notes` endpoint.
- `week2/app/routers/action_items.py`: Added `extract_llm` endpoint.
- `week2/frontend/index.html`: Added new buttons and display areas for LLM Extract and List Notes.
- `week2/frontend/app.js`: Added javascript fetch logic to call the new endpoints.
```


### Exercise 5: Generate a README from the Codebase
Prompt: 
```
Please analyze the current codebase and generate a well-structured `README.md` file. It should include: a brief overview of the project, setup and run instructions, API endpoints available, and instructions for running the test suite with pytest.
``` 

Generated Code Snippets:
```
`week2/README.md`: Created a new file containing the generated documentation, including overview, setup, API routes, and testing instructions.
```


## SUBMISSION INSTRUCTIONS
1. Hit a `Command (⌘) + F` (or `Ctrl + F`) to find any remaining `TODO`s in this file. If no results are found, congratulations – you've completed all required fields. 
2. Make sure you have all changes pushed to your remote repository for grading.
3. Submit via Gradescope. 