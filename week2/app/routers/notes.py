from __future__ import annotations

from fastapi import APIRouter, HTTPException

from .. import db
from ..schemas import NoteCreate, NoteResponse

router = APIRouter(prefix="/notes", tags=["notes"])

# Endpoint GET /notes - fetch all notes, newest first
@router.get("", response_model=list[NoteResponse])
def list_notes() -> list[NoteResponse]:
    """Get all notes, newest first."""
    rows = db.list_notes()
    return [
        NoteResponse(id=row["id"], content=row["content"], created_at=row["created_at"])
        for row in rows
    ]

# Endpoint POST /notes - create a new note
@router.post("", response_model=NoteResponse)
def create_note(payload: NoteCreate) -> NoteResponse:
    note_id = db.insert_note(payload.content)
    note = db.get_note(note_id)
    if note is None:
        raise HTTPException(status_code=500, detail="failed to retrieve created note")
    return NoteResponse(
        id=note["id"],
        content=note["content"],
        created_at=note["created_at"],
    )

# Endpoint GET /notes/{note_id} - get a single note by ID
@router.get("/{note_id}", response_model=NoteResponse)
def get_single_note(note_id: int) -> NoteResponse:
    row = db.get_note(note_id)
    if row is None:
        raise HTTPException(status_code=404, detail="note not found")
    return NoteResponse(
        id=row["id"],
        content=row["content"],
        created_at=row["created_at"],
    )
