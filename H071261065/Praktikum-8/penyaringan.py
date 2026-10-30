import re


def validasi_username(username):
    return re.fullmatch(r"[A-Za-z][A-Za-z0-9_]{4,11}", username) is not None


def main():
    username_valid = []

    print("=== Registrasi Username ===")
    print("Ketik 'SELESAI' untuk mengakhiri.\n")

    while True:
        username = input("Masukkan username: ").strip()

        if username == "SELESAI":
            break

        if validasi_username(username):
            print("Username tersedia.")
            username_valid.append(username)
        else:
            print("Username tidak valid!")

        print()

    print("=== Rekapitulasi ===")
    print("Username valid:")

    if username_valid:
        for nomor, username in enumerate(username_valid, start=1):
            print(f"{nomor}. {username}")
    else:
        print("Tidak ada username valid.")

    print(f"\nJumlah username valid: {len(username_valid)}")


if __name__ == "__main__":
    main()
