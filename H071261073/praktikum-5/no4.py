def deteksi_anomali_email(email, daftar):
    error = []

    if email.count('@') != 1:
        error.append("harus memiliki tepat satu karakter@.")
        return error


    bagian = email.split("@")
    local = bagian[0]
    domain = bagian[1]

    if local == "" or domain == "":
        error.append("bagian local atau domain tidak boleh kosong")

    if " " in email:
        error.append("tidak boleh ada spasi")

    if local != "":
        if local[0] == "." or local[-1] == ".":
            error.append("bagian local tidak boleh diawali atau diakhiri dengan titik")
        if ".." in local:
            error.append("bagian local tidak boleh mengandung titik berturut-turut")

    if domain != "":
        if "." not in domain:
            error.append("bagian domain harus mengandung setidaknya satu titik")
        if ". ." in domain:
            error.append("bagian domain tidak boleh mengandung titik berturut-turut")
        if domain[-1] == ".":
            error.append("bagian domain tidak boleh diakhiri dengan titik")

    if email.lower() in daftar:
        error.append("email sudah terdaftar (DUPLIKAT)")

    if not (domain.endswith(".com") or
            domain.endswith(".id") or
            domain.endswith(".ac.id")):
        error.append("wajib berakhiran dengan .com, .id, atau .ac.id")

    return error

def cetak_daftar(daftar, border):
    if not daftar:
        return ""
    panjang = max(map(len, daftar))
    garis = border * (panjang + 4)
    hasil = garis + "\n"
    for email in daftar:
        hasil += "| " + email.ljust(panjang) + " |\n" 
    return hasil + garis

valid = []
print("--- sistem pencatatan email ---")
border = input("masukkan border dengan karaker bebas: ")
print("Ketik 'tutup' untuk keluar dari program")

while True:

    # border = input("masukkan border dengan karaker bebas: ")

    email = input("masukkan email: ")
    if email.lower() == "tutup":
        break
    error = deteksi_anomali_email(email, valid)
    if not error:
        print("email VALID")
        valid.append(email.lower())
    else:
        print(">> Email DITOLAK karena:")
        for e in error:
            print("-", e)

print(cetak_daftar(valid, border))