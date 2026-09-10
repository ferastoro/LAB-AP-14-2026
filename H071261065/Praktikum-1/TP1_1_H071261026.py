# Data penjualan
menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

# Menghitung subtotal setiap minuman
sub_kopi = harga[0] * jumlah[0]
sub_matcha = harga[1] * jumlah[1]
sub_americano = harga[2] * jumlah[2]

# Menyimpan semua subtotal ke dalam list
subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano]

# Menghitung total pendapatan
total_seluruh = sum(subtotal_pendapatan)
 
# Menghitung pendapatan setelah dikurangi biaya operasional
BIAYA_OPERASIONAL = 15000
pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL

# Menghitung total barang yang terjual
total_barang = sum(jumlah)

# Menentukan apakah target penjualan tercapai
target_tercapai = total_seluruh > 200000 and total_barang > 10

# Menampilkan laporan
print("<<<< LAPORAN PENJUALAN KOPI SENJA >>>>")
print(f"Subtotal Kopisusu dan Americano : Rp{sub_kopi + sub_americano}")
print(f"Total Pendapatan : Rp{total_seluruh}")
print(f"Pendapatan Bersih : Rp{pendapatan_bersih}")
print("Jumlah Barang Terjual :", total_barang )
print("Target Tercapai :", target_tercapai)