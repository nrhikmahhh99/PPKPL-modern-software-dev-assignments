# Week 7 Write-up
Tip: To preview this markdown file
- On Mac, press `Command (⌘) + Shift + V`
- On Windows/Linux, press `Ctrl + Shift + V`

## Instructions

Fill out all of the `TODO`s in this file.

## Submission Details

Name: **Nur Hikmah** \
SUNet ID: **2310817120010** \
Citations: **Cursor AI, Graphite Diamond, ChatGPT/Gemini (untuk panduan langkah-langkah).**

This assignment took me about **3** hours to do. 


## Task 1: Add more endpoints and validations
a. Links to relevant commits/issues
> https://github.com/nrhikmahhh99/PPKPL-modern-software-dev-assignments/pull/6

b. PR Description
> Added new DELETE endpoints for notes and action-items, and GET by ID for action-items. Implemented input validation using Pydantic (e.g., min_length, whitespace stripping) and added path validation ensuring ID > 0. Added proper 404 HTTP Exceptions for items not found.

c. Graphite Diamond generated code review
> No issues found! The AI reviewer confirmed the endpoints and validations were implemented securely and correctly.

## Task 2: Extend extraction logic
a. Links to relevant commits/issues
> https://github.com/nrhikmahhh99/PPKPL-modern-software-dev-assignments/pull/5

b. PR Description
> Enhanced the action item extraction functionality in `extract.py`. Improved pattern recognition to detect due dates and assignees more accurately using refined regex and logic. Added 3 new test cases in `test_extract.py` to validate the new extraction rules.

c. Graphite Diamond generated code review
> No issues found! The AI reviewer confirmed the extend extraction logic was implemented securely and correctly.

## Task 3: Try adding a new model and relationships
a. Links to relevant commits/issues
> https://github.com/nrhikmahhh99/PPKPL-modern-software-dev-assignments/pull/4

b. PR Description
> Created a new `Tag` model in `models.py` with a relationship to the existing `Note` model. Added corresponding Pydantic schemas, and created a new router (`tags.py`) with full CRUD operations. Wrote 8 new test cases in `test_tags.py` to ensure the model and relationships work seamlessly.

c. Graphite Diamond generated code review
> No issues found! (The AI successfully reviewed the new models and relationships without finding any bugs).

## Task 4: Improve tests for pagination and sorting
a. Links to relevant commits/issues
> https://github.com/nrhikmahhh99/PPKPL-modern-software-dev-assignments/pull/3

b. PR Description
> Improved test coverage specifically targeting the pagination (limit, offset) and sorting functionality for the GET endpoints. Added 8 new comprehensive test scenarios in `test_notes.py` and `test_action_items.py` to validate data ordering and limits.

c. Graphite Diamond generated code review
> Graphite found no issues

## Brief Reflection 
a. The types of comments you typically made in your manual reviews (e.g., correctness, performance, security, naming, test gaps, API shape, UX, docs).
> In my manual reviews, I typically focused on correctness (whether the code successfully met the assignment requirements), API shape (ensuring the new endpoints followed RESTful conventions), and test gaps (verifying if edge cases were handled, like querying a non-existent ID). 

b. A comparison of **your** comments vs. **Graphite’s** AI-generated comments for each PR.
> My comments were mostly high-level, checking the "big picture" of the business logic. Graphite’s AI, on the other hand, was much faster and extremely precise in analyzing syntax, potential performance bottlenecks, and strict adherence to best practices without having to manually run the code in my head.

c. When the AI reviews were better/worse than yours (cite specific examples)
> The AI review was **better** at quickly scanning for security and validation flaws (like ensuring `Path(gt=0)` was used in Task 1). It acts as an excellent automated linter. However, it was **worse** (or less helpful) when it came to understanding the broader context of the assignment. Sometimes AI can be too nitpicky about stylistic choices that don't actually break the application.

d. Your comfort level trusting AI reviews going forward and any heuristics for when to rely on them.
>I feel very comfortable trusting AI reviews as a "first line of defense" to catch syntax errors, missing validations, and standard code-quality issues. My heuristic going forward is: rely completely on AI for catching technical bugs, typos, and performance issues, but rely on human manual review for architectural decisions, complex business logic, and overall system design. 



