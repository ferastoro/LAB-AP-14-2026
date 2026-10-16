ALFABET = "abcdefghijklmnopqrstuvwxyz"


def cek_kata(teks, kata):
    indeks = []

    if kata == "":
        return indeks

    teks_kecil = teks.lower()
    kata_kecil = kata.lower()

    mulai = 0

    while mulai < len(teks):
        posisi = teks_kecil.find(kata_kecil, mulai)

        if posisi == -1:
            break

        indeks.append(posisi)

        # lanjut dari karakter setelah posisi sebelumnya
        mulai = posisi + 1

    return indeks


def cek_batas_kata(teks, i, panjang):
    if i < 0 or panjang <= 0 or i + panjang > len(teks):
        return False

    # cek karakter sebelum kata
    if i > 0:
        karakter_sebelum = teks[i - 1].lower()

        if karakter_sebelum in ALFABET:
            return False

    # cek karakter setelah kata
    posisi_setelah = i + panjang

    if posisi_setelah < len(teks):
        karakter_setelah = teks[posisi_setelah].lower()

        if karakter_setelah in ALFABET:
            return False

    return True


def sensor_kata(teks, kata, simbol):
    if kata == "":
        return (teks, 0, [])

    if simbol == "":
        raise ValueError("simbol sensor tidak boleh kosong.")

    indeks_kemunculan = cek_kata(teks, kata)

    hasil = ""
    jumlah_tersensor = 0
    indeks_tersensor = []

    posisi_sekarang = 0
    panjang_kata = len(kata)

    for indeks in indeks_kemunculan:

        # lewati kalau bukan kata utuh
        if not cek_batas_kata(teks, indeks, panjang_kata):
            continue

        # cegah pemrosesan bagian yang tumpang tindih
        if indeks < posisi_sekarang:
            continue

        # masukkan teks sebelum kata target
        hasil += teks[posisi_sekarang:indeks]

        # ganti dengan simbol sebanyak panjang kata
        hasil += simbol * panjang_kata

        jumlah_tersensor += 1
        indeks_tersensor.append(indeks)

        posisi_sekarang = indeks + panjang_kata

    # masukkan sisa teks
    hasil += teks[posisi_sekarang:]

    return (hasil, jumlah_tersensor, indeks_tersensor)


# program utama
teks = input("masukkan teks: ")
kata = input("masukkan kata yang ingin disensor: ")
simbol = input("masukkan simbol sensor: ")

if kata == "":
    print("error: kata target tidak boleh kosong.")
elif simbol == "":
    print("error: simbol sensor tidak boleh kosong.")
else:
    hasil = sensor_kata(teks, kata, simbol)

    print("teks tersensor :", hasil[0])
    print("jumlah sensor  :", hasil[1])
    print("indeks awal    :", hasil[2])