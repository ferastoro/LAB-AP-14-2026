import re 
def validasi_nim(nim):
    return re.match(r"H071\d{6}", nim) is not None
def validasi_email(email):
    return re.match(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",email)is not None
def validasi_telepon(telepon):
    return re.match(r"\d{10,13}",telepon)is not None

print("=== validasi data mahasiswa ===")
nim = input("masukkan NIM    : ")
email = input("masukkan Email   : ")
telepon = input("masukkan No. telpon   : ")

nim_valid = validasi_nim(nim)
email_valid = validasi_email(email)
telepon_valid = validasi_telepon(telepon)

print("\n---hasil validasi---")
print("NIM            :", "Valid" if nim_valid else "tidak valid")
print("Email          :", "Valid" if email_valid else "tidak valid")
print("No. telepon    :", "Valid" if telepon_valid else "tidak valid")

if not nim_valid:
    print("format NIM tidak valid")
if not email_valid:
    print("format email tidak valid")
if not telepon_valid:
    print("nomor telepon tidak valid")
if nim_valid and email_valid and telepon_valid:
    print("data mahasiswa berhasil diverivikasi")

