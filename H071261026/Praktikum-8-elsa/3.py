import re

print("==== Pembersih Data Nomor Telpon ====")


jumlah_data = int(input("Masukkan jumlah data: "))

data_awal = []
data_bersih = []
nomor_valid = []

for i in range(jumlah_data):
    nomor = input(f"Nomor ke-{i+1}: ")
    data_awal.append(nomor)

print("\n=== Hasil Pembersihan ===")

for i, nomor in enumerate(data_awal):
    bersih = re.sub(r"[\s-]", "", nomor)

    if re.fullmatch(r"\d{10,13}", bersih):
        status = "Valid"
        nomor_valid.append(bersih)
    else:
        status = "Tidak valid"

    data_bersih.append(bersih)

    print(f"\nData {i+1}:")
    print(f"Sebelum : {nomor}")
    print(f"Sesudah : {bersih}")
    print(f"Status  : {status}")

print(f"\nJumlah nomor valid: {len(nomor_valid)}")