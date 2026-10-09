alfabet = "abcdefghijklmnopqrstuvwxyz"

def bersihkan_teks(teks):
    hasil = ""
    for karakter in teks:
        if karakter.lower() in alfabet:
            hasil += karakter.lower()
    return hasil

def cek_palindrom(teks):
    teks_balik = "".join(reversed(teks))
    if teks == teks_balik:
        return True, -1
    for i in range(len(teks)):
        if teks[i] != teks_balik[i]:
            return False, i
        # return True, -1

def inti_palindrom(teks):
    teks = bersihkan_teks(teks)
    palindrome_terpanjang = ""
    indeks_terbaik = 0

    for i in range(len(teks)):
        for j in range(i + 1, len(teks) + 1):
            bagian = teks[i:j]
            hasil_cek = cek_palindrom(bagian)
            if hasil_cek[0]:
                if len(bagian) > len(palindrome_terpanjang):
                    palindrome_terpanjang = bagian
                    indeks_terbaik = i
    return { 
        "teks": palindrome_terpanjang,
        "panjang": len(palindrome_terpanjang), 
        "indeks_awal": indeks_terbaik
    }

teks = input("masukkan teks prasasti:")
hasil = inti_palindrom(teks)
print("teks bersih:", bersihkan_teks(teks))
print("output terharap:", hasil)