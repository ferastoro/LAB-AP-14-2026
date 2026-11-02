import re

print("==== VALIDASI DATA MAHASISWA ====")

def validasi_nim(nim):
    pola = r"^H071\d{6}$"
    if re.match(pola, nim):
        return True
    else:
        return False
    
def validasi_email(email):
    pola = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(pola, email):
        return True
    else:
        return False

def validasi_telepon(telepon):
    pola = r"^\d{10,13}$"
    if re.match(pola, telepon):
        return True
    else:
        return False
    

nim = input("Masukkan NIM: ")
email = input("Masukkan Email: ")
telepon = input("Masukkan Nomor Telepon: ")

if validasi_nim(nim):
    print("NIM valid")
else:
    print("Format NIM tidak valid")

if validasi_email(email):
    print("Email valid")
else:
    print("Format Email tidak valid")

if validasi_telepon(telepon):
    print("Telepon valid")
else:
    print("Nomor Telepon tidak valid! ")
    
if validasi_nim(nim) and validasi_email(email) and validasi_telepon(telepon):
    print("DATA MAHASISWA BERHASIL DIVERIFIKASI")