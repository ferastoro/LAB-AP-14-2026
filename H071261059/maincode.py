with open("biodata.txt", "w")as file:
    nama = input("masukkan nama: ")
    program_studi =input("masukkan program studi: ")
    file.write(nama + "\n")
    file.write(program_studi)

with open("biodata.txt", "r")as file:
    print(file.read())