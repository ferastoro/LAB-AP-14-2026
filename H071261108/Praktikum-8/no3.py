import re


def validasi_telepon(telepon):
    return re.match(r"^\d{10,13}$", telepon) is not None


print("=== Pembersihan Data Nomor Telepon ===")

jumlah_data = int(input("Masukkan jumlah data: "))

data_telepon = []

for i in range(jumlah_data):
    nomor = input(f"\nNomor ke-{i + 1}: ")
    data_telepon.append(nomor)

print("\n--- Hasil Pembersihan ---")

daftar_valid = []

for i, nomor in enumerate(data_telepon, start=1):
    nomor_bersih = re.sub(r"[\s-]", "", nomor)

    if validasi_telepon(nomor_bersih):
        status = "Valid"
        daftar_valid.append(nomor_bersih)
    else:
        status = "Tidak valid"

    print(f"\nData {i}:")
    print("Sebelum :", nomor)
    print("Sesudah :", nomor_bersih)
    print("Status  :", status)

print("\nJumlah nomor valid:", len(daftar_valid))
