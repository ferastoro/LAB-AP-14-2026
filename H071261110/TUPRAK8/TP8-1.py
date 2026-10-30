import re


def validasi_nim(nim):
  return bool(re.match(r"^H071\d{6}$", nim))


def validasi_email(email):
  return bool(re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email))


def validasi_telp(telp):
  return bool(re.match(r"^\d{10,13}$", telp))


print("=== Validasi Data Mahasiswa ===")
nim = input("Masukkan NIM       : ")
email = input("Masukkan Email     : ")
telp = input("Masukkan No. Telp  : ")

print("\n--- Hasil Validasi ---")
is_nim_valid = validasi_nim(nim)
is_email_valid = validasi_email(email)
is_telp_valid = validasi_telp(telp)

print("NIM        :", "Valid" if is_nim_valid else "Format NIM tidak valid!")
print("Email      :", "Valid" if is_email_valid else "Format email tidak valid!")
print(
    "No. Telepon :",
    "Valid" if is_telp_valid else "Nomor telepon tidak valid!",
)

if is_nim_valid and is_email_valid and is_telp_valid:
  print("\nData mahasiswa berhasil diverifikasi!")