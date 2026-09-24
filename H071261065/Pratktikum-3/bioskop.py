# Sistem Denah Bioskop NontonYuk

print("--- Setup Denah Bioskop NontonYuk ---")


# input jumlah baris
while True:
    try:
        input_baris = input("Masukkan jumlah baris: ")

        if input_baris == "":
            print("Input baris harus berupa angka!")
            print()
            continue

        N = int(input_baris)

        if N <= 0:
            print("Jumlah baris harus lebih dari 0!")
            print()
            continue

        if N > 100:
            print("Jumlah baris maksimal 100!")
            print()
            continue

        break

    except ValueError:
        print("Input baris harus berupa angka!")
        print()


# input jumlah kursi setiap baris
while True:
    try:
        input_kursi = input("Masukkan jumlah kursi per baris: ")

        if input_kursi == "":
            print("Input kursi harus berupa angka!")
            print()
            continue

        M = int(input_kursi)

        if M <= 0:
            print("Jumlah kursi harus lebih dari 0!")
            print()
            continue

        # batas untuk mencegah input terlalu besar
        if M > 100:
            print("Jumlah kursi maksimal 100!")
            print()
            continue

        break

    except ValueError:
        print("Input kursi harus berupa angka!")
        print()


# menampilkan daftar kursi
print()
print("--- Daftar Kursi Tersedia ---")

for baris in range(1, N + 1):

    for kursi in range(1, M + 1):

        # kursi nomor 13 tidak tersedia
        if kursi == 13:
            continue

        # Baris 1 hanya menyediakan kursi ganjil
        if baris == 1 and kursi % 2 == 0:
            continue

        print(f"Baris {baris} - Kursi {kursi}")