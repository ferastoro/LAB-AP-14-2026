def tambah_buku(inventaris, judul, penulis, harga, stok):
    buku = {
        "judul": judul,
        "penulis": penulis,
        "harga": harga,
        "stok": stok
    }
    inventaris.append(buku)
    print(f"Buku '{judul}' berhasil ditambahkan!")

def cari_buku(inventaris, kata_kunci):
    hasil = [buku for buku in inventaris if kata_kunci.lower() in buku["judul"].lower()]
    if hasil:
        print(f"Ditemukan {len(hasil)} buku:")
        for i, buku in enumerate(hasil, 1):
            print(f"{i}. {buku['judul']}")
            print(f"   {buku['penulis']} | Rp{buku['harga']} | Stok: {buku['stok']}")
    else:
        print("Tidak ada buku yang ditemukan dengan kata kunci tersebut.")

def update_stok(inventaris, judul, jumlah):
    for buku in inventaris:
        if buku["judul"].lower() == judul.lower():
            stok_baru = buku["stok"] + jumlah
            if stok_baru < 0:
                print(f"Gagal! Stok '{buku['judul']}' tidak boleh negatif.")
            else:
                buku["stok"] = stok_baru
                status = "berkurang" if jumlah < 0 else "bertambah"
                print(f"Stok '{buku['judul']}' {status} {abs(jumlah)}. Stok sekarang: {buku['stok']}")
            return
    print(f"Error: Buku dengan judul '{judul}' tidak ditemukan.")

def ringkasan_inventaris(inventaris):
    if not inventaris:
        print("Inventaris masih kosong.")
        return
    
    jumlah_jenis = len(inventaris)
    total_stok = sum(buku["stok"] for buku in inventaris)
    total_nilai_aset = sum(buku["harga"] * buku["stok"] for buku in inventaris)
    buku_termahal = max(inventaris, key=lambda x: x["harga"])
    
    print("RINGKASAN INVENTARIS BOOKNEST")
    print("=" * 30)
    print(f"Jumlah jenis buku: {jumlah_jenis}")
    print(f"Total seluruh stok: {total_stok}")
    print(f"Total nilai aset : Rp{total_nilai_aset}")
    print(f"Buku termahal    : {buku_termahal['judul']} (Rp{buku_termahal['harga']})")

def main_booknest():
    inventaris = []
    while True:
        print("\nMenu:")
        print("1. Tambah Buku")
        print("2. Cari Buku")
        print("3. Update Stok")
        print("4. Ringkasan Inventaris")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ").strip()
        
        if pilihan == "1":
            judul = input("Judul buku: ")
            penulis = input("Penulis: ")
            try:
                harga = float(input("Harga: "))
                stok = int(input("Stok awal: "))
                if harga < 0 or stok < 0:
                    print("Harga dan stok tidak boleh negatif!")
                    continue
                tambah_buku(inventaris, judul, penulis, harga, stok)
            except ValueError:
                print("Error: Harga harus berupa angka dan stok harus berupa bilangan bulat!")
        
        elif pilihan == "2":
            kata_kunci = input("Masukkan kata kunci judul: ")
            cari_buku(inventaris, kata_kunci)
            
        elif pilihan == "3":
            judul = input("Judul buku yang ingin diupdate: ")
            try:
                jumlah = int(input("Jumlah perubahan (positif tambah, negatif=kurang): "))
                update_stok(inventaris, judul, jumlah)
            except ValueError:
                print("Error: Jumlah perubahan harus berupa angka!")
                
        elif pilihan == "4":
            ringkasan_inventaris(inventaris)
            
        elif pilihan == "5":
            print("Terima kasih telah menggunakan BookNest!")
            break
        else:
            print("Pilihan tidak valid, silakan pilih antara 1-5.")

if __name__ == "__main__":
    main_booknest()