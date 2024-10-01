username_benar = "yusuf"
password_benar = "93"
attempts = 0
login_berhasil = False

while attempts < 3 :
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        
        if username == username_benar and password == password_benar :
            print("login berhasil!, apakan anda ingin lanjut untuk membeli tiket?")
            login_berhasil = True
            break
        else :
            attempts += 1
            print(f"Username atau password salah. Sisa percobaan: {3 - attempts}") 

if not login_berhasil :
    print("Terlalu banyak percobaan. Program dihentikan.")
    
    
else :
    while True :
        jawab = input()
        if jawab == "g" or jawab == "gk" or jawab == "ngak" or jawab == "ga" :
            print("program di batalkan!")
            break
        else :
            print("program di lanjutkan")
    
        
        hari = input("Masukkan hari yang di inginkan untuk membeli tiket! ")
        uang = int(input("Masukkan uang Anda (dalam Rp): "))
        if hari == "senin" or hari == "selasa" or hari == "rabu" or hari == "kamis":
            print("harga tiket Rp 40000")
            harga_tiket = 40000
            if uang < harga_tiket :
                print(f"Maaf, {username}. Uang Anda tidak cukup untuk membeli tiket pada hari {hari}.")
            else :
                print(f"nama pembeli {username}! dibeli pada hari {hari}.")
        elif hari == "jumat":
            print("harga tiket Rp 45000")
            harga_tiket = 45000
            if uang < harga_tiket :
                print(f"Maaf, {username}. Uang Anda tidak cukup untuk membeli tiket pada hari {hari}.")
            else :
                print(f"nama pembeli {username}! dibeli pada hari {hari}.")
        elif hari == "sabtu":
            print("harga tiket Rp 55000")
            harga_tiket = 55000
            if uang < harga_tiket :
                print(f"Maaf, {username}. Uang Anda tidak cukup untuk membeli tiket pada hari {hari}.")
            else :
                print(f"nama pembeli {username}! dibeli pada hari {hari}.")
        elif hari == "minggu":
            print("harga tiket Rp 60000")
            harga_tiket = 60000
            if uang < harga_tiket:
                print(f"Maaf, {username}. Uang Anda tidak cukup untuk membeli tiket pada hari {hari}.")
            else :
                print(f"nama pembeli {username}! dibeli pada hari {hari}.")
        else:
            print("Hari yang Anda masukkan tidak valid. Silakan masukkan hari yang benar.")