
ALFABET = "abcdefghijklmnopqrstuvwxyz"


def cek_sandi(ch, k):
    huruf = ch.lower()
    posisi = ALFABET.find(huruf)

    # kalau bukan huruf, balikin seperti semula
    if posisi == -1:
        return ch

    # geser huruf sesuai kunci
    hasil = ALFABET[(posisi + k) % 26]

    # kapitalnya tetap dipertahankan
    if ch.isupper():
        return hasil.upper()

    return hasil


def mesin_enkripsi(teks, k):
    hasil = ""

    # proses tiap karakter dalam teks
    for ch in teks:
        hasil += cek_sandi(ch, k)

    return hasil


def mesin_dekripsi(teks, k):
    # dekripsi tinggal geser ke arah sebaliknya
    return mesin_enkripsi(teks, -k)


def retas_sandi(sandi, kata_kunci):
    hasil = []

    # cek kalau kata kunci kosong
    if not kata_kunci or not kata_kunci.strip():
        return hasil

    # coba semua kemungkinan kunci dari 0 sampai 25
    for kunci in range(26):
        pesan_asli = mesin_dekripsi(sandi, kunci)

        # simpan hasil yang mengandung kata kunci
        if kata_kunci.casefold() in pesan_asli.casefold():
            hasil.append((kunci, pesan_asli))

    return hasil


def main():
    sandi = input("Masukkan pesan tersita (enkripsi Caesar): ")
    kata_kunci = input("Masukkan kata kunci target: ")

    # hindari input yang kosong
    if not sandi.strip() or not kata_kunci.strip():
        print("Output Deskripsi: []")
        return

    hasil = retas_sandi(sandi, kata_kunci)
    print("Output Deskripsi:", hasil)


# jalankan program dari sini
if __name__ == "__main__":
    main()
