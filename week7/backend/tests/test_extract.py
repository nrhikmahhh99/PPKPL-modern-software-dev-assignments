from backend.app.services.extract import extract_action_items


def test_extract_action_items():
    text = """
    This is a note
    - TODO: write tests
    - ACTION: review PR
    - Ship it!
    Not actionable
    """
    items = extract_action_items(text)
    descriptions = [item.description for item in items]
    assert "TODO: write tests" in descriptions
    assert "ACTION: review PR" in descriptions
    assert "Ship it!" in descriptions


def test_extract_with_due_date():
    text = "- Deploy to prod due: 2024-12-31"
    items = extract_action_items(text)
    assert len(items) == 1
    assert items[0].description == "Deploy to prod"
    assert items[0].due_date == "2024-12-31"


def test_extract_with_assignee():
    text = "- Fix login bug assignee: @jane"
    items = extract_action_items(text)
    assert len(items) == 1
    assert "Fix login bug" in items[0].description
    assert items[0].assignee == "jane"


def test_extract_bullet_list():
    text = """
    * First task
    - Second task
    1. Third task
    """
    items = extract_action_items(text)
    assert len(items) >= 3
    descriptions = [item.description for item in items]
    assert "First task" in descriptions
    assert "Second task" in descriptions


