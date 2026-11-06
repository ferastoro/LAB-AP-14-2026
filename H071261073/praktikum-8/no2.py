import re 
def validasi_username(username):
    pola = r"[A-Za-z][A-Za-z0-9_]{4,11}"
    return re.match(pola, username)is not None
username_valid = []
print("=== Registrasi Username ===")
print("ketik 'selesai' untuk mengakhiri")

while True:
    username = input("\nmasukkan username: ")
    if username == "selesai":
        break
    if validasi_username(username):
        print("username tersedia.")
        username_valid.append(username)
    else:
        print("username tidak valid")
print("\n=== rekapitulasi ===")
print("username valid:")

for nomor, username in enumerate(username_valid, start=1):
    print(f"{nomor}. {username}")
print("\njumlah username valid:", len(username_valid))