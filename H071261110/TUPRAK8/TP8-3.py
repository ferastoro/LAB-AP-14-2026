import re

print("=== Pembersihan Data Nomor Telepon ===")
jumlah = int(input("Masukkan jumlah data: "))
data_nomor = []

for i in range(jumlah):
  nomor = input(f"Nomor ke-{i+1}: ")
  data_nomor.append(nomor)

print("\n--- Hasil Pembersihan ---")
valid_count = 0

for i, nomor in enumerate(data_nomor, 1):
  # Membersihkan spasi dan tanda minus menggunakan re.sub()
  sesudah = re.sub(r"[\s-]", "", nomor)

  # Pengecekan validitas (10-13 digit)
  is_valid = bool(re.match(r"^\d{10,13}$", sesudah))

  print(f"Data {i}:")
  print(f"Sebelum: {nomor}")
  print(f"Sesudah: {sesudah}")
  print(f"Status : {'Valid' if is_valid else 'Tidak valid'}\n")

  if is_valid:
    valid_count += 1

print(f"Jumlah nomor valid: {valid_count}")