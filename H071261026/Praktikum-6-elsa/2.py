def daftar_kandidat(kandidat_set, nama):
    kandidat_set.add(nama.capitalize())


def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    pemilih = nama_pemilih.lower()
    pilihan = pilihan.capitalize()

    if pemilih in rekap_suara:
        print("Pemilih sudah memilih!")
    elif pilihan not in kandidat_set:
        print("Kandidat tidak ditemukan!")
    else:
        rekap_suara[pemilih] = pilihan
        print("Suara berhasil dicatat!")


def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {}

    for kandidat in kandidat_set:
        perolehan[kandidat] = 0

    for pilihan in rekap_suara.values():
        perolehan[pilihan] += 1

    return perolehan


def tampilkan_hasil(perolehan):
    for kandidat, suara in perolehan.items():
        print(kandidat, ":", suara, "suara")

    if perolehan:
        tertinggi = max(perolehan.values())
        pemenang = []

        for kandidat, suara in perolehan.items():
            if suara == tertinggi:
                pemenang.append(kandidat)

        if len(pemenang) > 1:
            print("Hasil seri! Perlu pemilihan ulang.")
        else:
            print("Pemenang:", pemenang[0])


kandidat_set = set()
rekap_suara = {}

while True:
    nama = input("Nama kandidat (kosong untuk selesai): ")

    if nama == "":
        break

    daftar_kandidat(kandidat_set, nama)

if len(kandidat_set) < 2:
    print("Minimal harus ada 2 kandidat.")
else:
    while True:
        nama = input("Nama pemilih (kosong untuk selesai): ")

        if nama == "":
            break

        print("Kandidat tersedia:", kandidat_set)
        pilihan = input("Pilih kandidat: ")
        berikan_suara(rekap_suara, kandidat_set, nama, pilihan)

    hasil = hitung_suara(rekap_suara, kandidat_set)
    tampilkan_hasil(hasil)
    print("Total suara masuk: ", len(rekap_suara))