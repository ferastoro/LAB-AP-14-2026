# SOAL 2 - VOTECLASS
# Sistem pemilihan ketua kelas

def daftar_kandidat(kandidat_set, nama):
    # rapikan nama kandidat sesuai aturan soal
    nama = nama.strip().capitalize()
    if not nama:
        return
    if nama in kandidat_set:
        print(f"'{nama}' sudah terdaftar sebagai kandidat.")
    else:
        kandidat_set.add(nama)  # set otomatis menyimpan nama unik
        print(f"'{nama}' berhasil didaftarkan sebagai kandidat!")


def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    # simpan kunci pemilih dalam huruf kecil biar duplikat ketahuan
    nama_asli = nama_pemilih.strip()
    kunci_pemilih = nama_asli.lower()
    pilihan = pilihan.strip().capitalize()

    if kunci_pemilih in rekap_suara:
        print(f"'{nama_asli}' sudah memberikan suara sebelumnya!")
        return

    if pilihan not in kandidat_set:
        print("Error: kandidat tidak tersedia. Suara tidak dicatat.")
        return

    rekap_suara[kunci_pemilih] = pilihan
    print(f"Suara '{nama_asli}' untuk '{pilihan}' berhasil dicatat!")


def hitung_suara(rekap_suara, kandidat_set):
    # mulai semua kandidat dari 0 suara, termasuk yang belum dipilih
    perolehan = {nama: 0 for nama in kandidat_set}
    for pilihan in rekap_suara.values():
        perolehan[pilihan] += 1
    return perolehan


def tampilkan_hasil(perolehan):
    print("\n" + "=" * 40)
    print("HASIL PEMILIHAN KETUA KELAS")
    print("=" * 40)

    for nama, jumlah in perolehan.items():
        print(f"  {nama}: {jumlah} suara")

    total_suara = sum(perolehan.values())
    print(f"\nTotal suara masuk: {total_suara}")

    if not perolehan:
        print("Belum ada kandidat untuk menentukan pemenang.")
    else:
        suara_tertinggi = max(perolehan.values())
        pemenang = [nama for nama, jumlah in perolehan.items()
                    if jumlah == suara_tertinggi]

        if len(pemenang) > 1:
            print("Hasil SERI antara: " + ", ".join(pemenang))
            print("Perlu dilakukan pemilihan ulang!")
        else:
            print(f"PEMENANG: {pemenang[0]} dengan {suara_tertinggi} suara!")
    print("=" * 40)


def main():
    kandidat_set = set()  # set mencegah kandidat ganda
    rekap_suara = {}  # format: nama_pemilih_lower: kandidat

    print("=" * 40)
    print("SISTEM PEMILIHAN KETUA KELAS")
    print("=" * 40)

    print("\n--- FASE PENDAFTARAN KANDIDAT ---")
    while True:
        nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ").strip()
        if not nama:
            break
        daftar_kandidat(kandidat_set, nama)

    while len(kandidat_set) < 2:
        print("Minimal harus ada 2 kandidat. Silakan daftarkan kandidat lagi.")
        nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ").strip()
        if not nama:
            print("Pendaftaran belum memenuhi syarat. Program dihentikan.")
            return
        daftar_kandidat(kandidat_set, nama)

    print(f"\nKandidat terdaftar: {kandidat_set}")
    print("\n--- FASE PEMUNGUTAN SUARA ---")

    while True:
        nama_pemilih = input("\nNama pemilih (kosongkan untuk selesai): ").strip()
        if not nama_pemilih:
            break

        print(f"Kandidat yang tersedia: {kandidat_set}")
        pilihan = input("Pilih kandidat: ").strip()
        berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan)

    tampilkan_hasil(hitung_suara(rekap_suara, kandidat_set))


if __name__ == "__main__":
    main()
