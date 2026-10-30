
import re


def bersihkan_nomor(nomor):
    return re.sub(r"[ -]", "", nomor)


def validasi_telepon(nomor):
    return re.fullmatch(r"\d{10,13}", nomor) is not None


def main():
    data_asli = []
    data_bersih = []
    nomor_valid = []

    print("=== Pembersihan Data Nomor Telepon ===")

    while True:
        try:
            jumlah_data = int(input("\nMasukkan jumlah data: "))
            if jumlah_data < 0:
                print("Jumlah data tidak boleh negatif.")
                continue
            break
        except ValueError:
            print("Masukkan jumlah data berupa bilangan bulat.")

    for i in range(1, jumlah_data + 1):
        while True:
            nomor = input(f"\nNomor ke-{i}: ").strip()
            if re.fullmatch(r"[0-9 -]*", nomor):
                break
            print("Input hanya boleh berisi angka, spasi, dan tanda -.")

        nomor_bersih = bersihkan_nomor(nomor)
        data_asli.append(nomor)
        data_bersih.append(nomor_bersih)

        if validasi_telepon(nomor_bersih):
            nomor_valid.append(nomor_bersih)

    print("\n--- Hasil Pembersihan ---")
    for i, (asli, bersih) in enumerate(zip(data_asli, data_bersih), start=1):
        print(f"\nData {i}:")
        print(f"Sebelum : {asli}")
        print(f"Sesudah : {bersih}")
        print(f"Status  : {'Valid' if validasi_telepon(bersih) else 'Tidak valid'}")

    print(f"\nJumlah nomor valid: {len(nomor_valid)}")


if __name__ == "__main__":
    main()
