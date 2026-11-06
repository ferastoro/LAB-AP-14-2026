import re
def bersihkan_telepon(telepon):
    return re.sub(r"[ -]", "", telepon)
def validasi_telepon(telepon):
    return re.fullmatch(r"\d{10,13}",telepon)is not None
data_telepon =[]
data_bersih = []
nomor_valid = []
print("=== pembersihan data nomor telepon ===")
jumlah_data = int(input("masukkan jumlah data: "))
    
for i in range(jumlah_data):
    telepon = input(f"nomor ke-{i + 1}: ")
    data_telepon.append(telepon)

    hasil_bersih = bersihkan_telepon(telepon)
    data_bersih.append(hasil_bersih)
    if validasi_telepon(hasil_bersih):
        nomor_valid.append(hasil_bersih)
print("\n---hasil pembersihan---")
for i in range(jumlah_data):
    print(f"\ndata {i + 1}:")
    print("sebelum :", data_telepon[i])
    print("sesudah :", data_bersih[i])
    if validasi_telepon(data_bersih[i]):
        print("status : valid")
    else:
        print("status : tidak valid")
print("\njumlah nomor valid:", len(nomor_valid))