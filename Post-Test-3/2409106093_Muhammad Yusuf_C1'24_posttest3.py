# Meminta data
nama = input("Masukkan nama Anda: ")
hari = input("Masukkan hari : ")
uang = int(input("Masukkan uang Anda (dalam Rp): "))

# Menentukan harga tiket berdasarkan hari dengan if-else
if hari == "senin" or hari == "selasa" or hari == "rabu" or hari == "kamis":
    harga_tiket = 40000
    if uang < harga_tiket :
            print(f"Maaf, {nama}. Uang Anda tidak cukup untuk membeli tiket pada hari {hari}.")
    else :
            print(f"nama pembeli {nama}! dibeli pada hari {hari}.")
elif hari == "jumat":
    harga_tiket = 45000
    if uang < harga_tiket :
            print(f"Maaf, {nama}. Uang Anda tidak cukup untuk membeli tiket pada hari {hari}.")
    else :
            print(f"nama pembeli {nama}! dibeli pada hari {hari}.")
    
elif hari == "sabtu":
    harga_tiket = 55000
    if uang < harga_tiket :
            print(f"Maaf, {nama}. Uang Anda tidak cukup untuk membeli tiket pada hari {hari}.")
    else :
            print(f"nama pembeli {nama}! dibeli pada hari {hari}.")
    
elif hari == "minggu":
    harga_tiket = 60000
    if uang < harga_tiket:
            print(f"Maaf, {nama}. Uang Anda tidak cukup untuk membeli tiket pada hari {hari}.")
    else :
            print(f"nama pembeli {nama}! dibeli pada hari {hari}.")
    
else:
    print("Hari yang Anda masukkan tidak valid. Silakan masukkan hari yang benar.")