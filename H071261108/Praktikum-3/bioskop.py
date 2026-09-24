print("=== Setup Denah Bioskop NontonYuk ===")

while True:
    try:
        n = int(input("Masukkan jumlah baris: "))

        if n <= 0:
            print("Jumlah baris harus lebih dari 0!")
            continue

        break

    except ValueError:
        print("Input baris harus berupa angka!")


while True:
    try:
        m = int(input("Masukkan jumlah kursi per baris: "))

        if m <= 0:
            print("Jumlah kursi harus lebih dari 0!")
            continue

        break

    except ValueError:
        print("Input kursi harus berupa angka!")


print("\n=== Daftar Kursi Tersedia ===")

for baris in range(1, n + 1):
    for kursi in range(1, m + 1 ):

        # Kursi nomor 13 tidak dijual
        if kursi == 13:
            continue

        # Baris 1 hanya kursi ganjil
        if baris == 1 and kursi % 2 == 0:
            continue

        print(f"Baris {baris} - Kursi {kursi}")
