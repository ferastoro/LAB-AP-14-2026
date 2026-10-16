def deteksi_anomali_email(email, daftar_email_valid=None):
    error = []

    # aturan 1: harus tepat satu @
    jumlah_at = email.count("@")

    if jumlah_at != 1:
        error.append("email harus memiliki tepat satu karakter @.")
        return error

    posisi_at = email.find("@")

    local = email[:posisi_at]
    domain = email[posisi_at + 1:]

    # aturan 2: local dan domain tidak boleh kosong
    if local == "":
        error.append("bagian local sebelum @ tidak boleh kosong.")

    if domain == "":
        error.append("bagian domain setelah @ tidak boleh kosong.")

    # aturan 3: tidak boleh ada spasi
    if " " in email:
        error.append("email tidak boleh mengandung spasi.")

    # aturan 4: validasi bagian local
    if local != "":
        if local[0] == ".":
            error.append("bagian local tidak boleh diawali titik.")

        if local[-1] == ".":
            error.append("bagian local tidak boleh diakhiri titik.")

        if ".." in local:
            error.append("bagian local tidak boleh memiliki titik berurutan.")

    # aturan 5: validasi bagian domain
    if domain != "":
        if "." not in domain:
            error.append("bagian domain harus memiliki minimal satu titik.")

        if ".." in domain:
            error.append("bagian domain tidak boleh memiliki titik berurutan.")

        if domain[-1] == ".":
            error.append("bagian domain tidak boleh diakhiri titik.")

        # domain yang diperbolehkan
        if not domain.lower().endswith((".com", ".id", ".ac.id")):
            error.append(
                "email harus berakhiran .com, .id, atau .ac.id."
            )

    # aturan 6: tidak boleh ada duplikat
    if daftar_email_valid is not None:
        for email_lama in daftar_email_valid:
            if email_lama.lower() == email.lower():
                error.append("email tidak boleh duplikat.")
                break

    return error


def cetak_daftar(daftar_email_valid, karakter_border):
    if len(daftar_email_valid) == 0:
        return "belum ada email valid."

    panjang_terpanjang = 0

    # cari email yang paling panjang
    for email in daftar_email_valid:
        if len(email) > panjang_terpanjang:
            panjang_terpanjang = len(email)

    lebar = panjang_terpanjang + 4
    border = karakter_border * (lebar + 2)

    hasil = ""
    hasil += border + "\n"

    for email in daftar_email_valid:
        jumlah_spasi = panjang_terpanjang - len(email)

        hasil += karakter_border
        hasil += " " + email + (" " * jumlah_spasi) + " "
        hasil += karakter_border
        hasil += "\n"

    hasil += border

    return hasil


# program utama
daftar_email_valid = []

print("=== VALIDASI EMAIL ===")
print("ketik 'tutup' untuk mengakhiri.")

while True:
    email = input("\nmasukkan email: ")

    if email.lower() == "tutup":
        break

    error = deteksi_anomali_email(
        email,
        daftar_email_valid
    )

    if len(error) == 0:
        daftar_email_valid.append(email)

        print("\nemail valid!")
        print(cetak_daftar(daftar_email_valid, "="))

    else:
        print("\nemail tidak valid.")
        print("alasan:")

        for nomor, pesan_error in enumerate(error, start=1):
            print(str(nomor) + ". " + pesan_error)


print("\nprogram selesai.")
print("daftar email valid:")
print(cetak_daftar(daftar_email_valid, "="))