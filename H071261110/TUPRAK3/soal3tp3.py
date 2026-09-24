# Validasi input kuota kursi bus
while True:
    try:
        sisa_kursi = int(input("Masukkan maksimal kursi bus: "))
        if sisa_kursi <= 0:
            print("Jumlah kursi harus lebih dari 0!")
            continue
        break
    except ValueError:
        print("Input jumlah kursi harus berupa angka!")

total_pendapatan = 0

print("Sistem Reservasi PO BUS Dimulai")

# Loop masih ada kursi
while sisa_kursi > 0:
    print(f"Sisa kursi: {sisa_kursi}")
    input_umur = input("Masukkan umur penumpang: ")
    
    # Validasi input umur (angka)
    try:
        umur = int(input_umur)
    except ValueError:
        print("Input umur harus berupa angka!")
        continue

    # Validasi umur negatif
    if umur < 0:
        print("Umur tidak valid!")
        continue

    # Penentuan kategori dan harga tiket
    if 0 <= umur <= 5:
        kategori = "Balita"
        harga = 0
        print(f"Kategori: {kategori} Tiket Gratis (Rp 0)")
    elif 6 <= umur <= 12:
        kategori = "Anak"
        harga = 50000
        print(f"Kategori: {kategori} Harga: Rp 50.000")
    else:
        kategori = "Dewasa"
        harga = 100000
        print(f"Kategori: {kategori} Harga: Rp 100.000")

    # Update sisa kursi dan total pendapatan
    sisa_kursi -= 1
    total_pendapatan += harga

print("Semua Kursi Terisi")
print(f"Total pendapatan perjalanan PO BUS kali ini: Rp {total_pendapatan}")