# Input data
nama_lengkap = "muhammad yusuf"
nim = "2409106093"
harga_gula = float(input("masukan harga gula : "))

# Diskon masing-masing jenis gula
diskon_gulaku = 7
diskon_manis_kita = 11
diskon_gunung_madu = 13

# menghitung diskon
harga_gulaku = harga_gula - (harga_gula * diskon_gulaku/100)
harga_manis_kita = harga_gula - (harga_gula * diskon_manis_kita/100)
harga_gunung_madu = harga_gula - (harga_gula * diskon_gunung_madu/100)

# mengeluarkan hasil
print(f"{nama_lengkap} dengan nim {nim}")
print(f"Harga gula seharga beras: Rp {harga_gula}")
print(f"harga gulaku adalah : Rp {harga_gulaku} dari diskon 7%")
print(f"harga manis kita adalah : Rp {harga_manis_kita} dari diskon 11%")
print(f"harga gunung madu adalah : Rp {harga_gunung_madu} dari diskon 13%")

