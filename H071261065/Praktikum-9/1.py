
class Pemain:
    def __init__(self, nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.nilai_kill = nilai_kill
        self.nilai_assist = nilai_assist
        self.nilai_objective = nilai_objective

    def hitung_skor_akhir(self):
        skor = (0.3 * self.nilai_kill) + (0.3 * self.nilai_assist) + (0.4 * self.nilai_objective)
        return skor

    def status_performa(self):
        if self.hitung_skor_akhir() >= 60:
            return "Unggul"
        else:
            return "Perlu Evaluasi"

    def tampilkan_data(self):
        print(f"| {self.nama:<15} | {self.id_pemain:<12} | {self.role:<12} | {self.nilai_kill:<6} | {self.nilai_assist:<7} | {self.nilai_objective:<10} | {self.hitung_skor_akhir():<10.2f} | {self.status_performa():<16} |")

daftar_pemain = []

jumlah_pemain = int(input("Masukkan jumlah pemain: "))

for i in range(jumlah_pemain):
    print(f"\n---Data Pemain ke-{i + 1}---")

    nama = input("Nama pemain: ")
    id_pemain = input("ID pemain: ")
    role = input("Role pemain: ")
    nilai_kill = float(input("Nilai Kill: "))
    nilai_assist = float(input("Nilai Assist: "))
    nilai_objective = float(input("Nilai Objective: "))

    pemain = Pemain(nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective)

    daftar_pemain.append(pemain)

print("\n" + "=" * 125)
print("                 HASIL PERFORMA PEMAIN GAME KOMPETITIF")
print("=" * 125)

print(f"| {'Nama':<15} | {'ID Pemain':<12} | {'Role':<12} | {'Kill':<6} | {'Assist':<7} | {'Objective':<10} | {'Skor Akhir':<10} | {'Status':<16} |")
print("-" * 125)

for pemain in daftar_pemain:
    pemain.tampilkan_data()

print("=" * 125)
