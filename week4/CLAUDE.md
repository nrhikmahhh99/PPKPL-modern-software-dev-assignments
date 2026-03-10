# Panduan Proyek (CLAUDE.md)

Ini adalah "developer's command center", aplikasi full-stack minimalis dengan backend FastAPI (SQLite/SQLAlchemy) dan frontend statis.

## Navigasi Kode

- **Backend (API):** `backend/app/main.py` dan `backend/app/routers/`
- **Frontend (UI):** `frontend/index.html` dan `frontend/app.js`
- **Database:** `backend/app/db.py` (data awal ada di `data/seed.sql`)
- **Tests:** `backend/tests/`

## Aturan Workflow (Penting!)

Jika saya meminta Anda untuk menambahkan fitur atau endpoint baru:

1. **Pikirkan skenarionya**, lalu edit atau buat file yang relevan di `backend/app/` atau `frontend/`.
2. Jika perlu menambah _routing_, pastikan mendaftarkannya di `main.py`.
3. Setelah menulis fitur, jalankan _slash command_ yang tersedia untuk melakukan testing.
4. Jangan menghapus fungsi yang sudah ada kecuali jika diminta.
