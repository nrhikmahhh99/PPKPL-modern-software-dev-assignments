# Perintah: /test-and-lint

**Tujuan:**
Perintah ini digunakan untuk menjalankan seluruh rangkaian pengujian (pytest) dan merapikan kode (linting & formatting) dalam satu langkah otomatis.

**Langkah-langkah yang harus dilakukan oleh agen (Claude):**

1. Eksekusi perintah shell python -m pytest -q backend/tests untuk menjalankan pengujian.
2. Jika ada tes yang gagal (error), berhenti sejenak dan berikan saya ringkasan kegagalan tersebut serta saran kode untuk memperbaikinya.
3. Jika semua tes sukses (passed), langsung lanjutkan dengan mengeksekusi perintah shell `black .` kemudian dilanjutkan dengan `ruff check . --fix`.
4. Berikan pesan penutup yang ceria bahwa semua kode telah berhasil diuji dan dirapikan.
