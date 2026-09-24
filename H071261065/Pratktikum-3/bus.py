# Sistem Reservasi PO BUS

# input maksimal kursi bus
while True:
    try:
        N = int(input("Masukkan maksimal kursi bus: "))

        if N <= 0:
            print("Jumlah kursi harus lebih dari 0!")
            continue

        break

    except ValueError:
        print("Input jumlah kursi harus berupa angka!")


print()
print("--- Sistem Reservasi PO BUS Dimulai ---")
print()


# variabel
sisa_kursi = N
total_pendapatan = 0


# perulangan selama kursi masih tersedia
while sisa_kursi > 0:

    print(f"Sisa kursi: {sisa_kursi}")

    try:
        umur = int(input("Masukkan umur penumpang: "))

    except ValueError:
        print("Input umur harus berupa angka!")
        print()
        continue

    # validasi umur negatif
    if umur < 0:
        print("Umur tidak valid!")
        print()
        continue

    # validasi umur terlalu tua
    if umur > 100:
        print("Umur tidak valid!")
        print()
        continue

    # menentukan kategori dan harga tiket
    if umur <= 5:
        kategori = "Balita"
        harga = 0

    elif umur <= 12:
        kategori = "Anak"
        harga = 50000

    else:
        kategori = "Dewasa"
        harga = 100000

    # mengurangi jumlah kursi
    sisa_kursi -= 1

    # menambahkan harga ke total pendapatan
    total_pendapatan += harga

    # menampilkan kategori tiket
    if kategori == "Balita":
        print("Kategori: Balita - Tiket Gratis (Rp 0)")

    elif kategori == "Anak":
        print("Kategori: Anak - Harga: Rp 50.000")

    else:
        print("Kategori: Dewasa - Harga: Rp 100.000")

    print()


# semua kursi telah terisi
print("--- Semua Kursi Terisi ---")
print(f"Total pendapatan perjalanan PO BUS kali ini: Rp {total_pendapatan}")