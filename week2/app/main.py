"""Action Item Extractor - FastAPI application entry point."""

from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from .db import init_db
from .routers import action_items, notes

# Paths relative to this file (week2/app/)
APP_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = APP_DIR.parent / "frontend"

app = FastAPI(title="Action Item Extractor")


@app.on_event("startup")
def on_startup() -> None:
    """Initialize database on application startup."""
    init_db()


@app.get("/", response_class=HTMLResponse)
def index() -> str:
    """Serve the main HTML page."""
    html_path = FRONTEND_DIR / "index.html"
    return html_path.read_text(encoding="utf-8")


# Include API routers
app.include_router(notes.router)
app.include_router(action_items.router)

# Mount static files (CSS, JS)
app.mount("/static", StaticFiles(directory=str(FRONTEND_DIR)), name="static")