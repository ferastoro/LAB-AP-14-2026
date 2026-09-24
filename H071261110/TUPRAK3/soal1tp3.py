print("Recap Transaksi Dins Store")
print("Ketik '0' untuk menutup toko dan mengakhiri sesi.")

while True:
    input_str = input("Masukkan jumlah item: ")
    
    # Validasi input berupa angka bulat
    try:
        jumlah = int(input_str)
    except ValueError:
        print("Input harus berupa angka!")
        continue

    # Pengecekan kondisi sesuai aturan
    if jumlah == 0:
        print("Toko ditutup. Sesi rekap selesai.")
        break
    elif jumlah < 0:
        print("Jumlah tidak boleh negatif")
    elif jumlah > 100:
        print("Maksimal 100 item per transaksi!")
    else:
        print(f"Transaksi {jumlah} item berhasil!")