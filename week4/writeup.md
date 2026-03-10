# Week 4 Write-up
Tip: To preview this markdown file
- On Mac, press `Command (⌘) + Shift + V`
- On Windows/Linux, press `Ctrl + Shift + V`

## INSTRUCTIONS

Fill out all of the `TODO`s in this file.

## SUBMISSION DETAILS

Name: Nur Hikmah \
SUNet ID: 2310817120010 \
Citations: **Anthropic Claude Code Best Practices, GitHub Copilot**

This assignment took me about **3** hours to do. 


## YOUR RESPONSES
### Automation #1: Global Repository Guidance (CLAUDE.md)
a. Design inspiration (e.g. cite the best-practices and/or sub-agents docs)
> Desain automasi ini terinspirasi dari dokumentasi resmi Anthropic mengenai *Claude Code best practices*, khususnya pada bagian bagaimana memberikan panduan konteks repositori secara global menggunakan file `CLAUDE.md` agar agen AI selalu mengikuti standar proyek.

b. Design of each automation, including goals, inputs/outputs, steps
> * **Goal:** Memberikan peta navigasi kode dasar dan menetapkan aturan *Test-Driven Development* (TDD) yang ketat kepada agen AI.
> * **Inputs/Outputs:** Dibaca secara otomatis saat agen dijalankan di direktori. Tidak ada output terminal langsung, melainkan perubahan perilaku (behavior) agen AI.
> * **Steps:** Menginstruksikan agen bahwa setiap kali diminta membuat fitur baru, ia **wajib** menulis *failing test* di folder `backend/tests/` terlebih dahulu sebelum menulis implementasi kode aslinya di `backend/app/routers/`.

c. How to run it (exact commands), expected outputs, and rollback/safety notes
> **How to run:** Tidak ada perintah khusus. File ini dibaca otomatis setiap kali kita menjalankan perintah `claude` di terminal.
> **Expected output:** Agen AI merespons dengan rencana kerja yang selalu menempatkan penulisan tes (pengujian) sebagai langkah pertama.

d. Before vs. after (i.e. manual workflow vs. automated workflow)
> * **Before:** Agen AI (atau developer) sering kali langsung menulis fitur tanpa pengujian, menyebabkan arsitektur rentan dan *error* sulit dilacak.
> * **After:** *Workflow* terstandarisasi. Setiap fitur baru dijamin memiliki *test coverage* karena AI dipaksa membuat pengujiannya terlebih dahulu sesuai aturan di file panduan.

e. How you used the automation to enhance the starter application
> *(Hybrid Approach Note: Karena limitasi billing pada Anthropic Console API, saya mengadaptasi aturan automasi ini menggunakan GitHub Copilot di editor).* > Saat mengerjakan tugas "Add search endpoint for notes", saya secara ketat mengikuti aturan di `CLAUDE.md` ini dengan menyuruh Copilot membuat *failing test* `test_search_notes` terlebih dahulu. Setelah tes selesai dibuat dan divalidasi gagal (karena fitur belum ada), barulah saya menyuruh AI menulis fungsi `search_notes` di *router* dan menyambungkannya ke frontend (`app.js`).


### Automation #2: Custom Slash Command (/test-and-lint)
a. Design inspiration (e.g. cite the best-practices and/or sub-agents docs)
> Terinspirasi dari dokumentasi Anthropic mengenai penyederhanaan tugas repetitif *developer* menggunakan *custom slash commands* (`.claude/commands/*.md`).

b. Design of each automation, including goals, inputs/outputs, steps
> * **Goal:** Menjalankan seluruh *pipeline* pengujian dan perapian kode dalam satu perintah singkat.
> * **Inputs/Outputs:** Dipicu dengan mengetik `/test-and-lint`. Menghasilkan output berupa log terminal gabungan dari *pytest*, *black*, dan *ruff*.
> * **Steps:** >   1. Menjalankan `python -m pytest -q backend/tests` (menggunakan `python -m` untuk menghindari isu *PYTHONPATH* di Windows).
>   2. Berhenti mengeksekusi jika ada tes yang gagal (error).
>   3. Jika semua tes hijau (*passed*), dilanjutkan dengan mengeksekusi `black .` dan `ruff check . --fix`.

c. How to run it (exact commands), expected outputs, and rollback/safety notes
> **How to run:** Ketikkan perintah `/test-and-lint` di dalam sesi *prompt* Claude.
> **Expected output:** Laporan ringkas yang menyatakan semua tes lulus beserta hasil pemformatan kode.
> **Safety notes:** Agen diinstruksikan untuk berhenti seketika di langkah 1 apabila ada pengujian yang gagal, lalu memberikan saran perbaikan (*rollback* kode) tanpa memaksa melakukan *linting*.

d. Before vs. after (i.e. manual workflow vs. automated workflow)
> * **Before:** *Developer* harus mengetikkan `make test` (yang mana sering *error* di Windows), `make format`, dan `make lint` secara manual dan berturut-turut setiap kali selesai mengubah kode. Sangat rawan terlewat.
> * **After:** Seluruh proses validasi (*testing*, *formatting*, *linting*) terangkum dalam satu *command* otomatis yang *cross-platform* (ramah pengguna Windows), memastikan kode selalu lolos standar sebelum di-*commit*.

e. How you used the automation to enhance the starter application
> *(Meneruskan pendekatan Hybrid).* Saya mengeksekusi urutan langkah dari automasi ini secara manual di Anaconda Prompt untuk memvalidasi fitur pencarian `/search` yang dibuat sebelumnya. Automasi proses ini sangat membantu karena berhasil mendeteksi *Error 422 Unprocessable Entity* (karena ketiadaan *trailing slash* pada pemanggilan URL pengujian) dan masalah *WinError 32* (koneksi SQLite yang tidak ditutup di lingkungan Windows). Setelah *bug* tersebut diperbaiki, *pipeline* sukses memberikan output 100% *passed* dan kode berhasil dirapikan secara sempurna.
### *(Optional) Automation #3*
*If you choose to build additional automations, feel free to detail them here!*

a. Design inspiration (e.g. cite the best-practices and/or sub-agents docs)
> TODO

b. Design of each automation, including goals, inputs/outputs, steps
> TODO

c. How to run it (exact commands), expected outputs, and rollback/safety notes
> TODO

d. Before vs. after (i.e. manual workflow vs. automated workflow)
> TODO

e. How you used the automation to enhance the starter application
> TODO
