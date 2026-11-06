class Pemain:
    def __init__(self, nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective, level):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.nilai_kill = nilai_kill
        self.nilai_assist = nilai_assist
        self.nilai_objective = nilai_objective
        self.level = level
        
    def hitung_skor_akhir(self):
        skor = (0.3 * self.nilai_kill) + (0.3 * self.nilai_assist) + (0.4 * self.nilai_objective)
        return skor
    
    def status_performa(self):
        if self.hitung_skor_akhir() >= 60:
            return "Unggul"
        else:
            return "Perlu Evaluasi"
        
    def tampilkan_data(self, no):
        print(f"{no:<5} | {self.nama:<12} | {self.id_pemain:<12} | {self.role:<10} | {self.hitung_skor_akhir():<12.2f} | {self.status_performa():<12} | {self.tentukan_level()}")
        
    def tentukan_level(self):
        if self.hitung_skor_akhir >= 85:
            return "Diamond"
        elif self.hitung_skor_akhir >=70:
            return "Platinum"
        elif self.hitung_skor_akhir >= 60:
            return "Gold"
        else:
            return "Bronze"
        
        
daftar_pemain = []

jumlah_data = int(input("Masukkan jumlah pemain: "))

for i in range(jumlah_data):
    print(f"\n Data Pemain ke-{i+1}: ")
    nama = input("Nama: ")
    id_pemain = input("Id Pemain: ")
    role = input("Role: ")
    kill = float(input("Nilai Kill: "))
    assist = float(input("Nilai Assist: "))
    objective = float(input("Nilai Objective: "))
            
    pemain = Pemain(nama, id_pemain, role, kill, assist, objective, level=None)
            
    daftar_pemain.append(pemain)
            
print("\n====== REKAPITULASI PERFORMA PEMAIN ======")
print("=" * 90)

print(f"{'No':<5} | {'Nama':<12} | {'Id Pemain':<12} | {'Role':<12} | {'Skor Akhir':<12} | {'Status'} | {'Level'}")

print("=" * 90)

no = 1

for pemain in daftar_pemain:
    pemain.tampilkan_data(no)
    no += 1
    
print("=" * 90)