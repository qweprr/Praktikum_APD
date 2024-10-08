akuns = []

oshis = {
    "Feni": {
        "Gen": 3,
        "prestasi": ["Rank 2 SSK 2019", "9x Senbatsu", "2x SPV"]
    },
    "Gracia": {
        "Gen": 3,
        "prestasi": ["Rank 10 SSK 2019", "10x Senbatsu", "2x SPV"]
    },
    "Gita": {
        "Gen": 6,
        "prestasi": ["3x Senbatsu", "2x SPV"]
    },
    "Christy": {
        "Gen": 7,
        "prestasi": ["Rank 13 SSK 2019", "6x Senbatsu","3x SPV"]
    },
    "Olla": {
        "Gen": 7,
        "prestasi": ["1x Senbatsu","1x SPV"]
    },
    "Freya": {
        "Gen": 7,
        "prestasi": ["2x Senbatsu","4x SVP"]
    },
    "Eli": {
        "Gen": 7,
        "prestasi": ["Rank 15 SSK 2019","3x Senbatsu","2x SPV"]
    },
    "Jessi": {
        "Gen": 7,
        "prestasi": ["2x Senbatsu","2x SPV"]
    },
    "Muthe": {
        "Gen": 7,
        "prestasi": ["3x Senbatsu","3x SVP"]
    },
    "Onile": {
        "Gen": 8,
        "prestasi": ["1x Senbatsu","3x SPV"]
    },
    "Fiony": {
        "Gen": 8,
        "prestasi": ["4x Senbatsu","1x SPV"]
    },
    "Flora": {
        "Gen": 8,
        "prestasi": ["1x Senbatsu","2x SPV"]
    },
    "Adel": {
        "Gen": 8,
        "prestasi": ["2x Senbatsu","1x SPV","Mau Graduate:( )"]
    },
    "Lulu": {
        "Gen": 8,
        "prestasi": ["1x Senbatsu","2x SPV"]
    },
    "Kathrina": {
        "Gen": 9,
        "prestasi": ["3x Senbatsu","2x SPV"]
    },
    "Indah": {
        "Gen": 9,
        "prestasi": ["2x Senbatsu","1x SPV"]
    },
    "Marsha": {
        "Gen": 9,
        "prestasi": ["4x Senbatsu","2x SPV"]
    },
    "Amanda": {
        "Gen": 10,
        "prestasi": []
    },
    "Lia": {
        "Gen": 10,
        "prestasi": []
    },
    "Cellie": {
        "Gen": 10,
        "prestasi": []    
    },
    "Ella": {
        "Gen": 10,
        "prestasi": ["2x SPV"]
    },
    "Raisha": {
        "Gen": 10,
        "prestasi": []
    },
    "Indira": {
        "Gen": 10,
        "prestasi": []
    },
    "Greesel": {
        "Gen": 11,
        "prestasi": ["1x SPV"]
    },
    "Gracie": {
        "Gen": 11,
        "prestasi": []
    },
    "Alya": {
        "Gen": 11,
        "prestasi": []
    },
    "Anin": {
        "Gen": 11,
        "prestasi": []
    },
    "Chthy": {
        "Gen": 11,
        "prestasi": []
    },
    "elin": {
        "Gen": 11,
        "prestasi": [] 
    },
    "Chelsea": {
        "Gen": 11,
        "prestasi": []
    },
    "Dena": {
        "Gen": 11,
        "prestasi": []
    },
    "desy": {
        "Gen": 11,
        "prestasi": []
    },
    "Gendis": {
        "Gen": 11,
        "prestasi": []
    },
    "Michie": {
        "Gen": 11,
        "prestasi": []
    },
    "Aralie": {
        "Gen": 12,
        "prestasi": []
    },
    "Delyn": {
        "Gen": 12,
        "prestasi": ["Bocil Skem"]
    },
    "Lana": {
        "Gen": 12,
        "prestasi": []
    },
    "Erine": {
        "Gen": 12,
        "prestasi": []
    },
    "Fritzy": {
        "Gen": 12,
        "prestasi": []
    },
    "Lily": {
        "Gen": 12,
        "prestasi": ["MyLuvly"]
    },
    "Trisha": {
        "Gen": 12,
        "prestasi": []
    },
    "Moreen": {
        "Gen": 12,
        "prestasi": []
    },
    "Levi": {
        "Gen": 12,
        "prestasi": [] 
    },
    "Nayla": {
        "Gen": 12,
        "prestasi": []
    },
    "Nachia": {
        "Gen": 12,
        "prestasi": []
    },
    "Oline": {
        "Gen": 12,
        "prestasi": []
    },
    "Regi": {
        "Gen": 12,
        "prestasi": []
    },
    "Ribka": {
        "Gen": 12,
        "prestasi": []
    },
    "Nala": {
        "Gen": 12,
        "prestasi": []
    },
    "Kimmy": {
        "Gen": 12,
        "prestasi": []
    },
}

import os

while True:
    print("Halo! Selamat datang di Web Official JKT48")
    print("Silakan pilih Registrasi terlebih dahulu jika belum buat akun!")
    print("="*20)
    print("1. Registrasi")
    print("2. Login")
    print("3. Keluar")
    print("="*20)
    
    opsi = input("Pilih opsi: ")
    print(" ")

    if opsi == "1":
        print("Halo FJKT48! Silahkan Registrasi dulu")
        Username = input("Username: ")
        akuna = False
        for akun in akuns:
            if akun[0] == Username:
                akuna = True
                break
        if akuna:
            print("Nama Sudah Terpakai:b. Silahkan Coba Lagi")
        else:
            Password = input("Password: ")
            akuns.append([Username, Password, []])
            print(f"Akun Anda berhasil terdaftar dengan ID: {Username}")

    elif opsi == "2":
        print("Hallo, FJKT48, silahkan masukan akun anda!")
        Username = input("Username: ")
        Password = input("Password: ")
        for akun in akuns:
            if akun[0] == Username and akun[1] == Password:
                while True:
                    print(f"\nSelamat datang di web JKT48 {akun[0]}!")
                    print("===== Silahkan pilih Opsi =====")
                    print("1. Pilih Oshi Kamu")
                    print("2. List Oshi Kamu")
                    print("3. Ganti Oshi")
                    print("4. Menghapus Oshi")
                    print("5. Keluar")
                    
                    opsi = input("Pilih opsi: ")
                    print(" ")

                    if opsi == "1":
                        print("Pilih generasi yang diinginkan")
                        print("="*20)
                        unique_gens = set(data["Gen"] for data in oshis.values())
                        for gen in sorted(unique_gens):
                            print(f"Gen {gen}")
                        
                        Gen = input("Masukkan generasi: ")
                        
                        available_oshis = {oshi: data for oshi, data in oshis.items() if str(data["Gen"]) == Gen}
                        
                        if available_oshis:
                            print("="*20)
                            print(f"Anggota Gen {Gen}:")
                            for member in available_oshis.keys():
                                print(member)

                            oshi = input("Masukkan Nama Oshi: ")
                            print("="*20)
                            print( )
                            if oshi in available_oshis:
                                akun[2].append(oshi)
                                print(f"{oshi} telah ditambahkan ke Oshi Kamu!")
                                print("===== Prestasi =====")
                                for prestasi in available_oshis[oshi]["prestasi"]:
                                    print(prestasi)
                            else:
                                print("Oshi kamu mungkin sudah graduate.")
                        else:
                            print("="*20)
                            print("Graduate semua, yang member member aja")

                    elif opsi == "2":
                        if akun[2]:
                            print("="*20)
                            print("Daftar Oshi Kamu:")
                            for oshi in akun[2]:
                                print(oshi)
                        else:
                            print("Kamu belum memiliki oshi.")

                    elif opsi == "3":
                        old_oshi = input("Masukkan Oshi yang ingin diganti: ")
                        if old_oshi in akun[2]:
                            new_oshi = input("Masukkan Oshi baru: ")
                            if new_oshi in oshis:
                                akun[2][akun[2].index(old_oshi)] = new_oshi
                                print(f"Oshi Kamu telah diganti dari {old_oshi} menjadi {new_oshi}.")
                            else:
                                print("Oshi baru tidak valid.")
                        else:
                            print("Oshi tidak ditemukan dalam daftar Kamu.")

                    elif opsi == "4":
                        oshi = input("Masukkan Oshi yang ingin dihapus: ")
                        if oshi in akun[2]:
                            akun[2].remove(oshi)
                            print(f"Oshi {oshi} telah dihapus dari daftar Kamu.")
                        else:
                            print("Oshi tidak ditemukan dalam daftar Kamu.")

                    elif opsi == "5":
                        print("Terima kasih! Sampai jumpa.")
                        break
                    else:
                        print("Opsi tidak valid, silakan coba lagi.")

                break
        else:
            print("Username atau password salah.")

    elif opsi == "3":
        print("Terima kasih sudah menggunakan Web kami. sampai jumpa lagi :) !")
        break

    else:
        print("Opsi tidak valid, silakan coba lagi.")
