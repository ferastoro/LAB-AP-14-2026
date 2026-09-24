print("Setup Denah Bioskop")

# Validasi input baris
while True:
    try:
        baris = int(input("Masukkan jumlah baris: "))
        if baris <= 0:
            print("Jumlah baris harus lebih dari 0!")
            continue
        break
    except ValueError:
        print("Input baris harus berupa angka!")

# Validasi input kursi per baris
while True:
    try:
        kursi_per_baris = int(input("Masukkan jumlah kursi per baris: "))
        if kursi_per_baris <= 0:
            print("Jumlah kursi harus lebih dari 0!")
            continue
        break
    except ValueError:
        print("Input kursi harus berupa angka!")

print("\nDaftar Kursi Tersedia")

# Nested loop untuk mencetak kursi
for b in range(1, baris + 1):
    for k in range(1, kursi_per_baris + 1):
        # Aturan Mitos: Kursi 13 dilewati
        if k == 13:
            continue
        
        # Aturan Baris VVIP (Baris 1): Hanya kursi ganjil
        if b == 1:
            if k % 2 != 0:
                print(f"Baris {b} Kursi {k}")
        # Aturan Baris Reguler (Baris 2 dan seterusnya)
        else:
            print(f"Baris {b} Kursi {k}")