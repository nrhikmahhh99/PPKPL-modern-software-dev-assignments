# Week 3 - REST Countries MCP Server

Ini adalah implementasi kustom Model Context Protocol (MCP) Server untuk tugas Week 3. Server ini membungkus [REST Countries API](https://restcountries.com/) publik untuk memberikan kemampuan kepada AI Agent (seperti Claude) dalam mencari informasi demografis detail mengenai suatu negara dan menampilkan daftar negara berdasarkan letak benua/wilayahnya.

Server ini dijalankan secara lokal menggunakan transport STDIO dan dibangun menggunakan pustaka `FastMCP` dari SDK resmi MCP Python.

## 🛠️ Prerequisites & Environment Setup

Pastikan telah menginstal Python (atau Anaconda) di komputer.

1. **Buka terminal atau Anaconda Prompt**, lalu arahkan ke folder proyek:
   ```bash
   cd path/to/week3/server
   ```
2. **Aktifkan virtual environment** (misalnya jika menggunakan Conda):
   ```bash
   conda activate cs146s
   ```
3. **Instal dependencies yang dibutuhkan**
   ```bash
   pip install mcp requests
   (Catatan: Saya menggunakan requests untuk melakukan pemanggilan HTTP ke eksternal API, dan mcp untuk menjalankan server protocol).
   ```

## 🚀 Run Instructions & Client Configuration

Karena server ini menggunakan transport STDIO, server tidak berjalan di port jaringan, melainkan dipanggil langsung oleh klien MCP seperti Claude Desktop melalui konfigurasi.
**Konfigurasi Claude Desktop**
Tambahkan konfigurasi berikut ke dalam file konfigurasi Claude Desktop.

- Windows: %APPDATA%\Claude\claude_desktop_config.json
- Mac: ~/Library/Application Support/Claude/claude_desktop_config.json

```json
{
  "mcpServers": {
    "countries_server": {
      "command": "path/to/your/python.exe",
      "args": [
        "path/to/your/week3/server/main.py"
      ]
    }
  }
}
(Penting: Sesuaikan command dengan path Python environment dan args dengan path file main.py).
Setelah disimpan, Restart aplikasi Claude Desktop.

## 🧰 Tool Reference
Server ini mengekspos 2 tools utama kepada klien AI:
1. get_country_info
- Deskripsi: Mengambil informasi detail tentang sebuah negara berdasarkan namanya, termasuk ibu kota, benua, populasi, dan mata uang yang digunakan.
- Parameter: * country_name (string): Nama negara dalam ejaan bahasa Inggris. Contoh: "Germany", "Japan".
- Expected Behavior: Melakukan pemanggilan ke endpoint /name/{country_name} dengan batas timeout 5 detik untuk ketahanan (resilience). Mengembalikan string ringkasan data, atau pesan error graceful jika negara tidak ditemukan (HTTP 404).
2. get_countries_by_region
- Deskripsi: Mendapatkan daftar beberapa negara yang berada di benua atau wilayah tertentu.
- Parameter:
region (string): Nama benua. Pilihan yang valid: "Africa", "Americas", "Asia", "Europe", "Oceania".
- Expected Behavior: Memanggil endpoint /region/{region}. Mengembalikan daftar maksimal 10 negara di region tersebut agar output tidak membebani batas token klien.

## 💡 Example Invocation Flow
Setelah ikon tools (palu/colokan) muncul di Claude Desktop, Anda dapat mengetikkan prompt (perintah) natural seperti berikut untuk memicu tools:
User: "Tolong carikan saya informasi detail tentang negara Germany menggunakan tools yang tersedia, lalu sebutkan juga beberapa negara lain yang ada di Europe."
Claude akan:
- Meminta izin mengeksekusi tools.
- Memanggil get_country_info dengan argumen {"country_name": "Germany"}.
- Memanggil get_countries_by_region dengan argumen {"region": "Europe"}.
- Membaca balasan JSON/teks dari server lokal, merangkumnya, dan menyajikannya kepada pengguna.
```
