def daftar_kandidat(kandidat_set, nama):
    nama = nama.strip().capitalize()
    if nama in kandidat_set:
        print(f"'{nama}' sudah terdaftar sebagai kandidat!")
    else:
        kandidat_set.add(nama)
        print(f"'{nama}' berhasil didaftarkan sebagai kandidat!")


def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    nama_asli = nama_pemilih.strip()                 
    kunci = nama_asli.lower()                        
    pilihan = pilihan.strip().capitalize()

    if pilihan not in kandidat_set:
        print(f"Kandidat '{pilihan}' tidak terdaftar! Suara tidak dicatat.")
    elif kunci in rekap_suara:
        print(f"'{nama_asli}' sudah memberikan suara sebelumnya!")
    else:
        rekap_suara[kunci] = pilihan
        print(f"Suara '{nama_asli}' untuk '{pilihan}' berhasil dicatat!")


def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {}
    for kandidat in kandidat_set:
        perolehan[kandidat] = 0
    for pemilih in rekap_suara:
        kandidat = rekap_suara[pemilih]
        perolehan[kandidat] = perolehan[kandidat] + 1
    return perolehan


def tampilkan_hasil(perolehan):
    print("=" * 40)
    print(" HASIL PEMILIHAN KETUA KELAS")
    print("=" * 40)

    total = 0
    tertinggi = 0
    for kandidat in sorted(perolehan):
        suara = perolehan[kandidat]
        print(f" {kandidat}: {suara} suara")
        total = total + suara
        if suara > tertinggi:
            tertinggi = suara
    print(f"Total suara masuk: {total}")

    if total == 0:
        print("Belum ada suara yang masuk, pemenang belum bisa ditentukan.")
    else:
        pemenang = []
        for kandidat in sorted(perolehan):
            if perolehan[kandidat] == tertinggi:
                pemenang.append(kandidat)
        if len(pemenang) > 1:
            daftar_seri = ", ".join(pemenang)        
            print(f"Hasil SERI antara: {daftar_seri}")
            print("Perlu dilakukan pemilihan ulang!")
        else:
            print(f"PEMENANG: {pemenang[0]} dengan {tertinggi} suara!")
    print("=" * 40)


kandidat_set = set()
rekap_suara = {}

print("=" * 40)
print(" SISTEM PEMILIHAN KETUA KELAS")
print("=" * 40)

print("--- FASE PENDAFTARAN KANDIDAT ---")
while True:
    nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ").strip()
    if nama == "":
        if len(kandidat_set) < 2:
            print(f"Minimal harus ada 2 kandidat! Saat ini baru {len(kandidat_set)}.")
        else:
            break
    else:
        daftar_kandidat(kandidat_set, nama)
print(f"Kandidat terdaftar: {kandidat_set}")

print()
print("--- FASE PEMUNGUTAN SUARA ---")
while True:
    nama_pemilih = input("Nama pemilih (kosongkan untuk selesai): ").strip()
    if nama_pemilih == "":
        break
    print(f"Kandidat yang tersedia: {kandidat_set}")
    pilihan = input("Pilih kandidat: ").strip()
    berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan)

perolehan = hitung_suara(rekap_suara, kandidat_set)
tampilkan_hasil(perolehan)