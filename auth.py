from utils import pause, users
from admin import menu_admin
from user import menu_user
import inquirer

def login():
    """Fungsi untuk proses login user"""
    global users  # Mengakses variabel global

    print("=== LOGIN ===")
    
    # Gunakan inquirer untuk input login
    questions = [
        inquirer.Text('nama', message="Username"),
        inquirer.Password('pw', message="Password") # Gunakan Password untuk menyembunyikan input
    ]
    
    answers = inquirer.prompt(questions)
    if not answers: # Jika prompt dibatalkan
        print("Login dibatalkan.")
        pause()
        return
        
    nama = answers['nama']
    pw = answers['pw']

    # Validasi input kosong
    if not nama or not pw:
        print("Username dan password tidak boleh kosong!")
        pause()
        return

    # Error Handling saat mengakses dictionary
    try:
        # Cek apakah user ada dan password benar
        if users[nama]["password"] == pw:
            role = users[nama]["role"]
            if role == "admin":
                menu_admin()
            else:
                menu_user(nama)
        else:
            print("Login gagal! Password salah.")
    except KeyError: # Jika username tidak ditemukan
        print("Login gagal! Username tidak ditemukan.")
    except Exception as e: # Error lainnya
        print(f"Terjadi kesalahan saat login: {e}")
    pause()


def register():
    """Fungsi untuk proses registrasi user baru"""
    global users

    print("=== REGISTER AKUN BARU ===")
    
    # Gunakan inquirer untuk input registrasi
    questions = [
        inquirer.Text('nama', message="Masukkan username baru"),
        inquirer.Password('pw', message="Masukkan password baru")
    ]
    
    answers = inquirer.prompt(questions)
    if not answers:  # Jika prompt dibatalkan
        print("Registrasi dibatalkan.")
        pause()
        return

    nama = answers['nama']
    pw = answers['pw']

    nama_kosong = not nama.strip()
    pw_kosong = not pw.strip()

    if nama_kosong and pw_kosong:
        print("Username dan password tidak boleh kosong atau hanya berisi spasi!")
        pause()
        return
    elif nama_kosong:
        print("Username tidak boleh kosong atau hanya berisi spasi!")
        pause()
        return
    elif pw_kosong:
        print("Password tidak boleh kosong atau hanya berisi spasi!")
        pause()
        return

    # Validasi username dan password tidak boleh sama
    if nama == pw:
        print("Username dan password tidak boleh sama!")
        pause()
        return

    # Simpan akun baru
    try:
        if nama not in users:
            users[nama] = {"password": pw, "role": "user"}
            print("Akun berhasil dibuat!")
        else:
            print("Username sudah digunakan!")
    except Exception as e:
        print(f"Terjadi kesalahan saat registrasi: {e}")

    pause()