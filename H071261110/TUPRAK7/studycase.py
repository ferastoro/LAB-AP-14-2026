nama = input("Masukkan Nama: ")
jurusan = input("Masukkan Jurusan: ")

with open("biodata.txt", "w") as f:
    f.write (f"{nama}\n")
    f.write (f"{jurusan}\n")

print("Data Tersimpan")