def format_durasi(detik):
    menit = detik // 60
    sisa = detik % 60
    if sisa < 10:
        return f"{menit}:0{sisa}"                    
    return f"{menit}:{sisa}"


def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    genre_final = genre
    for g in genre_set:
        if g.lower() == genre.lower():
            genre_final = g
    lagu = (judul, artis, genre_final, durasi)
    playlist.append(lagu)
    genre_set.add(genre_final)
    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!")


def tampilkan_playlist(playlist):
    if len(playlist) == 0:
        print("Playlist masih kosong.")
        return
    print("=" * 55)
    print(f"{'No':<4}{'Judul':<22}{'Artis':<16}{'Genre':<8}Durasi")
    print("=" * 55)
    nomor = 1
    total_detik = 0
    for lagu in playlist:
        print(f"{nomor:<4}{lagu[0]:<22}{lagu[1]:<16}{lagu[2]:<8}{format_durasi(lagu[3])}")
        total_detik = total_detik + lagu[3]
        nomor = nomor + 1
    print("=" * 55)
    print(f"Total durasi playlist: {total_detik // 60} menit {total_detik % 60} detik")


def filter_genre(playlist, genre_target):
    return [lagu for lagu in playlist if lagu[2].lower() == genre_target.lower()]


def hapus_lagu(playlist, nomor):
    if nomor < 1 or nomor > len(playlist):
        print(f"Nomor lagu tidak valid. Pilih 1 sampai {len(playlist)}.")
        return False
    lagu = playlist.pop(nomor - 1)
    print(f"Lagu '{lagu[0]}' berhasil dihapus.")
    return True


def statistik_playlist(playlist, genre_set):
    print("=" * 40)
    print(" STATISTIK PLAYLIST PLAYTUNE")
    print("=" * 40)
    if len(playlist) == 0:
        print(" Playlist masih kosong, belum ada statistik.")
        print("=" * 40)
        return

    print(f" Total lagu   : {len(playlist)}")
    print(f" Jumlah genre : {len(genre_set)}")
    print(f" Daftar genre : {genre_set}")

    hitung = {}
    for lagu in playlist:
        genre = lagu[2]
        if genre in hitung:
            hitung[genre] = hitung[genre] + 1
        else:
            hitung[genre] = 1
    print(" Distribusi genre:")
    for genre in hitung:
        batang = "#" * hitung[genre]                
        print(f"   {genre:<8}: {batang} ({hitung[genre]})")

    terpanjang = playlist[0]
    terpendek = playlist[0]
    for lagu in playlist:
        if lagu[3] > terpanjang[3]:
            terpanjang = lagu
        if lagu[3] < terpendek[3]:
            terpendek = lagu
    print(f" Lagu terpanjang : {terpanjang[0]} ({format_durasi(terpanjang[3])})")
    print(f" Lagu terpendek  : {terpendek[0]} ({format_durasi(terpendek[3])})")
    print("=" * 40)


playlist = []
genre_set = set()

print("=" * 40)
print(" PLAYLIST MUSIK - PLAYTUNE")
print("=" * 40)

while True:
    print("Menu:")
    print("1. Tambah Lagu")
    print("2. Tampilkan Playlist")
    print("3. Filter berdasarkan Genre")
    print("4. Hapus Lagu")
    print("5. Statistik Playlist")
    print("6. Keluar")
    pilihan = input("Pilih menu (1-6): ").strip()

    if pilihan == "1":
        judul = input("Judul lagu: ").strip()
        artis = input("Artis: ").strip()
        genre = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ").strip()
        if judul == "" or artis == "" or genre == "":
            print("Judul, artis, dan genre tidak boleh kosong.")
        else:
            try:
                durasi = int(input("Durasi (dalam detik): "))
                if durasi <= 0:
                    print("Durasi harus berupa angka positif.")
                else:
                    tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)
            except ValueError:
                print("Durasi harus berupa angka bulat.")

    elif pilihan == "2":
        tampilkan_playlist(playlist)

    elif pilihan == "3":
        if len(playlist) == 0:
            print("Playlist masih kosong.")
        else:
            print(f"Genre tersedia: {genre_set}")
            genre_target = input("Masukkan genre yang ingin difilter: ").strip()
            hasil = filter_genre(playlist, genre_target)
            if len(hasil) == 0:
                print(f"Tidak ada lagu bergenre '{genre_target}'.")
            else:
                print(f"Lagu bergenre '{genre_target}':")
                nomor = 1
                for lagu in hasil:
                    print(f" {nomor}. {lagu[0]} - {lagu[1]} ({format_durasi(lagu[3])})")
                    nomor = nomor + 1

    elif pilihan == "4":
        if len(playlist) == 0:
            print("Playlist masih kosong, tidak ada lagu yang bisa dihapus.")
        else:
            tampilkan_playlist(playlist)
            try:
                nomor = int(input("Nomor lagu yang ingin dihapus: "))
                if hapus_lagu(playlist, nomor):
                    genre_set.clear()
                    for lagu in playlist:
                        genre_set.add(lagu[2])
            except ValueError:
                print("Nomor lagu harus berupa angka.")

    elif pilihan == "5":
        statistik_playlist(playlist, genre_set)

    elif pilihan == "6":
        print("Terima kasih telah menggunakan PlayTune!")
        break

    else:
        print("Pilihan tidak valid, masukkan angka 1-6.")