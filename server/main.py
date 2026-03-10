import logging
import requests
from mcp.server.fastmcp import FastMCP

# Konfigurasi Logging (Wajib mengarah ke stderr untuk server STDIO)
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Inisialisasi Server MCP
mcp = FastMCP("CountriesMCPServer")

BASE_URL = "https://restcountries.com/v3.1"

# TOOL 1: Mencari informasi spesifik suatu negara
@mcp.tool()
def get_country_info(country_name: str) -> str:
    """
    Mengambil informasi detail tentang sebuah negara berdasarkan namanya.
    
    Args:
        country_name: Nama negara dalam bahasa Inggris (contoh: "Germany", "Japan").
    """
    try:
        # Menambahkan timeout=5 untuk memenuhi syarat "resilience"
        response = requests.get(f"{BASE_URL}/name/{country_name}", timeout=5)
        
        # Menangani hasil kosong atau negara tidak ditemukan (HTTP 404)
        if response.status_code == 404:
            return f"Negara '{country_name}' tidak ditemukan. Pastikan ejaannya benar dalam bahasa Inggris."
            
        # Menangani error HTTP lainnya (500, dll)
        response.raise_for_status()
        
        data = response.json()[0] # Ambil hasil pertama yang paling relevan
        
        # Mengekstrak data
        name = data.get("name", {}).get("common", "Unknown")
        capital = data.get("capital", ["Unknown"])[0] if data.get("capital") else "Unknown"
        region = data.get("region", "Unknown")
        population = data.get("population", 0)
        currencies_data = data.get("currencies", {})
        currencies = ", ".join([c["name"] for c in currencies_data.values()]) if currencies_data else "Unknown"
        
        return (
            f"Informasi untuk {name}:\n"
            f"- Ibu Kota: {capital}\n"
            f"- Benua: {region}\n"
            f"- Populasi: {population:,} jiwa\n"
            f"- Mata Uang: {currencies}"
        )

    except requests.exceptions.Timeout:
        logging.error("Request timeout saat menghubungi API")
        return "Gagal mengambil data: Koneksi ke server REST Countries terputus (Timeout)."
    except requests.exceptions.RequestException as e:
        logging.error(f"HTTP Error: {e}")
        return f"Terjadi kesalahan saat menghubungi API: {str(e)}"
    except Exception as e:
        return f"Terjadi kesalahan internal: {str(e)}"

# TOOL 2: Mencari daftar negara berdasarkan benua/region
@mcp.tool()
def get_countries_by_region(region: str) -> str:
    """
    Mendapatkan daftar negara yang berada di benua atau wilayah tertentu.
    
    Args:
        region: Nama benua (pilihan: "Africa", "Americas", "Asia", "Europe", "Oceania").
    """
    try:
        response = requests.get(f"{BASE_URL}/region/{region}", timeout=5)
        
        if response.status_code == 404:
            return f"Wilayah '{region}' tidak valid. Gunakan: Africa, Americas, Asia, Europe, atau Oceania."
            
        response.raise_for_status()
        data = response.json()
        
        # Ambil maksimal 10 negara agar output tidak terlalu panjang
        country_names = [country.get("name", {}).get("common") for country in data[:10]]
        
        return f"Beberapa negara di wilayah {region}:\n" + "\n".join(f"- {name}" for name in country_names)

    except requests.exceptions.Timeout:
        return "Gagal mengambil data: Timeout."
    except Exception as e:
        return f"Terjadi kesalahan: {str(e)}"

# Entrypoint utama
if __name__ == "__main__":
    logging.info("Memulai Countries MCP Server...")
    mcp.run()