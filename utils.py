import os

# Struktur data kolektif (Dictionary & List)
users = {
    "NAR": {"password": "Luluskan", "role": "admin"}
}
lomba = {
    1: {
        "nama": "Lomba Mobile Legends",
        "tanggal": "1 Januari 2025",
        "aturan": "Dilarang cheat",
        "hadiah": "Rp 1.000.000"
    }
}
peserta = [] # List untuk menyimpan data pendaftaran

# Fungsi untuk membersihkan layar
def clear_screen():
    """Membersihkan layar terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def garis():
    """Fungsi tanpa parameter"""
    print("=======================================")

def pause():
    """Fungsi tanpa parameter"""
    input("Pencet enter untuk lanjut...")
    clear_screen() # Tambahkan clear_screen setelah pause

def valid_angka(teks):
    """Fungsi dengan parameter dan return value"""
    try:
        int(teks)
        return True
    except ValueError:
        return False