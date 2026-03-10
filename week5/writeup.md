# Week 5 Write-up

Tip: To preview this markdown file

- On Mac, press `Command (⌘) + Shift + V`
- On Windows/Linux, press `Ctrl + Shift + V`

## INSTRUCTIONS

Fill out all of the `TODO`s in this file.

## SUBMISSION DETAILS

Name: **Nur Hikmah** \
SUNet ID: **2310817120010** \
Citations: **Warp AI**

This assignment took me about **3** hours to do.

## YOUR RESPONSES

### Automation A: Warp Drive saved prompts, rules, MCP servers

a. Design of each automation, including goals, inputs/outputs, steps

> Saya membuat Saved Prompt di dalam Warp Drive untuk mengimplementasikan fitur pagination (Task 8). Tujuannya adalah menambahkan parameter page dan page_size pada endpoint list. Inputnya berupa instruksi teks: "Tolong baca file backend/app/routers/notes.py dan action_items.py. Implementasikan fitur pagination...". Outputnya adalah modifikasi kode pada kedua file backend tersebut yang mengembalikan data dalam format items dan total.

b. Before vs. after (i.e. manual workflow vs. automated workflow)

> Sebelum menggunakan otomatisasi ini, saya harus memikirkan logika pembatasan data (limit/offset) dan mengetik ulang struktur kembalian dictionary secara manual. Setelah menggunakan Warp Drive, saya hanya perlu memanggil prompt yang sudah disimpan, dan agen AI langsung menulis dan memasukkan kodenya dalam hitungan detik.

c. Autonomy levels used for each completed task (what code permissions, why, and how you supervised)

> Saya memberikan izin penuh kepada AI untuk membaca direktori (read) dan menerapkan perubahan kode secara langsung (write/apply changes). Saya memberikan izin ini untuk menguji tingkat kemandirian AI. Pengawasan saya lakukan dengan meninjau diff kode yang diubah dan menguji endpoint tersebut.

d. (if applicable) Multi‑agent notes: roles, coordination strategy, and concurrency wins/risks/failures

> N/A (Fokus pada satu agen, catatan multi-agen dijelaskan di bagian B).

e. How you used the automation (what pain point it resolves or accelerates)

> Otomatisasi ini sangat mempercepat penulisan kode boilerplate yang repetitif seperti pagination. Ini menghilangkan pain point kelelahan mengetik kode standar, sehingga developer bisa mengalokasikan waktu untuk arsitektur yang lebih kompleks.

### Automation B: Multi‑agent workflows in Warp

a. Design of each automation, including goals, inputs/outputs, steps

> Saya menjalankan dua agen AI secara bersamaan di dua tab Warp Terminal yang berbeda. Tab pertama (Agen A) bertugas mengerjakan Task 8 (Pagination), sedangkan tab kedua (Agen B) bertugas mengerjakan Task 7 (Global Exception Handlers & Response Envelopes). Keduanya bekerja secara paralel memodifikasi file backend yang berbeda.

b. Before vs. after (i.e. manual workflow vs. automated workflow)

> Secara manual, pengembangan dua fitur ini harus dilakukan secara berurutan (sequential). Dengan multi-agent workflow, pengembangan dua fitur berbeda dapat diselesaikan dalam waktu yang hampir bersamaan (parallel), sangat memangkas waktu pengerjaan.

c. Autonomy levels used for each completed task (what code permissions, why, and how you supervised)

> Kedua agen diberikan otonomi eksekusi kode untuk mengubah main.py, schemas.py, dan router. Saya bertindak sebagai Mandor atau pengawas tingkat tinggi (human-in-the-loop) yang memantau pekerjaan mereka, lalu melakukan pengujian integrasi akhir melalui browser (UI).

d. (if applicable) Multi‑agent notes: roles, coordination strategy, and concurrency wins/risks/failures

> Concurrency risks & failures: Terjadi masalah integrasi yang menarik saat kedua agen bekerja. Karena Agen A dan B bekerja terpisah (silo) dalam memodifikasi struktur respons backend (menjadi format {"ok": true, "data": {"items": []}}), mereka mengabaikan file frontend. Akibatnya, script app.js tidak mengenali format respons baru tersebut, yang menyebabkan tombol 'Add' pada UI tidak berfungsi dan list tidak muncul. Saya harus melakukan intervensi dengan memberikan instruksi baru kepada AI untuk membaca dan memperbaiki app.js agar selaras dengan backend.

e. How you used the automation (what pain point it resolves or accelerates)

> Multi-agent ini secara luar biasa mempercepat penyelesaian banyak fitur (akselerasi waktu). Namun, ini menyelesaikan pain point lain: menyadarkan bahwa pendelegasian buta kepada AI bisa memecah integrasi sistem. Pengalaman ini membuktikan bahwa peran developer berevolusi dari sekadar "pengetik kode" menjadi "manajer sistem" yang harus mengawasi gambaran besar (UI/UX hingga Database).

### (Optional) Automation C: Any Additional Automations

a. Design of each automation, including goals, inputs/outputs, steps

> TODO

b. Before vs. after (i.e. manual workflow vs. automated workflow)

> TODO

c. Autonomy levels used for each completed task (what code permissions, why, and how you supervised)

> TODO

d. (if applicable) Multi‑agent notes: roles, coordination strategy, and concurrency wins/risks/failures

> TODO

e. How you used the automation (what pain point it resolves or accelerates)

> TODO
