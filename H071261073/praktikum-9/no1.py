
class Pemain:

    def __init__(self, nama, id_pemain, role,
                 nilai_kill, nilai_assist, nilai_objective,level):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.nilai_kill = nilai_kill
        self.nilai_assist = nilai_assist
        self.nilai_objective = nilai_objective
        self.level = level

    def hitung_skor_akhir(self):
        skor = (0.3 * self.nilai_kill) + \
               (0.3 * self.nilai_assist) + \
               (0.4 * self.nilai_objective)
        return skor

    def status_performa(self):
        if self.hitung_skor_akhir() >= 60:
            return "Unggul"
        else:
            return "Perlu Evaluasi"

    def tampilkan_data(self):
        print(f"Nama: {self.nama}")
        print(f"ID Pemain: {self.id_pemain}")
        print(f"Role: {self.role}")
        print(f"Nilai Kill: {self.nilai_kill}")
        print(f"Nilai Assist: {self.nilai_assist}")
        print(f"Nilai Objective: {self.nilai_objective}")
        print(f"Skor Akhir: {self.hitung_skor_akhir():.2f}")
        print(f"Status: {self.status_performa()}")
        print(f"Level: {self.tentukan_level()}")

    def tentukan_level(self):
        skor = self.hitung_skor_akhir()
        if skor >= 85:
            return "Diamond"
        elif skor >= 70:
            return "Platinum"
        elif skor >= 60:
            return "Gold"
        else:
            return "Bronze"


print("=== SISTEM PENILAIAN PERFORMA PEMAIN ===")

daftar_pemain = []

jumlah_pemain = int(input("\nMasukkan jumlah pemain: "))

for i in range(jumlah_pemain):

    print(f"\n-- Data Pemain ke-{i+1} --")

    nama = input("Nama: ")
    id_pemain = input("ID Pemain: ")
    role = input("Role: ")
    nilai_kill = float(input("Nilai Kill: "))
    nilai_assist = float(input("Nilai Assist: "))
    nilai_objective = float(input("Nilai Objective: "))
    level = None
    

    pemain = Pemain(
        nama, id_pemain, role,
        nilai_kill, nilai_assist, nilai_objective, level
    )


    daftar_pemain.append(pemain)




print("\n=== REKAPITULASI PERFORMA PEMAIN ===")

print("=" * 85)
print(f"{'No':<4} {'Nama':<12} {'ID Pemain':<15} {'Role':<12} {'Skor Akhir':<12} {'Status':<18} {'Level':<12}")
print("=" * 85)


for i, pemain in enumerate(daftar_pemain, start=1):
    print(
        f"{i:<4} "
        f"{pemain.nama:<12} "
        f"{pemain.id_pemain:<15} "
        f"{pemain.role:<12} "
        f"{pemain.hitung_skor_akhir():<12.2f} "
        f"{pemain.status_performa():<18}"
        f"{pemain.tentukan_level():<12}"
    )

print("=" * 85)