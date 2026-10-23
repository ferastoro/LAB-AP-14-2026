
import datetime
import random
import os


# KONFIGURASI
FOLDER_INVOICE = "invoices"
FILE_HISTORY = "trx_history.txt"
LEBAR = 76


# FUNGSI MENYIAPKAN FOLDER

def siapkan_folder():
    os.makedirs(FOLDER_INVOICE, exist_ok=True)


# FUNGSI FORMAT RUPIAH

def format_rupiah(nominal):
    return f"Rp{nominal:,}".replace(",", ".")


# FUNGSI VALIDASI INPUT ANGKA

def input_positif(pesan):
    while True:
        try:
            nilai = int(input(pesan))

            if nilai <= 0:
                print("Input harus lebih dari 0.")
                continue

            return nilai

        except ValueError:
            print("Input harus berupa bilangan bulat.")


# FUNGSI MEMBUAT ID TRANSAKSI

def buat_id_transaksi(nama_kasir, waktu):
    inisial = "".join(
        kata[0] for kata in nama_kasir.split()
    ).upper()

    bagian_waktu = waktu.strftime("%y%m%d%H%M")

    while True:
        angka_acak = random.randint(100, 999)
        id_transaksi = inisial + bagian_waktu + str(angka_acak)
        nama_file = id_transaksi + ".txt"
        path_file = os.path.join(FOLDER_INVOICE, nama_file)

        if not os.path.exists(path_file):
            return id_transaksi, path_file


# FUNGSI MEMBUAT INVOICE

def buat_invoice(nama_kasir, waktu, id_transaksi, produk,
                 total_nominal_transaksi):

    nama_file = id_transaksi + ".txt"
    path_file = os.path.join(FOLDER_INVOICE, nama_file)

    try:
        with open(path_file, "x") as file:
            file.write("TOKO NABILA".center(LEBAR) + "\n")
            file.write("=" * LEBAR + "\n")
            file.write(f"Nama Kasir      : {nama_kasir}\n")
            file.write(
                "Waktu Transaksi : "
                f"{waktu.strftime('%d/%m/%y %H:%M:%S')}\n"
            )
            file.write(f"ID Transaksi    : {id_transaksi}\n")
            file.write("=" * LEBAR + "\n\n")
            file.write("DAFTAR PRODUK".center(LEBAR) + "\n\n")

            file.write("-" * LEBAR + "\n")
            file.write(
                f"| {'Nama Produk':<28} | {'Harga':>12} | "
                f"{'Jumlah':>6} | {'Subtotal':>14} |\n"
            )
            file.write("-" * LEBAR + "\n")

            for item in produk:
                nama = item["nama"][:28]

                file.write(
                    f"| {nama:<28} | "
                    f"{format_rupiah(item['harga']):>12} | "
                    f"{item['jumlah']:>6} | "
                    f"{format_rupiah(item['subtotal']):>14} |\n"
                )

            file.write("-" * LEBAR + "\n")
            file.write(
                f"| {'TOTAL TRANSAKSI':<50} | "
                f"{format_rupiah(total_nominal_transaksi):>18} |\n"
            )
            file.write("=" * LEBAR + "\n\n")
            file.write(
                "TERIMA KASIH TELAH BERBELANJA".center(LEBAR) + "\n"
            )

        return path_file

    except OSError as error:
        print(f"Gagal menyimpan invoice: {error}")
        return None


# FUNGSI MENYIAPKAN RIWAYAT TRANSAKSI

def siapkan_riwayat():
    if not os.path.exists(FILE_HISTORY):
        try:
            with open(FILE_HISTORY, "w") as file:
                file.write("RIWAYAT TRANSAKSI".center(LEBAR) + "\n")
                file.write("=" * LEBAR + "\n")
                file.write(
                    f"| {'Waktu':<19} | "
                    f"{'ID Transaksi':<25} | "
                    f"{'Nominal Transaksi':>23} |\n"
                )
                file.write("=" * LEBAR + "\n")

        except OSError as error:
            print(f"Gagal membuat file riwayat: {error}")


# FUNGSI MENCATAT RIWAYAT TRANSAKSI

def catat_riwayat(waktu, id_transaksi, nominal):
    try:
        with open(FILE_HISTORY, "a") as file:
            file.write(
                f"| {waktu.strftime('%Y-%m-%d %H:%M:%S'):<19} | "
                f"{id_transaksi:<25} | "
                f"{format_rupiah(nominal):>23} |\n"
            )
            file.write("=" * LEBAR + "\n")

        return True

    except OSError as error:
        print(f"Gagal mencatat riwayat transaksi: {error}")
        return False


# MENU 1: TRANSAKSI BARU

def transaksi_baru():
    print("\n" + "=" * 35)
    print("         TRANSAKSI BARU")
    print("=" * 35)

    nama_kasir = input("Masukkan nama kasir: ").strip()

    if not nama_kasir:
        print("Nama kasir tidak boleh kosong.")
        return

    produk = []
    total_nominal_transaksi = 0

    while True:
        print("\nMasukkan detail produk.")
        nama_produk = input("Nama produk: ").strip()

        if not nama_produk:
            print("Nama produk tidak boleh kosong.")
            continue

        harga_produk = input_positif("Harga produk: Rp")
        jumlah_produk = input_positif("Jumlah produk: ")

        subtotal = harga_produk * jumlah_produk
        total_nominal_transaksi += subtotal

        produk.append({
            "nama": nama_produk,
            "harga": harga_produk,
            "jumlah": jumlah_produk,
            "subtotal": subtotal
        })

        print(f"Subtotal produk: {format_rupiah(subtotal)}")

        tambah = input("Tambah produk lain? (y/n): ").strip().lower()

        while tambah not in ("y", "n"):
            tambah = input("Masukkan y atau n: ").strip().lower()

        if tambah == "n":
            break

    waktu = datetime.datetime.now()
    id_transaksi, path_file = buat_id_transaksi(nama_kasir, waktu)

    hasil_invoice = buat_invoice(
        nama_kasir,
        waktu,
        id_transaksi,
        produk,
        total_nominal_transaksi
    )

    if hasil_invoice is None:
        print("Transaksi belum berhasil disimpan.")
        return

    berhasil_riwayat = catat_riwayat(
        waktu, id_transaksi, total_nominal_transaksi
    )

    print("\n" + "=" * 35)
    print("TRANSAKSI BERHASIL")
    print("=" * 35)
    print(f"ID Transaksi : {id_transaksi}")
    print(f"Total        : {format_rupiah(total_nominal_transaksi)}")
    print(f"Invoice      : {path_file}")

    if berhasil_riwayat:
        print("Riwayat      : berhasil dicatat")
    else:
        print("Peringatan   : riwayat belum tercatat")

    print("=" * 35)


# MENU 2: CARI INVOICE

def cari_invoice():
    print("\n" + "=" * 35)
    print("         CARI TRANSAKSI")
    print("=" * 35)

    id_dicari = input(
        "Masukkan ID transaksi (tanpa .txt): "
    ).strip()

    if not id_dicari:
        print("ID transaksi tidak boleh kosong.")
        return

    if (
        os.path.basename(id_dicari) != id_dicari
        or "/" in id_dicari
        or "\\" in id_dicari
        or id_dicari.lower().endswith(".txt")
    ):
        print("Masukkan ID transaksi saja, tanpa path atau .txt.")
        return

    nama_file = id_dicari + ".txt"
    path_file = os.path.join(FOLDER_INVOICE, nama_file)

    if not os.path.isfile(path_file):
        print("Transaksi tidak ditemukan.")
        return

    try:
        with open(path_file, "r") as file:
            isi_invoice = file.read()

        print("\n" + isi_invoice)

    except OSError as error:
        print(f"Gagal membaca invoice: {error}")


# MENU UTAMA

def main():
    siapkan_folder()
    siapkan_riwayat()

    while True:
        print("\n" + "=" * 35)
        print("       APLIKASI KASIR")
        print("=" * 35)
        print("1. Transaksi baru")
        print("2. Cari transaksi")
        print("3. Keluar")
        print("=" * 35)

        pilihan = input("Masukkan opsi pilihan: ").strip()

        if pilihan == "1":
            transaksi_baru()

        elif pilihan == "2":
            cari_invoice()

        elif pilihan == "3":
            print("Terima kasih telah menggunakan aplikasi kasir.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")


main()
