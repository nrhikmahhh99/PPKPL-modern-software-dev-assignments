def test_create_complete_list_and_patch_action_item(client):
    payload = {"description": "Ship it"}
    r = client.post("/action-items/", json=payload)
    assert r.status_code == 201, r.text
    item = r.json()
    assert item["completed"] is False
    assert "created_at" in item and "updated_at" in item

    r = client.put(f"/action-items/{item['id']}/complete")
    assert r.status_code == 200
    done = r.json()
    assert done["completed"] is True

    r = client.get("/action-items/", params={"completed": True, "limit": 5, "sort": "-created_at"})
    assert r.status_code == 200
    items = r.json()
    assert len(items) >= 1

    r = client.patch(f"/action-items/{item['id']}", json={"description": "Updated"})
    assert r.status_code == 200
    patched = r.json()
    assert patched["description"] == "Updated"


def test_action_items_pagination_limit(client):
    """GET /action-items returns at most 'limit' items."""
    for i in range(5):
        client.post("/action-items/", json={"description": f"Task {i}"})

    r = client.get("/action-items/", params={"limit": 2})
    assert r.status_code == 200
    items = r.json()
    assert len(items) == 2, f"Expected exactly 2 items, got {len(items)}"

    r = client.get("/action-items/", params={"limit": 4})
    assert r.status_code == 200
    items = r.json()
    assert len(items) == 4, f"Expected exactly 4 items, got {len(items)}"


def test_action_items_pagination_skip(client):
    """GET /action-items with skip returns items offset by skip."""
    for i in range(5):
        client.post("/action-items/", json={"description": f"Item {i}"})

    r_all = client.get("/action-items/", params={"limit": 10, "sort": "id"})
    assert r_all.status_code == 200
    all_items = r_all.json()
    assert len(all_items) >= 5

    r_first = client.get("/action-items/", params={"skip": 0, "limit": 2, "sort": "id"})
    r_second = client.get("/action-items/", params={"skip": 2, "limit": 2, "sort": "id"})
    assert r_first.status_code == 200
    assert r_second.status_code == 200

    first_page = r_first.json()
    second_page = r_second.json()
    assert len(first_page) == 2
    assert len(second_page) == 2

    first_ids = [x["id"] for x in first_page]
    second_ids = [x["id"] for x in second_page]
    assert first_ids != second_ids
    assert set(first_ids) & set(second_ids) == set()


def test_action_items_sorting_desc(client):
    """GET /action-items with sort=-field returns descending order."""
    client.post("/action-items/", json={"description": "Alpha"})
    client.post("/action-items/", json={"description": "Beta"})
    client.post("/action-items/", json={"description": "Gamma"})

    r = client.get("/action-items/", params={"limit": 10, "sort": "-description"})
    assert r.status_code == 200
    items = r.json()
    descriptions = [x["description"] for x in items]
    assert descriptions == sorted(descriptions, reverse=True), f"Expected desc, got {descriptions}"


def test_action_items_sorting_asc(client):
    """GET /action-items with sort=field returns ascending order."""
    client.post("/action-items/", json={"description": "Zebra"})
    client.post("/action-items/", json={"description": "Apple"})
    client.post("/action-items/", json={"description": "Mango"})

    r = client.get("/action-items/", params={"limit": 10, "sort": "description"})
    assert r.status_code == 200
    items = r.json()
    descriptions = [x["description"] for x in items]
    assert descriptions == sorted(descriptions), f"Expected asc, got {descriptions}"

