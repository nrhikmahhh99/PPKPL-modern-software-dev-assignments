import os
import pytest
from unittest.mock import MagicMock, patch

from ..app.services.extract import extract_action_items, extract_action_items_llm


def test_extract_bullets_and_checkboxes():
    text = """
    Notes from meeting:
    - [ ] Set up database
    * implement API extract endpoint
    1. Write tests
    Some narrative sentence.
    """.strip()

    items = extract_action_items(text)
    assert "Set up database" in items
    assert "implement API extract endpoint" in items
    assert "Write tests" in items


# --- Tests for extract_action_items_llm (mocked to avoid LLM calls) ---


@patch("week2.app.services.extract.chat")
def test_extract_action_items_llm_empty_input(mock_chat):
    """Empty input returns [] without calling the LLM."""
    result = extract_action_items_llm("")
    assert result == []
    mock_chat.assert_not_called()


@patch("week2.app.services.extract.chat")
def test_extract_action_items_llm_whitespace_only(mock_chat):
    """Whitespace-only input returns [] without calling the LLM."""
    result = extract_action_items_llm("   \n\t  ")
    assert result == []
    mock_chat.assert_not_called()


@patch("week2.app.services.extract.chat")
def test_extract_action_items_llm_bullet_list(mock_chat):
    """Bullet list input is extracted as action items."""
    mock_response = MagicMock()
    mock_response.message.content = '["Set up database", "implement API endpoint", "Write tests"]'
    mock_chat.return_value = mock_response

    text = """
    - Set up database
    * implement API endpoint
    1. Write tests
    """
    result = extract_action_items_llm(text)

    assert result == ["Set up database", "implement API endpoint", "Write tests"]
    mock_chat.assert_called_once()
    assert mock_chat.call_args.kwargs.get("model") == "llama3.1:8b"


@patch("week2.app.services.extract.chat")
def test_extract_action_items_llm_keyword_prefixed(mock_chat):
    """Keyword-prefixed lines (todo:, action:, next:) are extracted."""
    mock_response = MagicMock()
    mock_response.message.content = '["Review pull request", "Update documentation", "Schedule follow-up"]'
    mock_chat.return_value = mock_response

    text = """
    todo: Review pull request
    action: Update documentation
    next: Schedule follow-up
    """
    result = extract_action_items_llm(text)

    assert result == ["Review pull request", "Update documentation", "Schedule follow-up"]
    mock_chat.assert_called_once()


@patch("week2.app.services.extract.chat")
def test_extract_action_items_llm_markdown_code_block(mock_chat):
    """Response wrapped in markdown code block is parsed correctly."""
    mock_response = MagicMock()
    mock_response.message.content = '```json\n["Fix bug", "Add feature"]\n```'
    mock_chat.return_value = mock_response

    result = extract_action_items_llm("Fix bug. Add feature.")

    assert result == ["Fix bug", "Add feature"]
    mock_chat.assert_called_once()


@patch("week2.app.services.extract.chat")
def test_extract_action_items_llm_invalid_json_returns_empty(mock_chat):
    """Invalid JSON response returns empty list."""
    mock_response = MagicMock()
    mock_response.message.content = "This is not valid JSON at all"
    mock_chat.return_value = mock_response

    result = extract_action_items_llm("Some notes here")

    assert result == []
    mock_chat.assert_called_once()


@patch("week2.app.services.extract.chat")
def test_extract_action_items_llm_non_list_json_returns_empty(mock_chat):
    """Non-list JSON response returns empty list."""
    mock_response = MagicMock()
    mock_response.message.content = '{"items": ["a", "b"]}'
    mock_chat.return_value = mock_response

    result = extract_action_items_llm("Some notes")

    assert result == []
    mock_chat.assert_called_once()
