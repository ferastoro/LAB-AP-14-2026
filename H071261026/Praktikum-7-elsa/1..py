import os
import random
from datetime import datetime

os.makedirs("invoices", exist_ok=True)

def buat_invoice():
    kasir = input("Masukkan Nama kasir: ")
    inisial = "".join(n[0] for n in kasir.split()).upper()

    waktu = datetime.now()
    id_transaksi = (
        f"{inisial}{waktu:%y%m%d%H%M}{random.randint(100, 999)}"
    )

    daftar_barang = []
    total = 0

    while True:
        nama = input("Masukkan Nama produk: ")
        harga = int(input("Masukkan Harga produk: "))
        jumlah = int(input("Masukkan Jumlah produk: "))

        subtotal = harga * jumlah
        total += subtotal
        daftar_barang.append(
            f"{nama} x{jumlah} = Rp{subtotal}"
        )

        tambah = input("Tambah produk? (y/t): ")
        if tambah.lower() != "y":
            break

    nama_file = f"invoices/{id_transaksi}.txt"

    with open(nama_file, "w") as file:
        file.write(f"Kasir: {kasir}\n")
        file.write(f"ID Transaksi: {id_transaksi}\n")
        file.write("\n".join(daftar_barang))
        file.write(f"\nTotal: Rp{total}\n")

    with open("trx_history.txt", "a") as file:
        file.write(
            f"{waktu:%Y-%m-%d %H:%M:%S} | "
            f"{id_transaksi} | Rp{total}\n"
        )

    print("=== TRANSAKSI BERHASIL ===")
    print("ID transaksi:", id_transaksi)


def cari_invoice():
    nomor = input("Masukkan ID transaksi: ")
    nama_file = f"invoices/{nomor}.txt"

    if os.path.exists(nama_file):
        with open(nama_file, "r") as file:
            print(file.read())
    else:
        print("Transaksi tidak ditemukan.")


while True:
    print("=== APLIKASI KASIR ===")
    print("1. Transaksi Baru")
    print("2. Cari Transaksi")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        buat_invoice()
    elif pilihan == "2":
        cari_invoice()
    elif pilihan == "3":
        print("=== SAMPAI JUMPA ===")
        break
    else:
        print("Pilihan tidak valid.")