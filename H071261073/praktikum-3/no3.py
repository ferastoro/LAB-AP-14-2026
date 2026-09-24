while True:
    try:
        kursi = int(input("masukkan maksimal kursi bus: "))

        if kursi <= 0:
            print("jumlah kursi harus lebih dari 0!")
            continue
        break

    except ValueError:
        print("input jumlah harus berupa angka! ")

total_pendapatan = 0
sisa_kursi = kursi

print("--- sistem reservasi PO BUS dimulai ---")

while sisa_kursi > 0:
    print(f"\nsisa kursi: {sisa_kursi}")

    try:
        umur = int(input("masukkan umur penumpang: "))

        if umur < 0:
            print("umur tidak valid!")
            continue

        if umur <= 5:
            harga = 0
            print("kategori: balita - tiket gratis (Rp 0)")

        elif umur <= 12:
            harga = 50000
            print("kategori: anak - harga: Rp 50.000")

        else:
            harga = 100000
            print("kategori: dewasa - harga: Rp 100.000")


        total_pendapatan += harga
        sisa_kursi -= 1

    except ValueError:
        print("input umur harus berupa angka! ")

print("--- semua kursi terisi ---")
print(f"total pendapatan perjalanan PO BUS kali ini: Rp {total_pendapatan}")