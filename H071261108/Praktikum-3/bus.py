print("=== Sistem Reservasi PO BUS ===")

while True:
    try:
        maksimal_kursi = int(input("Masukkan maksimal kursi bus: "))

        if maksimal_kursi <= 0:
            print("Jumlah kursi harus lebih dari 0!")
            continue

        break

    except ValueError:
        print("Input jumlah kursi harus berupa angka!")


sisa_kursi = maksimal_kursi
total_pendapatan = 0

print("\n=== Sistem Reservasi PO BUS Dimulai ===")

while sisa_kursi > 0:

    print(f"\nSisa kursi: {sisa_kursi}")

    try:
        umur = int(input("Masukkan umur penumpang: "))

    except ValueError:
        print("Input umur harus berupa angka!")
        continue

    if umur < 0:
        print("Umur tidak valid!")
        continue

    if umur <= 5:
        harga = 0
        kategori = "Tiket Gratis"

    elif umur <= 12:
        harga = 50000
        kategori = "Tiket Anak"

    else:
        harga = 100000
        kategori = "Tiket Dewasa"

    sisa_kursi -= 1
    total_pendapatan += harga

    print(f"Kategori: {kategori} - Harga: Rp {harga:,}".replace(",", "."))


print("\n=== Semua Kursi Terisi ===")
print(
    f"Total pendapatan perjalanan PO BUS kali ini: "
    f"Rp {total_pendapatan:,}".replace(",", ".")
)
