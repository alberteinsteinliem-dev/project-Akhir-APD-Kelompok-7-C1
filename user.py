from utils import pause, clear_screen, lomba, peserta
from prettytable import PrettyTable
import inquirer

def format_rupiah(nilai_str):
    try:
        cleaned = nilai_str.replace('.', '').replace(',', '')
        angka = int(cleaned)
        return f"Rp {angka:,}".replace(',', '.')
    except (ValueError, TypeError):
        return nilai_str

def tampil_lomba(data_lomba):
    if len(data_lomba) == 0:
        print("Belum ada lomba terdaftar.")
    else:
        table = PrettyTable()
        table.field_names = ["ID", "Nama Lomba", "Tanggal", "Aturan", "Hadiah"]
        for urutan, (id_asli, d) in enumerate(data_lomba.items(), start=1):
            hadiah_tampil = format_rupiah(d['hadiah'])
            table.add_row([urutan, d['nama'], d['tanggal'], d['aturan'], hadiah_tampil])
        print(table)

def daftar_lomba(nama_pengguna):
    global peserta, lomba
    tampil_lomba(lomba)
    if not lomba:
        print("Tidak ada lomba untuk didaftar.")
        pause()
        return

    # Hanya tampilkan nama lomba (tanpa angka/ID di depan)
    choices = [val['nama'] for val in lomba.values()]
    questions = [
        inquirer.List('nama_lomba', message="Pilih lomba", choices=choices)
    ]
    answers = inquirer.prompt(questions)
    if not answers:
        print("Pendaftaran lomba dibatalkan.")
        pause()
        return

    nama_pilih = answers['nama_lomba']

    # Cari ID lomba berdasarkan nama yang dipilih
    id_lomba = None
    for key, data in lomba.items():
        if data['nama'] == nama_pilih:
            id_lomba = key
            break

    if id_lomba is None:
        print("Lomba tidak ditemukan.")
        pause()
        return

    # Validasi duplikat pendaftaran
    for p in peserta:
        if p.get("nama") == nama_pengguna and p.get("lomba") == nama_pilih:
            print("Anda sudah terdaftar di lomba ini!")
            pause()
            return

    # Daftarkan peserta
    try:
        peserta.append({
            "nama": nama_pengguna,
            "lomba": nama_pilih
        })
        print("Berhasil terdaftar.")
    except Exception as e:
        print(f"Terjadi kesalahan saat mendaftar: {e}")
    pause()

def lihat_lomba_diikuti(nama_pengguna):
    global peserta, lomba
    try:
        table = PrettyTable()
        table.field_names = ["Nama Lomba", "Tanggal", "Aturan", "Hadiah"]
        ada = False

        for p in peserta:
            if p.get("nama") == nama_pengguna:
                nama_lomba = p["lomba"]
                lomba_ditemukan = None
                for data in lomba.values():
                    if data["nama"] == nama_lomba:
                        lomba_ditemukan = data
                        break

                if lomba_ditemukan:
                    hadiah_tampil = format_rupiah(lomba_ditemukan["hadiah"])
                    table.add_row([
                        lomba_ditemukan["nama"],
                        lomba_ditemukan["tanggal"],
                        lomba_ditemukan["aturan"],
                        hadiah_tampil
                    ])
                    ada = True

        if not ada:
            print("Belum ikut lomba apa pun.")
        else:
            print("Lomba yang Anda ikuti:")
            print(table)

    except Exception as e:
        print(f"Terjadi kesalahan saat melihat lomba: {e}")
    pause()

def menu_user(nama):
    global lomba, peserta
    while True:
        clear_screen()
        print(r"""
 ______ ____   ______  _______  __    __       ______   ______  _______   ______   ______  __    __ _______   ______  
|      \    \ /      \|       \|  \  |  \     /      \ /      \|       \ /      \ /      \|  \  |  \       \ |      \ 
| ▓▓▓▓▓▓\▓▓▓▓\  ▓▓▓▓▓▓\ ▓▓▓▓▓▓▓\ ▓▓  | ▓▓    |  ▓▓▓▓▓▓\  ▓▓▓▓▓▓\ ▓▓▓▓▓▓▓\  ▓▓▓▓▓▓\  ▓▓▓▓▓▓\ ▓▓  | ▓▓ ▓▓▓▓▓▓▓\ \▓▓▓▓▓▓\
| ▓▓ | ▓▓ | ▓▓ ▓▓    ▓▓ ▓▓  | ▓▓ ▓▓  | ▓▓    | ▓▓  | ▓▓ ▓▓    ▓▓ ▓▓  | ▓▓ ▓▓  | ▓▓ ▓▓  | ▓▓ ▓▓  | ▓▓ ▓▓  | ▓▓/      ▓▓
| ▓▓ | ▓▓ | ▓▓ ▓▓▓▓▓▓▓▓ ▓▓  | ▓▓ ▓▓__/ ▓▓    | ▓▓__/ ▓▓ ▓▓▓▓▓▓▓▓ ▓▓  | ▓▓ ▓▓__| ▓▓ ▓▓__| ▓▓ ▓▓__/ ▓▓ ▓▓  | ▓▓  ▓▓▓▓▓▓▓
| ▓▓ | ▓▓ | ▓▓\▓▓     \ ▓▓  | ▓▓\▓▓    ▓▓    | ▓▓    ▓▓\▓▓     \ ▓▓  | ▓▓\▓▓    ▓▓\▓▓    ▓▓\▓▓    ▓▓ ▓▓  | ▓▓\▓▓    ▓▓
 \▓▓  \▓▓  \▓▓ \▓▓▓▓▓▓▓\▓▓   \▓▓ \▓▓▓▓▓▓     | ▓▓▓▓▓▓▓  \▓▓▓▓▓▓▓\▓▓   \▓▓_\▓▓▓▓▓▓▓_\▓▓▓▓▓▓▓ \▓▓▓▓▓▓ \▓▓   \▓▓ \▓▓▓▓▓▓▓
                                             | ▓▓                       |  \__| ▓▓  \__| ▓▓                           
                                             | ▓▓                        \▓▓    ▓▓\▓▓    ▓▓                           
                                              \▓▓                         \▓▓▓▓▓▓  \▓▓▓▓▓▓                            
""")
        questions = [
            inquirer.List('pilih', 
                          message="Pilih menu", 
                          choices=[
                              '1. Lihat Lomba',
                              '2. Daftar Lomba',
                              '3. Lihat Lomba yang Diikuti',
                              '4. Kembali'
                          ])
        ]
        answers = inquirer.prompt(questions)
        if not answers:
            print("Logout dari akun pengguna.")
            break
        pilih = answers['pilih'].split('.')[0]

        if pilih == "1":
            tampil_lomba(lomba)
            pause()
        elif pilih == "2":
            daftar_lomba(nama)
        elif pilih == "3":
            lihat_lomba_diikuti(nama)
        elif pilih == "4":
            break
        else:
            print("Pilihan tidak valid!")
            pause()