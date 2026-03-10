"""Pydantic schemas for API request and response validation."""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field, field_validator


# --- Note schemas ---


class NoteCreate(BaseModel):
    """Request body for creating a note."""

    content: str = Field(..., min_length=1, description="Note content")

    @field_validator("content", mode="before")
    @classmethod
    def strip_content(cls, v: str) -> str:
        return str(v).strip() if v is not None else ""


class NoteResponse(BaseModel):
    """Response schema for a single note."""

    id: int
    content: str
    created_at: str

    model_config = {"from_attributes": True}


# --- Action item extract schemas ---


class ActionItemExtractRequest(BaseModel):
    """Request body for extracting action items from text."""

    text: str = Field(..., min_length=1, description="Text to extract action items from")
    save_note: bool = Field(default=False, description="Whether to save the text as a note")

    @field_validator("text", mode="before")
    @classmethod
    def strip_text(cls, v: str) -> str:
        return str(v).strip() if v is not None else ""


class ActionItemExtractItem(BaseModel):
    """Single extracted action item (id + text)."""

    id: int
    text: str


class ActionItemExtractResponse(BaseModel):
    """Response schema for action item extraction."""

    note_id: Optional[int] = None
    items: list[ActionItemExtractItem]


# --- Action item list schemas ---


class ActionItemResponse(BaseModel):
    """Response schema for a single action item."""

    id: int
    note_id: Optional[int] = None
    text: str
    done: bool
    created_at: str

    model_config = {"from_attributes": True}


# --- Mark done schemas ---


class MarkDoneRequest(BaseModel):
    """Request body for marking an action item as done."""

    done: bool = Field(default=True, description="Whether the item is done")


class MarkDoneResponse(BaseModel):
    """Response schema for mark done operation."""

    id: int
    done: bool
