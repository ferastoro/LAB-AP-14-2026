import os
import random
from datetime import datetime


def buat_invoice():
  # Membuat folder 'invoices' jika belum ada
  if not os.path.exists("invoices"):
    os.makedirs("invoices")

  nama_kasir = input("Masukkan Nama Kasir: ").strip()

  # Mengambil inisial nama kasir dalam huruf kapital
  inisial_kasir = "".join([word[0].upper() for word in nama_kasir.split()])
  if not inisial_kasir:
    inisial_kasir = "KSR"

  # Mengambil komponen waktu untuk ID transaksi[cite: 1]
  now = datetime.now()
  tahun = now.strftime("%y")  # Dua digit tahun[cite: 1]
  bulan = now.strftime("%m")  # Dua digit bulan[cite: 1]
  tanggal = now.strftime("%d")  # Dua digit tanggal[cite: 1]
  waktu_hm = now.strftime("%H%M")  # Empat digit jam dan menit[cite: 1]
  waktu_lengkap = now.strftime("%Y-%m-%d %H:%M:%S")

  # Tiga digit angka acak antara 100 sampai 999[cite: 1]
  angka_acak = str(random.randint(100, 999))

  # Menggabungkan komponen menjadi ID Transaksi tanpa spasi[cite: 1]
  id_transaksi = (
      f"{inisial_kasir}{tahun}{bulan}{tanggal}{waktu_hm}{angka_acak}"
  )

  daftar_belanja = []
  total_nominal = 0

  print("\n--- Input Produk ---")
  while True:
    nama_produk = input('Nama Produk (ketik "selesai" untuk berhenti): ')
    if nama_produk.lower() == "selesai":
      break
    try:
      harga_produk = float(input("Harga Produk: "))
      jumlah_produk = int(input("Jumlah Produk: "))
      subtotal = harga_produk * jumlah_produk
      total_nominal += subtotal
      daftar_belanja.append({
          "nama": nama_produk,
          "harga": harga_produk,
          "jumlah": jumlah_produk,
          "subtotal": subtotal,
      })
    except ValueError:
      print("Input harga atau jumlah tidak valid. Silakan coba lagi.")

    lanjut = input("Tambah produk lain? (y/n): ")
    if lanjut.lower() != "y":
      break

  if not daftar_belanja:
    print("Transaksi dibatalkan karena tidak ada produk yang diinput.")
    return

  # Menyusun isi teks invoice
  isi_invoice = "=" * 40 + "\n"
  isi_invoice += "               STRUK BELANJA              \n"
  isi_invoice += "=" * 40 + "\n"
  isi_invoice += f"ID Transaksi : {id_transaksi}\n"
  isi_invoice += f"Waktu        : {waktu_lengkap}\n"
  isi_invoice += f"Kasir        : {nama_kasir}\n"
  isi_invoice += "-" * 40 + "\n"
  for item in daftar_belanja:
    isi_invoice += (
        f"{item['nama']} ({item['jumlah']}x) @ Rp"
        f" {item['harga']:,.0f} = Rp {item['subtotal']:,.0f}\n"
    )
  isi_invoice += "-" * 40 + "\n"
  isi_invoice += f"Total Nominal: Rp {total_nominal:,.0f}\n"
  isi_invoice += "=" * 40 + "\n"

  # Menyimpan file invoice ke dalam folder 'invoices'[cite: 1, 2]
  file_path = os.path.join("invoices", f"{id_transaksi}.txt")
  with open(file_path, "w", encoding="utf-8") as f:
    f.write(isi_invoice)

  # Mencatat riwayat transaksi ke trx_history.txt
  history_path = "trx_history.txt"
  file_exists = os.path.exists(history_path)

  with open(history_path, "a", encoding="utf-8") as f:
    if not file_exists:
      f.write(
          "=" * 67 + "\n"
          f"| {'Waktu':<19} | {'ID Transaksi':<16} | {'Nominal Transaksi':<17}"
          " |\n"
          + "=" * 67 + "\n"
      )
    f.write(
        f"| {waktu_lengkap} | {id_transaksi} | Rp. {int(total_nominal):<13} |\n"
        + "=" * 67 + "\n"
    )

  print(f"\nTransaksi Berhasil! File invoice disimpan: {id_transaksi}.txt[cite: 1, 2]")
  print(isi_invoice)


def cari_invoice():
  # Kasir memasukkan ID transaksi saja
  id_cari = input("Masukkan ID Transaksi yang dicari: ").strip()
  file_path = os.path.join("invoices", f"{id_cari}.txt")

  # Mencari file invoice di folder invoices[cite: 2]
  if os.path.exists(file_path):
    print(f"\n--- Invoice Ditemukan: {id_cari} ---")
    with open(file_path, "r", encoding="utf-8") as f:
      print(f.read())  # Ditampilkan di terminal tanpa dicetak ulang[cite: 2]
  else:
    print(f'\nInvoice dengan ID "{id_cari}" tidak ditemukan di folder invoices.')


def lihat_riwayat():
  history_path = "trx_history.txt"
  if os.path.exists(history_path):
    print("\n--- Riwayat Transaksi (trx_history.txt) ---[cite: 2]")
    with open(history_path, "r", encoding="utf-8") as f:
      print(f.read())
  else:
    print("\nBelum ada riwayat transaksi yang tercatat.")


def main():
  while True:
    print("\n=== APLIKASI KASIR SEDERHANA ===")
    print("1. Buat Transaksi Baru & Cetak Invoice[cite: 1]")
    print("2. Cari & Tampilkan Invoice[cite: 2]")
    print("3. Lihat Riwayat Transaksi[cite: 2]")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ").strip()

    if pilihan == "1":
      buat_invoice()
    elif pilihan == "2":
      cari_invoice()
    elif pilihan == "3":
      lihat_riwayat()
    elif pilihan == "4":
      print("Terima kasih telah menggunakan aplikasi kasir!")
      break
    else:
      print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
  main()