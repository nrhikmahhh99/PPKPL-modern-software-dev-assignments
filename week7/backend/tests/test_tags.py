def test_create_list_tags(client):
    payload = {"name": "work"}
    r = client.post("/tags/", json=payload)
    assert r.status_code == 201, r.text
    data = r.json()
    assert data["name"] == "work"
    assert "id" in data
    assert "created_at" in data and "updated_at" in data

    r = client.get("/tags/")
    assert r.status_code == 200
    items = r.json()
    assert len(items) >= 1
    names = [t["name"] for t in items]
    assert "work" in names


def test_get_tag_by_id(client):
    r = client.post("/tags/", json={"name": "personal"})
    assert r.status_code == 201
    tag = r.json()

    r = client.get(f"/tags/{tag['id']}")
    assert r.status_code == 200
    data = r.json()
    assert data["id"] == tag["id"]
    assert data["name"] == "personal"


def test_get_tag_not_found(client):
    r = client.get("/tags/99999")
    assert r.status_code == 404
    assert "not found" in r.json()["detail"].lower()


def test_patch_tag(client):
    r = client.post("/tags/", json={"name": "urgent"})
    assert r.status_code == 201
    tag = r.json()

    r = client.patch(f"/tags/{tag['id']}", json={"name": "high-priority"})
    assert r.status_code == 200
    patched = r.json()
    assert patched["name"] == "high-priority"


def test_delete_tag(client):
    r = client.post("/tags/", json={"name": "todelete"})
    assert r.status_code == 201
    tag = r.json()

    r = client.delete(f"/tags/{tag['id']}")
    assert r.status_code == 204

    r = client.get(f"/tags/{tag['id']}")
    assert r.status_code == 404


def test_create_duplicate_tag_fails(client):
    r = client.post("/tags/", json={"name": "duplicate"})
    assert r.status_code == 201

    r = client.post("/tags/", json={"name": "duplicate"})
    assert r.status_code == 400
    assert "already exists" in r.json()["detail"].lower()


def test_list_tags_with_query(client):
    client.post("/tags/", json={"name": "python"})
    client.post("/tags/", json={"name": "javascript"})
    client.post("/tags/", json={"name": "rust"})

    r = client.get("/tags/", params={"q": "script"})
    assert r.status_code == 200
    items = r.json()
    names = [t["name"] for t in items]
    assert "javascript" in names


def test_list_tags_pagination(client):
    for i in range(5):
        client.post("/tags/", json={"name": f"tag-{i}"})

    r = client.get("/tags/", params={"skip": 0, "limit": 2})
    assert r.status_code == 200
    items = r.json()
    assert len(items) <= 2
