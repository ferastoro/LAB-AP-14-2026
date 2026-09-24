print("--- setup denah bioskop  NontonYukk ---")

while True:
    try:
        baris = int(input("masukkan jumlah baris: "))

        if baris <= 0:
            print("jumlah baris harus lebih dari 0!")
            continue
        break
    except ValueError:
        print("input baris harus berupa angka!")

while True:
    try:
        kursi = int(input("masukkan jumlah kursi per baris: "))


        if kursi <= 0:
            print("jumlah kursi harus lebih dari 0!")
            continue
        break
    except ValueError:
        ("input kursi harus berupa angka!")

print("\n--- daftar kursi tersedia ---")

for i in range(1, baris + 1):
    for j in range(1, kursi + 1):

        if j == 13:
            continue

        if i == 1:
            if j % 2 == 1:
                print(f"baris {i} - kursi {j}")
        else:
            print(f"baris {i} - kursi {j}")