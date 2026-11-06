


def tambah_buku(inventaris, judul, penulis, harga, stok):
    buku = {"judul": judul, "penulis": penulis, "harga": harga, "stok": stok}
    inventaris.append(buku)
    print(f"buku '{judul}' berhasil ditambahkan")

def cari_buku(inventaris, kata_kunci):
    hasil = [b for b in inventaris if kata_kunci.lower() in b["judul"].lower()]
    if hasil:
        print(f"ditemukan {len(hasil)} buku:")
        for i, b in enumerate(hasil, 1):
            print(f" {i}. {b['judul']} - {b['penulis']} | Rp{b['harga']} | stok: {b['stok']}")
    else:
        print("buku tidak ditemukan")

def update_stok(inventaris, judul, jumlah):
    for b in inventaris:
        if b["judul"].lower() == judul.lower():
            stok_baru = b["stok"] + jumlah
            if stok_baru < 0:
                print("stok tidak boleh negatif.")
            else:
                b["stok"] = stok_baru
                if jumlah < 0:
                    print(f"stok '{b['judul']}' berkurang {-jumlah}. stok sekarang: {stok_baru}")
                else:
                    print(f"stok '{b['judul']}' bertambah {+jumlah}. stok sekarang: {stok_baru}")
            return 
    print("error buku tidak ditemukan")

def ringkasan_inventaris(inventaris):
    total_stok = sum(b["stok"] for b in inventaris)
    total_aset = sum(b["harga"] * b["stok"] for b in inventaris)
    print("=" * 40)
    print("RINGKASAN INVENTARIS BOOKNEST")
    print("=" * 40)
    print(f"jumlah jenis buku : {len(inventaris)}")
    print(f"total seluruh stok : {total_stok}")
    print(f"total nilai aset : Rp{total_aset}")
    if inventaris:
        termahal = max(inventaris, key=lambda b: b ["harga"])
        print(f"buku termahal   : {termahal['judul']} (Rpi{termahal['harga']})")
    else:
        print("buku termahal   :belum ada buku")
    print("=" * 40)

inventaris = []

while True:
    print("\nmenu:")
    print("1. tambah buku")
    print("2. cari buku")
    print("3. update stok")
    print("4. ringkasan inventaris")
    print("5. keluar")
    menu = input("pilih menu (1-5): ")

    if menu == "1":
        judul = input("judul buku: ")
        penulis = input("penulis: ")
        try:
            harga = float(input("harga: "))
            stok = int(input("stok awal: "))
            if harga < 0 or stok < 0:
                print("harga dan stok tidak boleh negatif")
            else:
                tambah_buku(inventaris, judul, penulis, harga, stok)
        except ValueError:
            print("harga harus berupa angka dan stok harus berupa bilangan bulat")

    elif menu == "2":
        kata_kunci = input("masukkan kata kunci judul: ")
        cari_buku(inventaris, kata_kunci)

    elif menu == "3":
        judul = input("judul buku yang ingim di update: ")
        try:
            jumlah = int(input("jumlah perubahan (positif=tambah, negatif=kurang): "))
            update_stok(inventaris, judul, jumlah)
        except ValueError:
            print("jumlah perubahan harus angka bulat")

    elif menu == "4":
        ringkasan_inventaris (inventaris)

    elif menu == "5":
        print("terima kasih telah menggunakan booknest")
        break
    else:
        print("pilihan tidak valid")