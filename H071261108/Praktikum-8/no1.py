import re


def validasi_nim(nim):
    return re.match(r"^H071\d{6}$", nim) is not None


def validasi_email(email):
    return re.match(r"^[A-Za-z0-9]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", email) is not None


def validasi_telepon(telepon):
    return re.match(r"^\d{10,13}$", telepon) is not None


print("=== Validasi Data Mahasiswa ===")

nim = input("Masukkan NIM     : ")
email = input("Masukkan Email   : ")
telepon = input("Masukkan No. Telp: ")

status_nim = validasi_nim(nim)
status_email = validasi_email(email)
status_telepon = validasi_telepon(telepon)

print("\n--- Hasil Validasi ---")

if status_nim:
    print("NIM       : Valid")
else:
    print("NIM       : Format NIM tidak valid!")

if status_email:
    print("Email     : Valid")
else:
    print("Email     : Format email tidak valid!")

if status_telepon:
    print("No. Telepon: Valid")
else:
    print("No. Telepon: Nomor telepon tidak valid!")

if status_nim and status_email and status_telepon:
    print("\nData mahasiswa berhasil diverifikasi!")
