import re

print("==== Registrasi Username ====")
print("Ketik 'SELESAI' untuk mengakhiri registrasi.")

username_valid = []

def validasi_username(username):
    pola = r"^[A-Za-z][A-Za-z0-9_]{4,11}$"
    return re.match(pola, username) is not None

while True:
    username = input("Masukkan username: ")
    if username == "SELESAI":
        break
    
    if validasi_username(username):
        print("Username tersedia. ")
        username_valid.append(username)
    else:
        print("Username tidak valid!")
        
print("\ndaftar username yang valid: ")
for username in username_valid:
    print(username)
    
print("Jumlah username valid: ",len(username_valid))