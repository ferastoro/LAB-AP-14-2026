def tambah_buku(inventaris, judul, penulis, harga, stok):
    buku = {
        "judul": judul,
        "penulis": penulis,
        "harga": harga,
        "stok": stok
    }
    inventaris.append(buku)
    print("Buku berhasil ditambahkan!")


def cari_buku(inventaris, kata_kunci):
    ditemukan = 0

    for buku in inventaris:
        if kata_kunci.lower() in buku["judul"].lower():
            print(buku)
            ditemukan += 1

    if ditemukan == 0:
        print("Buku tidak ditemukan.")


def update_stok(inventaris, judul, jumlah):
    for buku in inventaris:
        if buku["judul"].lower() == judul.lower():
            stok_baru = buku["stok"] + jumlah

            if stok_baru < 0:
                print("Gagal! Stok tidak boleh negatif.")
            else:
                buku["stok"] = stok_baru
                print("Stok berhasil diperbarui!")
            return

    print("Buku tidak ditemukan.")


def ringkasan_inventaris(inventaris):
    jumlah_buku = len(inventaris)
    total_stok = 0
    total_aset = 0

    for buku in inventaris:
        total_stok += buku["stok"]
        total_aset += buku["harga"] * buku["stok"]

    print("Jumlah jenis buku:", jumlah_buku)
    print("Total seluruh stok:", total_stok)
    print("Total nilai aset: Rp", total_aset)

    if jumlah_buku > 0:
        termahal = inventaris[0]

        for buku in inventaris:
            if buku["harga"] > termahal["harga"]:
                termahal = buku

        print("Buku termahal:", termahal["judul"])


inventaris = []

while True:
    print("SISTEM INVENTARIS BUKU BOOKNEST")
    print("1. Tambah Buku")
    print("2. Cari Buku")
    print("3. Update Stok")
    print("4. Ringkasan Inventaris")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        judul = input("Judul buku: ")
        penulis = input("Penulis: ")

        try:
            harga = float(input("Harga: "))
            stok = int(input("Stok awal: "))

            if harga < 0 or stok < 0:
                print("Harga dan stok tidak boleh negatif.")
            else:
                tambah_buku(inventaris, judul, penulis, harga, stok)

        except ValueError:
            print("Harga harus angka dan stok harus bilangan bulat.")

    elif pilihan == "2":
        kata_kunci = input("Kata kunci judul: ")
        cari_buku(inventaris, kata_kunci)

    elif pilihan == "3":
        judul = input("Judul buku yang ingin diupdate: ")

        try:
            jumlah = int(input("Jumlah perubahan (positif=tambah, negatif=kurang): "))
            update_stok(inventaris, judul, jumlah)

        except ValueError:
            print("Perubahan stok harus berupa bilangan bulat.")

    elif pilihan == "4":
        ringkasan_inventaris(inventaris)

    elif pilihan == "5":
        print("Terima kasih telah menggunakan BookNest!")
        break

    else:
        print("Pilihan tidak valid.")