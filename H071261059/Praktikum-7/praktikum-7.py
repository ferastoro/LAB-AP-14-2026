import os
import random
from datetime import datetime

if not os.path.exists("invoices"):
    os.makedirs("invoices")

def buat_transaksi():
    print("\n--- TRANSAKSI BARU ---")
    kasir = input("Masukkan Nama Kasir: ").strip()
    if kasir == "":
        print("Nama kasir tidak boleh kosong!")
        return
    
    inisial = "".join(k[0].upper() for k in kasir.split())

    belanja = []
    total = 0

    while True:
        nama = input("Nama Produk: ")
        try:
            harga = float(input("Harga Produk: "))
            jumlah = int(input("Jumlah Produk: "))
        except ValueError:
            print("Harga atau jumlah harus berupa angka!")
            continue

        subtotal = harga * jumlah
        total += subtotal
        belanja.append((nama, harga, jumlah, subtotal))

        if input("Tambah produk lagi? (y/n): ").strip().lower() != "y":
            break

    waktu = datetime.now()
    id_trx = f"{inisial}{waktu:%y%m%d%H%M}{random.randint(100, 999)}"

    invoice = f"""========================================
             STRUK BELANJA TOKO
========================================
ID Transaksi : {id_trx}
Waktu        : {waktu:%Y-%m-%d %H:%M:%S}
Kasir        : {kasir}
----------------------------------------
DAFTAR BELANJA:
"""
    for nama, harga, jumlah, subtotal in belanja:
        invoice += f"- {nama} ({jumlah}x @Rp{harga:,.0f}) = Rp{subtotal:,.0f}\n"

    invoice += f"""----------------------------------------
TOTAL NOMINAL : Rp{total:,.0f}
========================================
Terima kasih telah berbelanja!
"""

    file_invoice = f"invoices/{id_trx}.txt"
    with open(file_invoice, "w") as f:
        f.write(invoice)

    ada_history = os.path.exists("trx_history.txt")
    with open("trx_history.txt", "a") as f:
        if not ada_history:
            f.write("==================================================================\n")
            f.write(f"| {'Waktu':<19} | {'ID Transaksi':<16} | {'Nominal Transaksi':<17} |\n")
            f.write("==================================================================\n")

        f.write(f"| {waktu:%Y-%m-%d %H:%M:%S} | {id_trx} | {'Rp. ' + str(int(total)):<17} |\n")
        f.write("==================================================================\n")

    print("\n[SUKSES] Transaksi berhasil!")
    print(f"ID Transaksi: {id_trx}")
    print(f"File invoice disimpan di: {file_invoice}")


def cari_invoice():
    print("\n--- CARI INVOICE ---")
    id_cari = input("Masukkan ID Transaksi: ").strip()
    file_invoice = f"invoices/{id_cari}.txt"

    if os.path.exists(file_invoice):
        print(f"\n--- MENAMPILKAN INVOICE: {id_cari} ---")
        with open(file_invoice, "r") as f:
            print(f.read())
    else:
        print(f"\n[GAGAL] Invoice dengan ID '{id_cari}' tidak ditemukan!")


def main():
    while True:
        print("\n==============================")
        print("    APLIKASI KASIR SEDERHANA  ")
        print("==============================")
        print("1. Transaksi Baru (Buat Invoice)")
        print("2. Cari & Tampilkan Invoice")
        print("3. Keluar")

        pilihan = input("Pilih menu (1/2/3): ").strip()

        if pilihan == "1":
            buat_transaksi()
        elif pilihan == "2":
            cari_invoice()
        elif pilihan == "3":
            print("\nTerima kasih telah menggunakan aplikasi kasir!")
            break
        else:
            print("\nPilihan tidak valid. Masukkan angka 1, 2, atau 3.")

main()