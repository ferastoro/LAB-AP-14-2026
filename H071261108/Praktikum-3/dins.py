print("=== Rekapitulasi Transaksi Dins Store ===")
print("Ketik '0' untuk menutup toko dan mengakhiri sesi.")

while True:
    try:
        jumlah = int(input("\nMasukkan jumlah item: "))

        if jumlah == 0:
            print("Toko ditutup. Sesi rekap selesai.")
            break

        if jumlah < 0:
            print("Jumlah tidak boleh negatif")
            continue

        if jumlah > 100:
            print("Maksimal 100 item per transaksi!")
            continue

        print(f"Transaksi {jumlah} item berhasil!")

    except ValueError:
        print("Input harus berupa angka!")
