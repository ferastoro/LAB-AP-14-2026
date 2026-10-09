alfabet = "abcdefghijklmnopqrstuvwxyz"

def cek_sandi(karakter, k):
    if karakter.lower() not in alfabet:
        return karakter
    posisi = alfabet.find(karakter.lower())
    baru = alfabet[(posisi + k) % 26]
    return baru.upper() if karakter.isupper() else baru

def mesin_enkripsi(teks , k):
    hasil = ""
    for karakter in teks:
        hasil += cek_sandi(karakter, k)
    return hasil

def mesin_dekripsi(teks, k):
    return mesin_enkripsi(teks, -k)

def retas_sandi(sandi, kata_kunci):
    hasil = []

    for k in range(26):
        pesan = mesin_dekripsi(sandi, k)
        if kata_kunci.lower() in pesan.lower():
            hasil.append((k, pesan))
    return hasil

sandi = input("masukkan sandi: ")
kata = input("masukkan kata kunci: ")
print(retas_sandi(sandi, kata))
