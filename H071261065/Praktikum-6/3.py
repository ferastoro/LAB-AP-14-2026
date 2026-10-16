# SOAL 3 - PLAYTUNE
# Sistem manajemen playlist musik

def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    # tuple dipakai biar data lagu tidak berubah setelah ditambahkan
    lagu = (judul, artis, genre, durasi)
    playlist.append(lagu)
    genre_set.add(genre)  # set menyimpan genre unik


def format_durasi(detik):
    # ubah detik jadi format menit:detik
    menit = detik // 60
    sisa_detik = detik % 60
    return f"{menit}:{sisa_detik:02d}"


def tampilkan_playlist(playlist):
    if not playlist:
        print("Playlist masih kosong.")
        print("Total durasi playlist: 0 menit 0 detik")
        return

    print("\n" + "=" * 63)
    print(f"{'No':<4}{'Judul':<21}{'Artis':<15}{'Genre':<10}{'Durasi':<8}")
    print("=" * 63)

    total_durasi = 0
    for nomor, lagu in enumerate(playlist, start=1):
        judul, artis, genre, durasi = lagu
        # potong teks panjang biar kolom tabel tetap rapi
        print(f"{nomor:<4}{judul[:20]:<21}{artis[:14]:<15}"
              f"{genre:<10}{format_durasi(durasi):<8}")
        total_durasi += durasi

    print("=" * 63)
    print(f"Total durasi playlist: {total_durasi // 60} menit "
          f"{total_durasi % 60} detik")


def filter_genre(playlist, genre_target):
    # list comprehension buat ambil lagu sesuai genre
    return [lagu for lagu in playlist
            if lagu[2].lower() == genre_target.lower()]


def hapus_lagu(playlist, nomor):
    # nomor yang dilihat pengguna mulai dari 1, indeks list mulai dari 0
    if nomor < 1 or nomor > len(playlist):
        print("Nomor lagu tidak valid.")
        return

    lagu = playlist.pop(nomor - 1)  # pop hapus lagu dari indeks yang dipilih
    print(f"Lagu '{lagu[0]}' berhasil dihapus!")


def statistik_playlist(playlist, genre_set):
    print("\n" + "=" * 40)
    print("STATISTIK PLAYLIST PLAYTUNE")
    print("=" * 40)
    print(f"  Total lagu      : {len(playlist)}")
    print(f"  Jumlah genre    : {len(genre_set)}")
    print(f"  Daftar genre    : {genre_set}")

    distribusi = {}
    for genre in genre_set:
        distribusi[genre] = sum(1 for lagu in playlist if lagu[2] == genre)

    print("\n  Distribusi genre:")
    for genre, jumlah in distribusi.items():
        print(f"    {genre:<12}: {'#' * jumlah} ({jumlah})")

    if playlist:
        terpanjang = max(playlist, key=lambda lagu: lagu[3])
        terpendek = min(playlist, key=lambda lagu: lagu[3])
        print(f"\n  Lagu terpanjang : {terpanjang[0]} "
              f"({format_durasi(terpanjang[3])})")
        print(f"  Lagu terpendek : {terpendek[0]} "
              f"({format_durasi(terpendek[3])})")
    else:
        print("\n  Lagu terpanjang : Belum ada lagu")
        print("  Lagu terpendek : Belum ada lagu")
    print("=" * 40)


def input_durasi():
    # try-except biar input huruf tidak bikin program berhenti
    while True:
        try:
            durasi = int(input("Durasi (dalam detik): "))
            if durasi <= 0:
                print("Durasi harus berupa angka positif.")
                continue
            return durasi
        except ValueError:
            print("Durasi harus berupa angka bulat.")


def main():
    playlist = []  # list berisi tuple lagu
    genre_set = set()  # kumpulan genre unik

    print("=" * 40)
    print("PLAYLIST MUSIK - PLAYTUNE")
    print("=" * 40)

    while True:
        print("\nMenu:")
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
            if not judul or not artis:
                print("Judul dan artis tidak boleh kosong.")
                continue

            genre_input = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ").strip().lower()
            # samakan penulisan genre biar RnB tidak berubah jadi Rnb
            genre_map = {
                "pop": "Pop", "rock": "Rock", "jazz": "Jazz",
                "rnb": "RnB", "dangdut": "Dangdut"
            }
            genre = genre_map.get(genre_input, genre_input.capitalize())
            durasi = input_durasi()
            tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)
            print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!")

        elif pilihan == "2":
            tampilkan_playlist(playlist)

        elif pilihan == "3":
            print(f"Genre tersedia: {genre_set}")
            genre_target = input("Masukkan genre yang ingin difilter: ").strip()
            hasil = filter_genre(playlist, genre_target)

            print(f"\nLagu bergenre '{genre_target}':")
            if not hasil:
                print("  Tidak ada lagu untuk genre tersebut.")
            else:
                for nomor, lagu in enumerate(hasil, start=1):
                    print(f"  {nomor}. {lagu[0]} - {lagu[1]} "
                          f"({format_durasi(lagu[3])})")

        elif pilihan == "4":
            tampilkan_playlist(playlist)
            if playlist:
                try:
                    nomor = int(input("Nomor lagu yang ingin dihapus: "))
                    hapus_lagu(playlist, nomor)
                    # hitung ulang genre supaya genre lagu yang dihapus tidak tertinggal
                    genre_set.clear()
                    genre_set.update(lagu[2] for lagu in playlist)
                except ValueError:
                    print("Nomor lagu harus berupa angka bulat.")

        elif pilihan == "5":
            statistik_playlist(playlist, genre_set)

        elif pilihan == "6":
            print("Terima kasih telah menggunakan PlayTune!")
            break

        else:
            print("Pilihan tidak valid. Masukkan angka 1-6.")


if __name__ == "__main__":
    main()
