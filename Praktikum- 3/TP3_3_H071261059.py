
while True:
    try:
        N = int(input("Masukkan maksimal kursi bus: "))
        if N <= 0:
            print("Jumlah kursi harus lebih dari 0!\n")
            continue
        break
    except:
        print("Input jumlah kursi harus berupa angka!\n")

sisa_kursi = N
total_pendapatan = 0

print("\n--- Sistem Reservasi PO BUS Dimulai ---\n")

while sisa_kursi > 0:
    print(f"Sisa kursi: {sisa_kursi}")

    try:
        umur = int(input("Masukkan umur penumpang: "))
    except:
        print("Input umur harus berupa angka!\n")

        continue

    if umur < 0:
        print("Umur tidak valid!\n")
        continue

    if umur <= 5:
        harga = 0
        print("Kategori: Balita - Tiket Gratis (Rp 0)\n")
    elif umur <= 12:
        harga = 50000
        print("Kategori: Anak - Harga: Rp 50.000\n")
    else:
        harga = 100000
        print("Kategori: Dewasa - Harga: Rp 100.000\n")

    total_pendapatan += harga
    sisa_kursi -= 1

print("--- Semua Kursi Terisi ---")
print(f"Total pendapatan perjalanan PO BUS kali ini: Rp {total_pendapatan}")