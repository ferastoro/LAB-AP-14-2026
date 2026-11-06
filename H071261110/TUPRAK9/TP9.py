class Pemain:

  def __init__(self, nama, id_pemain, role, kill, assist, objective, level):
    # Menginisialisasi atribut pemain sesuai requirements
    self.nama = nama
    self.id_pemain = id_pemain
    self.level = level
    self.role = role
    self.kill = kill
    self.assist = assist
    self.objective = objective

  def hitung_skor_akhir(self):
    # Menghitung skor performa akhir berdasarkan rumus bobot penilaian[cite: 1]
    skor_akhir = (0.3 * self.kill) + (0.3 * self.assist) + (0.4 * self.objective)
    return skor_akhir

  def status_performa(self):
    # Menentukan status performa berdasarkan skor akhir[cite: 1]
    skor = self.hitung_skor_akhir()
    if skor >= 60:
      return "Unggul"
    else:
      return "Perlu Evaluasi"
    
  def tentukan_level(self):
    # Menentukan level pemain berdasarkan skor akhir
    skor = self.hitung_skor_akhir()
    if skor >= 85:
      return "Diamond"
    elif skor >= 70:
      return "Platinum"
    elif skor >= 60:
      return "Gold"
    else:
          return "Bronze"

  def tampilkan_data(self):
    # Menampilkan informasi detail pemain secara terstruktur
    print(f"Nama: {self.nama}")
    print(f"ID Pemain: {self.id_pemain}")
    print(f"Role: {self.role}")
    print(f"Nilai Kill: {self.kill}")
    print(f"Nilai Assist: {self.assist}")
    print(f"Nilai Objective: {self.objective}")
    print(f"Level: {self.level}")


def main():
  print("=== SISTEM PENILAIAN PERFORMA PEMAIN ===")
  try:
    jumlah_pemain = int(input("Masukkan jumlah pemain: "))
  except ValueError:
    jumlah_pemain = 0

  daftar_pemain = []

  # Perulangan untuk memasukkan data beberapa pemain
  for i in range(jumlah_pemain):
    print(f"\nData Pemain ke-{i + 1}")
    nama = input("Nama: ")
    id_pemain = input("ID Pemain: ")
    role = input("Role: ")
    level = None
    try:
      kill = float(input("Nilai Kill: "))
      assist = float(input("Nilai Assist: "))
      objective = float(input("Nilai Objective: "))
    except ValueError:
      kill, assist, objective = 0.0, 0.0, 0.0

    # Membuat objek dari class Pemain dan menyimpannya ke dalam list
    pemain_baru = Pemain(nama, id_pemain, role, kill, assist, objective, level)
    daftar_pemain.append(pemain_baru)

  # Menampilkan rekapitulasi performa dalam bentuk tabel yang rapi
  print("\n" + "=" * 65)
  print("REKAPITULASI PERFORMA PEMAIN")
  print("=" * 65)
  print(
      f"{'No':<3} {'Nama':<10} {'ID Pemain':<12} {'Role':<12}"
      f" {'Skor Akhir':<12} {'Status':<15} {'Level':<20}"
  )
  print("-" * 80)

  for i, p in enumerate(daftar_pemain, 1):
    skor = p.hitung_skor_akhir()
    status = p.status_performa()
    level = p.tentukan_level()
    # Memanfaatkan f-string untuk menampilkan format rapi[cite: 2]
    print(
        f"{i:<3} {p.nama:<10} {p.id_pemain:<12} {p.role:<12}",
        f" {skor:<12.2f} {status:<15} {level:<20}"
)
  print("=" * 80)


if __name__ == "__main__":
  main()