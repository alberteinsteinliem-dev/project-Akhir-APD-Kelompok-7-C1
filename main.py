from utils import clear_screen, garis, pause
from auth import login, register
import inquirer

def menu_utama():
    """Fungsi utama untuk menampilkan menu utama"""
    while True: # Perulangan utama program
        clear_screen() # Bersihkan layar sebelum menampilkan menu
        print(r"""
░░NAVTALY░ALBERT░RIDHO░
░░╔══╗░░░░░░░░░░╔══╗░░░
░╚╣▐▐╠╝░░╔══╗░░╚╣▐▐╠╝░░
░░╚╦╦╝░░╚╣▌▌╠╝░░╚╦╦╝░░░
░░░╚╚░░░░╚╦╦╝░░░░╚╚░░░░
░░░░░░░░░░╝╝░░░░░░░░░░░""")
        print(r"""
░▒█▀▀▄░█▀▀▄░█▀▀░▀█▀░█▀▀▄░█▀▀▄░░░▒█░░░░▄▀▀▄░█▀▄▀█░█▀▀▄░█▀▀▄░░░▀▀█▀▀░█▀▀▄░█░░░░█░▒█░█▀▀▄░░░▒█▀▀▄░█▀▀▄░█▀▀▄░█░▒█
░▒█░▒█░█▄▄█░█▀░░░█░░█▄▄█░█▄▄▀░░░▒█░░░░█░░█░█░▀░█░█▀▀▄░█▄▄█░░░░▒█░░░█▄▄█░█▀▀█░█░▒█░█░▒█░░░▒█▀▀▄░█▄▄█░█▄▄▀░█░▒█
░▒█▄▄█░▀░░▀░▀░░░░▀░░▀░░▀░▀░▀▀░░░▒█▄▄█░░▀▀░░▀░░▒▀░▀▀▀▀░▀░░▀░░░░▒█░░░▀░░▀░▀░░▀░░▀▀▀░▀░░▀░░░▒█▄▄█░▀░░▀░▀░▀▀░░▀▀▀
""")
        
        # Gunakan inquirer untuk memilih menu
        questions = [
            inquirer.List('menu', 
                          message="Pilih menu", 
                          choices=['1. Login', '2. Register', '3. Keluar'])
        ]
        
        answers = inquirer.prompt(questions)
        if not answers: # Jika prompt dibatalkan
            print("Program dihentikan.")
            break
        
        menu = answers['menu'].split('.')[0] # Ambil angka dari pilihan

        # Percabangan if/elif/else
        if menu == "1":
            login()
        elif menu == "2":
            register()
        elif menu == "3":
            print("Terima kasih! Semoga beruntung!!")
            break # Keluar dari perulangan utama
        else:
            print("Pilihan tidak valid!")
            pause()

# Panggil fungsi utama untuk memulai program
if __name__ == "__main__":
    menu_utama()