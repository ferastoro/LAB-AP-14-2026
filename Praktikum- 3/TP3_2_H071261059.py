print("--- Setup Denah Bioskop NontonYuk ---")

while True:
    try:
        n_baris = int(input("Masukkan jumlah baris: "))
        if n_baris <= 0:
            print("Jumlah baris harus lebih dari 0!\n")
            continue
        break
    except:
        print("Input baris harus berupa angka!\n")

while True:
    try:
        m_kursi = int(input("Masukkan jumlah kursi per baris: "))
        if m_kursi <= 0:
            print("Jumlah kursi harus lebih dari 0!\n")
            continue
        break
    except:
        print("Input kursi harus berupa angka!\n")

print("\n--- Daftar Kursi Tersedia ---")
for baris in range(1, n_baris + 1):
    for kursi in range(1, m_kursi + 1):
        if kursi == 13:
            continue

        if baris == 1 and kursi % 2 == 0:
            continue

        print(f"Baris {baris} - Kursi {kursi}")