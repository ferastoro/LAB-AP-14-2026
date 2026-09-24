#R

print()
print("--- Sistem Reservasi PO BUS Dimulai ---")
print()

while True:
    try:
        jumlah = int(input("Masukkan jumlah item: "))

        # jika 0, toko ditutup
        if jumlah == 0:
            print("Toko ditutup. Sesi rekap selesai.")
            break

        # tidak boleh negatif
        if jumlah < 0:
            print("Jumlah tidak boleh negatif")
            continue

        # maksimal 100 item
        if jumlah > 100:
            print("Maksimal 100 item per transaksi!")
            continue

        # jika semua valid
        print(f"Transaksi {jumlah} item berhasil!")

    except ValueError:
        print("Input harus berupa angka!")