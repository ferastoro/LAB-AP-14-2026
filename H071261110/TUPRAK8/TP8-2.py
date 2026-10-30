import re


def validasi_username(username):
  # Panjang 5-12 karakter, diawali huruf, hanya huruf/angka/underscore
  pattern = r"^[a-zA-Z][a-zA-Z0-9_]{4,11}$"
  return bool(re.match(pattern, username))


print("=== Registrasi Username ===")
print("Ketik 'SELESAI' untuk mengakhiri.")

username_valid = []

while True:
  username = input("Masukkan username: ")
  if username == "SELESAI":
    break

  if validasi_username(username):
    print("Username tersedia.")
    username_valid.append(username)
  else:
    print("Username tidak valid!")

print("\n=== Rekapitulasi ===")
print("Username valid:")
for i, user in enumerate(username_valid, 1):
  print(f"{i}. {user}")
print(f"Jumlah username valid: {len(username_valid)}")