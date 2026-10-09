alfabet = "abcdefghijklmnopqrstuvwxyz"
def cek_kata(teks, kata):
    hasil = []
    teks = teks.lower()
    kata = kata.lower()
    start = 0

    while True:
        i = teks.find(kata, start)
        if i == -1:
            break
        hasil.append(i)
        start = i + 1
    return hasil

def cek_batas_kata(teks, i, panjang):
    if i > 0 and teks[i - 1].lower() in alfabet:
        return False
    if i + panjang < len(teks) and teks[i + panjang].lower() in alfabet:
        return False
    return True

def sensor_kata(teks, kata, simbol):
    hasil = ""
    akhir = 0
    indeks = []
    for i in cek_kata(teks, kata):
        if cek_batas_kata(teks, i, len(kata)):
            hasil += teks[akhir :i]
            hasil += simbol * len(kata)
            akhir = i + len(kata)
            indeks.append(i)
    hasil += teks[akhir:]
    return hasil, len(indeks), indeks

teks = input("masukkan teks: ")
kata = input("masukkan kata target: ")
simbol = input("masukkan simbol: ")

print(sensor_kata(teks, kata, simbol))