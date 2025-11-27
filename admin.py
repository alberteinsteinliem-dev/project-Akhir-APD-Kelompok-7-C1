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

def hanya_huruf_dan_spasi(teks):
    for char in teks:
        if not (('a' <= char <= 'z') or ('A' <= char <= 'Z') or char == ' '):
            return False
    return True

def validasi_tanggal_desember_januari(tanggal_str):
    try:
        parts = tanggal_str.strip().split()
        if len(parts) != 3:
            return False
        hari_str, bulan_str, tahun_str = parts
        if not hari_str.isdigit():
            return False
        hari = int(hari_str)
        if not tahun_str.isdigit():
            return False
        bulan_norm = bulan_str.capitalize()
        if bulan_norm in ["Januari", "Desember"]:
            if hari < 1 or hari > 31:
                return False
        return True
    except:
        return False

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

def tambah_lomba():
    global lomba
    print("=== TAMBAH LOMBA BARU ===")
    questions = [
        inquirer.Text('nama_lomba', message="Lomba"),
        inquirer.Text('hari', message="Tanggal lomba"),
        inquirer.Text('aturan', message="Aturan lomba"),
        inquirer.Text('hadiah', message="Hadiah lomba"),
    ]
    answers = inquirer.prompt(questions)
    if not answers:
        print("Penambahan lomba dibatalkan.")
        pause()
        return

    nama_input = answers['nama_lomba'].strip()
    hari_input = answers['hari'].strip()
    aturan_input = answers['aturan'].strip()
    hadiah_input = answers['hadiah'].strip()

    if not nama_input or not hari_input or not aturan_input or not hadiah_input:
        print("Semua field wajib diisi!")
        pause()
        return
    if not validasi_tanggal_desember_januari(hari_input):
        print("Format tanggal salah!")
        pause()
        return
    if not hanya_huruf_dan_spasi(nama_input):
        print("Nama lomba hanya boleh berisi huruf dan spasi!")
        pause()
        return
    for data in lomba.values():
        if data['nama'].strip().lower() == nama_input.lower():
            print("Lomba dengan nama ini sudah digunakan.")
            pause()
            return

    try:
        id_baru = max(lomba.keys()) + 1 if lomba else 1
        lomba[id_baru] = {
            "nama": nama_input,
            "tanggal": hari_input,
            "aturan": aturan_input,
            "hadiah": hadiah_input
        }
        print("Lomba berhasil ditambahkan!")
    except Exception as e:
        print(f"Ada kesalahan ketika menambah lomba: {e}")
    pause()

def hapus_lomba():
    global lomba, peserta
    tampil_lomba(lomba)
    if not lomba:
        print("Tidak ada lomba untuk dihapus.")
        pause()
        return

    choices = [d['nama'] for d in lomba.values()]
    questions = [inquirer.List('nama', message="Pilih lomba yang ingin dihapus", choices=choices)]
    answers = inquirer.prompt(questions)
    if not answers:
        pause()
        return

    nama_pilih = answers['nama']
    id_hapus = None
    for id_lomba, data in lomba.items():
        if data['nama'] == nama_pilih:
            id_hapus = id_lomba
            break

    if id_hapus is not None:
        # Hapus lomba
        del lomba[id_hapus]
        
        # Hapus semua peserta yang mendaftar lomba ini
        peserta = [p for p in peserta if p["lomba"] != nama_pilih]
        
        print("Lomba dan seluruh pendaftarnya berhasil dihapus!")
    else:
        print("Lomba tidak ditemukan.")
    pause()

def ubah_lomba():
    global lomba
    tampil_lomba(lomba)
    if not lomba:
        print("Tidak ada lomba untuk diubah.")
        pause()
        return

    choices = [data['nama'] for data in lomba.values()]
    questions = [inquirer.List('nama_lomba', message="Pilih lomba yang ingin diubah", choices=choices)]
    answers = inquirer.prompt(questions)
    if not answers:
        print("Pengubahan lomba dibatalkan.")
        pause()
        return

    nama_dipilih = answers['nama_lomba']
    id_lomba = None
    data_lama = None
    for id_key, data in lomba.items():
        if data['nama'] == nama_dipilih:
            id_lomba = id_key
            data_lama = data
            break

    if id_lomba is None:
        print("Lomba tidak ditemukan.")
        pause()
        return

    print("Masukkan data baru (tekan Enter untuk tetap):")
    questions_update = [
        inquirer.Text('nama_baru', message="Nama", default=data_lama['nama']),
        inquirer.Text('tanggal_baru', message="Tanggal", default=data_lama['tanggal']),
        inquirer.Text('aturan_baru', message="Aturan", default=data_lama['aturan']),
        inquirer.Text('hadiah_baru', message="Hadiah", default=data_lama['hadiah']),
    ]
    answers_update = inquirer.prompt(questions_update)
    if not answers_update:
        print("Pengubahan lomba dibatalkan.")
        pause()
        return

    nama_baru = answers_update['nama_baru'].strip()
    tanggal_baru = answers_update['tanggal_baru'].strip()
    aturan_baru = answers_update['aturan_baru'].strip()
    hadiah_baru = answers_update['hadiah_baru'].strip()

    if not nama_baru or not tanggal_baru or not aturan_baru or not hadiah_baru:
        print("Semua field wajib diisi!")
        pause()
        return
    if not validasi_tanggal_desember_januari(tanggal_baru):
        print("Format tanggal salah!")
        pause()
        return
    if not hanya_huruf_dan_spasi(nama_baru):
        print("Nama lomba hanya boleh berisi huruf dan spasi!")
        pause()
        return

    try:
        lomba[id_lomba] = {
            "nama": nama_baru,
            "tanggal": tanggal_baru,
            "aturan": aturan_baru,
            "hadiah": hadiah_baru
        }
        print("Data lomba berhasil diubah!")
    except Exception as e:
        print(f"Terjadi kesalahan saat mengubah lomba: {e}")
    pause()

def lihat_peserta():
    global peserta
    try:
        if len(peserta) == 0:
            print("Belum ada peserta terdaftar.")
        else:
            table = PrettyTable()
            table.field_names = ["Nama Peserta", "Mengikuti"]
            for p in peserta:
                table.add_row([p["nama"], p["lomba"]])
            print(table)
    except Exception as e:
        print(f"Ada kesalahan saat menampilkan peserta: {e}")
    pause()

def menu_admin():
    global lomba, peserta
    while True:
        clear_screen()
        print(r"""
                                                             __              __          
                                                            |  \            |  \         
 ______ ____   ______  _______  __    __       ______   ____| ▓▓______ ____  \▓▓_______  
|      \    \ /      \|       \|  \  |  \     |      \ /      ▓▓      \    \|  \       \ 
| ▓▓▓▓▓▓\▓▓▓▓\  ▓▓▓▓▓▓\ ▓▓▓▓▓▓▓\ ▓▓  | ▓▓      \▓▓▓▓▓▓\  ▓▓▓▓▓▓▓ ▓▓▓▓▓▓\▓▓▓▓\ ▓▓ ▓▓▓▓▓▓▓\
| ▓▓ | ▓▓ | ▓▓ ▓▓    ▓▓ ▓▓  | ▓▓ ▓▓  | ▓▓     /      ▓▓ ▓▓  | ▓▓ ▓▓ | ▓▓ | ▓▓ ▓▓ ▓▓  | ▓▓
| ▓▓ | ▓▓ | ▓▓ ▓▓▓▓▓▓▓▓ ▓▓  | ▓▓ ▓▓__/ ▓▓    |  ▓▓▓▓▓▓▓ ▓▓__| ▓▓ ▓▓ | ▓▓ | ▓▓ ▓▓ ▓▓  | ▓▓
| ▓▓ | ▓▓ | ▓▓\▓▓     \ ▓▓  | ▓▓\▓▓    ▓▓     \▓▓    ▓▓\▓▓    ▓▓ ▓▓ | ▓▓ | ▓▓ ▓▓ ▓▓  | ▓▓
 \▓▓  \▓▓  \▓▓ \▓▓▓▓▓▓▓\▓▓   \▓▓ \▓▓▓▓▓▓       \▓▓▓▓▓▓▓ \▓▓▓▓▓▓▓\▓▓  \▓▓  \▓▓\▓▓\▓▓   \▓▓                                                                                    
""")
        questions = [
            inquirer.List('pilih', 
                          message="Pilih menu", 
                          choices=[
                              '1. Lihat Semua Lomba',
                              '2. Tambah Lomba',
                              '3. Ubah Lomba',
                              '4. Hapus Lomba',
                              '5. Lihat Peserta',
                              '6. Kembali'
                          ])
        ]
        answers = inquirer.prompt(questions)
        if not answers:
            print("Logout dari akun admin.")
            break
        pilih = answers['pilih'].split('.')[0]

        if pilih == "1":
            tampil_lomba(lomba)
            pause()
        elif pilih == "2":
            tambah_lomba()
        elif pilih == "3":
            ubah_lomba()
        elif pilih == "4":
            hapus_lomba()
        elif pilih == "5":
            lihat_peserta()
        elif pilih == "6":
            break
        else:
            print("Pilihan tidak valid!")
            pause()
