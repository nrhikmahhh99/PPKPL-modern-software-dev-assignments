# Week 6 Write-up

Tip: To preview this markdown file

- On Mac, press `Command (⌘) + Shift + V`
- On Windows/Linux, press `Ctrl + Shift + V`

## Instructions

Fill out all of the `TODO`s in this file.

## Submission Details

Name: **Nur Hikmah** \
SUNet ID: **2310817120010** \
Citations: **Digunakan AI prompt (Gemini) untuk penjelasan mitigasi dan perbaikan kode.**

This assignment took me about **TODO** hours to do.

## Brief findings overview

> Semgrep reported several vulnerabilities categorized primarily under SAST (Static Application Security Testing). The findings included web security risks such as overly permissive CORS (Wildcard CORS), database vulnerabilities like SQL Injection via raw SQL evaluation (`sqlalchemy.text`), frontend Cross-Site Scripting (XSS) risks due to unsafe DOM writes (`innerHTML`), as well as command injection and dynamic evaluation risks (`eval()`, `subprocess.run(shell=True)`). I chose to ignore the remaining `eval` and `subprocess` warnings because the assignment only required 3 fixes, and those debug endpoints are likely intended for local testing purposes.

## Fix #1

a. File and line(s)

> `week6/backend/app/main.py` (Line 24)

b. Rule/category Semgrep flagged

> `python.fastapi.security.wildcard-cors.wildcard-cors`

c. Brief risk description

> The CORS policy allows any origin (`*`) to access the API. This is highly insecure because malicious websites could make cross-origin requests and steal sensitive data from users authenticated on this application.

d. Your change (short code diff or explanation, AI coding tool usage)

> Changed `allow_origins=["*"]` to explicitly allow only trusted origins.
> Before: `allow_origins=["*"],`
> After: `allow_origins=["http://localhost:8000", "http://127.0.0.1:8000"],`
> _(Guided by AI to specify localized secure origins)._

e. Why this mitigates the issue

> By specifying exact trusted domains (like localhost), we enforce the Same-Origin Policy. Browsers will now block unauthorized domains from interacting with the API, effectively preventing cross-origin data theft.

## Fix #2

a. File and line(s)

> `week6/backend/app/routers/notes.py` (Line 71-79)

b. Rule/category Semgrep flagged

> `python.sqlalchemy.security.audit.avoid-sqlalchemy-text.avoid-sqlalchemy-text`

c. Brief risk description

> The code used Python's f-string to dynamically insert user input (`q`) directly into a SQL query. This is a classic SQL Injection vulnerability that allows attackers to manipulate the query structure, potentially extracting or destroying database records.

d. Your change (short code diff or explanation, AI coding tool usage)

> Replaced the f-string formatting with parameterized query binding.
> Before: `WHERE title LIKE '%{q}%' OR content LIKE '%{q}%'` and `db.execute(sql).all()`
> After: `WHERE title LIKE :q OR content LIKE :q` and `db.execute(sql, {"q": f"%{q}%"}).all()`
> _(Guided by AI to implement safe bindings)._

e. Why this mitigates the issue

> Parameterized queries separate the SQL code from the user-provided data. The database engine treats the input strictly as a string literal (data) rather than executable SQL commands, making SQL injection impossible.

## Fix #3

a. File and line(s)

> `week6/frontend/app.js` (Line 14)

b. Rule/category Semgrep flagged

> `javascript.browser.security.insecure-document-method.insecure-document-method`

c. Brief risk description

> Writing user-controlled data directly into the DOM using `innerHTML` is an anti-pattern. If a user inputs malicious JavaScript code into the note's title or content, the browser will execute it, leading to a Cross-Site Scripting (XSS) attack.

d. Your change (short code diff or explanation, AI coding tool usage)

> Replaced `innerHTML` with `textContent` to safely render DOM elements.
> Before: `li.innerHTML = \`<strong>${n.title}</strong>: ${n.content}\`;`
> After:

```javascript
const strong = document.createElement('strong');
strong.textContent = n.title;
li.appendChild(strong);
li.appendChild(document.createTextNode(`: ${n.content}`));

e. Why this mitigates the issue
> Using textContent (and createTextNode) forces the browser to treat the input purely as plain text. Any HTML tags or script elements injected by the user will be rendered as literal characters on the screen, completely neutralizing the XSS vector.
```
