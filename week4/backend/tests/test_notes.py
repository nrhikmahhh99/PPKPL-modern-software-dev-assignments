def test_create_and_list_notes(client):
    payload = {"title": "Test", "content": "Hello world"}
    r = client.post("/notes/", json=payload)
    assert r.status_code == 201, r.text
    data = r.json()
    assert data["title"] == "Test"

    r = client.get("/notes/")
    assert r.status_code == 200
    items = r.json()
    assert len(items) >= 1

    r = client.get("/notes/search/")
    assert r.status_code == 200

    r = client.get("/notes/search/", params={"q": "Hello"})
    assert r.status_code == 200
    items = r.json()
    assert len(items) >= 1

def test_search_notes(client):
    # Buat catatan baru untuk dicari
    client.post("/notes/", json={"title": "Tugas Kuliah", "content": "Belajar membuat REST API"})
    
    # Lakukan pencarian menggunakan parameter 'q' dengan garis miring yang BENAR
    response = client.get("/notes/search/?q=REST") 
    assert response.status_code == 200
    
    # Validasi hasilnya
    data = response.json()
    assert len(data) > 0
    assert "REST" in data[0]["content"]