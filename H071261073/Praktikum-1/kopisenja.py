menu =["Kopi Susu", "Matcha Latte","Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]
biaya_operasional = 15000
#langkah 1 sub-total
sub_kopi = harga[0] * jumlah[0]
sub_matcha = harga[1] * jumlah[1]
sub_americano = harga[2] * jumlah[2]
#langkah 2 masukan sub-total ke dalam list
subtotal_pendapatan = [sub_kopi, sub_matcha,  sub_americano]
#langkah 3 total dan bersih
# total_seluruh = subtotal_pendapatan[0] + subtotal_pendapatan[1] + subtotal_pendapatan[2]
total_seluruh = sum(subtotal_pendapatan)
pendapatan_bersih = total_seluruh - biaya_operasional
#langkah 4 cek target
total_barang = jumlah[0] + jumlah[1] + jumlah[2]
target_tercapai = total_seluruh > 200000 and total_barang > 10
#output
print(f"Subtotal Kopi Susu: Rp{sub_kopi}")
print(f"Subtotal Matcha Latte: Rp{sub_matcha}")
print(f"Subtotal Americano: Rp{sub_americano}")
print(f"Total Pendapatan: Rp{total_seluruh}")
print(f"Pendapatan Bersih: Rp{pendapatan_bersih}")
print(f"Total Barang Terjual: {total_barang}")
print(f"Target Tercapai: {target_tercapai}")
