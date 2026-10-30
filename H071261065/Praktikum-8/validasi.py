import re


def validasi_nim(nim):
    return re.fullmatch(r"H071\d{6}", nim) is not None


def validasi_email(email):
    pola_email = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    return re.fullmatch(pola_email, email) is not None


def validasi_telepon(nomor):
    return re.fullmatch(r"\d{10,13}", nomor) is not None


def main():
    print("=== Validasi Data Mahasiswa ===\n")

    nim = input("Masukkan NIM       : ").strip()
    email = input("Masukkan Email     : ").strip()
    telepon = input("Masukkan No. Telp  : ").strip()

    status_nim = validasi_nim(nim)
    status_email = validasi_email(email)
    status_telepon = validasi_telepon(telepon)

    print("\n--- Hasil Validasi ---")
    print(f"NIM         : {'Valid' if status_nim else 'Format NIM tidak valid!'}")
    print(f"Email       : {'Valid' if status_email else 'Format email tidak valid!'}")
    print(f"No. Telepon : {'Valid' if status_telepon else 'Nomor telepon tidak valid!'}")

    if status_nim and status_email and status_telepon:
        print("\nData mahasiswa berhasil diverifikasi!")


if __name__ == "__main__":
    main()
