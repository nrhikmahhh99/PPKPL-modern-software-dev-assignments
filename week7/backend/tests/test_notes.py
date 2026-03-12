def test_create_list_and_patch_notes(client):
    payload = {"title": "Test", "content": "Hello world"}
    r = client.post("/notes/", json=payload)
    assert r.status_code == 201, r.text
    data = r.json()
    assert data["title"] == "Test"
    assert "created_at" in data and "updated_at" in data

    r = client.get("/notes/")
    assert r.status_code == 200
    items = r.json()
    assert len(items) >= 1

    r = client.get("/notes/", params={"q": "Hello", "limit": 10, "sort": "-created_at"})
    assert r.status_code == 200
    items = r.json()
    assert len(items) >= 1

    note_id = data["id"]
    r = client.patch(f"/notes/{note_id}", json={"title": "Updated"})
    assert r.status_code == 200
    patched = r.json()
    assert patched["title"] == "Updated"


def test_notes_pagination_limit(client):
    """GET /notes returns at most 'limit' items."""
    for i in range(5):
        client.post("/notes/", json={"title": f"Note {i}", "content": f"Content {i}"})

    r = client.get("/notes/", params={"limit": 2})
    assert r.status_code == 200
    items = r.json()
    assert len(items) == 2, f"Expected exactly 2 items, got {len(items)}"

    r = client.get("/notes/", params={"limit": 3})
    assert r.status_code == 200
    items = r.json()
    assert len(items) == 3, f"Expected exactly 3 items, got {len(items)}"


def test_notes_pagination_skip(client):
    """GET /notes with skip returns items offset by skip."""
    for i in range(5):
        client.post("/notes/", json={"title": f"Note {i}", "content": f"Content {i}"})

    r_all = client.get("/notes/", params={"limit": 10, "sort": "id"})
    assert r_all.status_code == 200
    all_items = r_all.json()
    all_ids = [n["id"] for n in all_items]
    assert len(all_ids) >= 5

    r_first = client.get("/notes/", params={"skip": 0, "limit": 2, "sort": "id"})
    r_second = client.get("/notes/", params={"skip": 2, "limit": 2, "sort": "id"})
    assert r_first.status_code == 200
    assert r_second.status_code == 200

    first_page = r_first.json()
    second_page = r_second.json()
    assert len(first_page) == 2
    assert len(second_page) == 2

    first_ids = [n["id"] for n in first_page]
    second_ids = [n["id"] for n in second_page]
    assert first_ids != second_ids, "Skip should return different items"
    assert set(first_ids) & set(second_ids) == set(), "Pages should not overlap"


def test_notes_sorting_desc(client):
    """GET /notes with sort=-field returns descending order."""
    client.post("/notes/", json={"title": "Alpha", "content": "A"})
    client.post("/notes/", json={"title": "Beta", "content": "B"})
    client.post("/notes/", json={"title": "Gamma", "content": "C"})

    r = client.get("/notes/", params={"limit": 10, "sort": "-title"})
    assert r.status_code == 200
    items = r.json()
    titles = [n["title"] for n in items]
    assert titles == sorted(titles, reverse=True), f"Expected desc by title, got {titles}"


def test_notes_sorting_asc(client):
    """GET /notes with sort=field (no minus) returns ascending order."""
    client.post("/notes/", json={"title": "Zebra", "content": "Z"})
    client.post("/notes/", json={"title": "Apple", "content": "A"})
    client.post("/notes/", json={"title": "Mango", "content": "M"})

    r = client.get("/notes/", params={"limit": 10, "sort": "title"})
    assert r.status_code == 200
    items = r.json()
    titles = [n["title"] for n in items]
    assert titles == sorted(titles), f"Expected asc by title, got {titles}"


