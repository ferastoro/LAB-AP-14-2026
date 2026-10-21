def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    playlist.append((judul, artis, genre, durasi))
    genre_set.add(genre)


def tampilkan_playlist(playlist):
    for i, lagu in enumerate(playlist, 1):
        menit = lagu[3] // 60
        detik = lagu[3] % 60
        print(i, lagu[0], "-", lagu[1], "-", lagu[2],
              f"({menit}:{detik:02d})")

    total = sum(lagu[3] for lagu in playlist)
    print("Total durasi:", total // 60, "menit", total % 60, "detik")


def filter_genre(playlist, genre_target):
    return [lagu for lagu in playlist
            if lagu[2].lower() == genre_target.lower()]


def hapus_lagu(playlist, nomor):
    if 1 <= nomor <= len(playlist):
        playlist.pop(nomor - 1)
        print("Lagu berhasil dihapus!")
    else:
        print("Nomor lagu tidak valid.")


def statistik_playlist(playlist, genre_set):
    print("Total lagu:", len(playlist))
    print("Jumlah genre:", len(genre_set))
    print("Daftar genre:", genre_set)

    distribusi = {}
    for lagu in playlist:
        distribusi[lagu[2]] = distribusi.get(lagu[2], 0) + 1

    print("Distribusi genre:", distribusi)

    if playlist:
        terpanjang = max(playlist, key=lambda lagu: lagu[3])
        terpendek = min(playlist, key=lambda lagu: lagu[3])
        print("Lagu terpanjang:", terpanjang[0])
        print("Lagu terpendek:", terpendek[0])


playlist = []
genre_set = set()

while True:
    print("1. Tambah Lagu")
    print("2. Tampilkan Playlist")
    print("3. Filter Genre")
    print("4. Hapus Lagu")
    print("5. Statistik Playlist")
    print("6. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        judul = input("Judul lagu: ")
        artis = input("Artis: ")
        genre = input("Genre (Pop/Rock/Jazz/RnB/Dandut): ")

        try:
            durasi = int(input("Durasi (detik): "))
            if durasi > 0:
                tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)
                print("Lagu berhasil ditambahkan!")
            else:
                print("Durasi harus positif.")
        except ValueError:
            print("Durasi harus berupa angka.")

    elif pilih == "2":
        tampilkan_playlist(playlist)

    elif pilih == "3":
        print("Genre tersedia:", genre_set)
        genre = input("Genre yang dicari: ")
        hasil = filter_genre(playlist, genre)

        for lagu in hasil:
            print(lagu)

        if not hasil:
            print("Lagu tidak ditemukan.")

    elif pilih == "4":
        tampilkan_playlist(playlist)
        try:
            nomor = int(input("Nomor lagu yang dihapus: "))
            hapus_lagu(playlist, nomor)
            genre_set.clear()
            for lagu in playlist:
                genre_set.add(lagu[2])
        except ValueError:
            print("Masukkan nomor yang benar.")

    elif pilih == "5":
        statistik_playlist(playlist, genre_set)

    elif pilih == "6":
        print("Terima kasih telah menggunakan PlayTune!")
        break

    else:
        print("Pilihan tidak valid.")