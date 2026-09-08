# LAB-AP-14-2026

## 📚 Repositori Tugas Praktikum Algoritma & Pemrograman 2026

Selamat datang di repositori resmi **Praktikum Algoritma & Pemrograman 2026**. Repositori ini digunakan oleh mahasiswa untuk mengumpulkan seluruh Tugas Praktikum (TP) selama semester berlangsung melalui mekanisme *Fork* dan *Pull Request* (PR) di GitHub.

---

## 🛠️ Prasyarat (Requirements)

Sebelum memulai, pastikan Anda telah menyiapkan hal-hal berikut:
1. **Akun GitHub**: Terdaftar di [github.com](https://github.com/).
2. **Git CLI**: Terinstal di komputer Anda ([Download Git](https://git-scm.com/)). Cek instalasi via terminal:
   ```bash
   git --version
   ```
3. **Text Editor / IDE**: Visual Studio Code, PyCharm, atau editor lain pilihan Anda.

---

## 📁 Struktur Repositori & Penamaan File

Setiap mahasiswa telah memiliki folder khusus di repositori ini dengan format:
`<NIM>`

### Visualisasi Struktur Folder:
```text
LAB-AP-14-2026/
├── H071261026/
│   ├── Praktikum-1/
│   │   ├── TP1_1_H071261026.py
│   │   └── TP1_2_H071261026.py
│   └── Praktikum-2/
│       └── TP2_1_H071261026.py
├── H071261059/
└── README.md
```

### Aturan Penamaan File & Folder:
| Elemen | Format / Aturan Penamaan | Contoh |
| :--- | :--- | :--- |
| **Folder Mahasiswa** | `<NIM>` | `H071261026` *(Sudah ada di repo)* |
| **Folder Praktikum** | `Praktikum-<n>` *(n = nomor praktikum)* | `Praktikum-1`, `Praktikum-2` |
| **File Tugas** | `TP<n>_<noSoal>_<NIM>.py` | `TP1_1_H071261026.py`, `TP2_3_H071261026.py` |

---

## 🚀 Alur Pengumpulan Tugas (Step-by-Step Tutorial)

Ikuti langkah-langkah berikut secara berurutan:

### 1. Fork Repositori
1. Buka halaman repositori utama [LAB-AP-14-2026](https://github.com/ferastoro/LAB-AP-14-2026) di GitHub.
2. Klik tombol **Fork** di pojok kanan atas halaman.
3. Klik **Create fork** untuk menyalin repositori ini ke akun GitHub Anda.

---

### 2. Clone Repositori Fork ke Komputer
Buka Terminal / Command Prompt / Git Bash di komputer Anda, lalu jalankan perintah:

```bash
git clone https://github.com/USERNAME_ANDA/LAB-AP-14-2026.git
cd LAB-AP-14-2026
```
> [!IMPORTANT]
> Ganti `USERNAME_ANDA` dengan username akun GitHub Anda sendiri.

---

### 3. Konfigurasi Identitas Git (Sekali di Komputer)
Pastikan Git mengidentifikasi commit Anda dengan nama dan email GitHub yang benar:

```bash
git config user.name "USERNAME_GITHUB_ANDA"
git config user.email "EMAIL_GITHUB_ANDA"
```

---

### 4. Buat dan Pindah ke Branch Baru (`NIM_ANDA`)
Selalu kerjakan tugas pada **branch baru** dengan nama **NIM** Anda (bukan di branch `main`):

```bash
# Membuat sekaligus berpindah ke branch baru
git checkout -b NIM_ANDA
```
*Contoh:* `git checkout -b H071261026`

---

### 5. Masuk ke Folder Mahasiswa & Buat Sub-folder Praktikum
Navigasikan ke dalam folder nama Anda yang telah tersedia di repositori, lalu buat folder praktikum sesuai minggunya:

```bash
# Masuk ke folder Anda (gunakan tanda kutip jika nama folder mengandung spasi)
cd "H071261026"

# Buat folder Praktikum-n (misal: Praktikum-1)
mkdir Praktikum-1
cd Praktikum-1
```

---

### 6. Simpan File Tugas Anda
Simpan seluruh file program Python Anda di dalam folder `Praktikum-n` tersebut dengan penamaan yang sesuai.

*Contoh:*
- File soal 1: `TP1_1_H071261026.py`
- File soal 2: `TP1_2_H071261026.py`

---

### 7. Stage (Add) dan Commit Perubahan
Setelah menyelesaikan kode program:

1. **Cek Status Perubahan:**
   ```bash
   git status
   ```

2. **Tambahkan File ke Staging Area:**
   ```bash
   git add TP1_1_H071261026.py
   # Atau tambahkan seluruh file di folder Praktikum saat ini:
   git add .
   ```
   > [!TIP]
   > Gunakan `git status` kembali untuk memastikan file yang akan di-commit berwarna hijau.

3. **Lakukan Commit dengan Pesan Deskriptif:**
   ```bash
   git commit -m "Menambahkan tugas TP1 no 1 dan 2 H071261026"
   ```

---

### 8. Push Branch ke Repositori Fork Anda
Unggah perubahan dari komputer ke akun GitHub Anda:

```bash
git push origin NIM_ANDA
```
*Contoh:* `git push origin H071261026`

---

### 9. Buat Pull Request (PR) di GitHub
1. Buka repositori hasil **fork** Anda di halaman browser GitHub.
2. Anda akan melihat spanduk kuning bertuliskan **Compare & pull request**, klik tombol tersebut.
   *(Atau masuk ke tab **Pull requests** > **New pull request**)*.
3. Pastikan konfigurasi perbandingan branch benar:
   - **base repository**: `ferastoro/LAB-AP-14-2026` (base: `main`)
   - **head repository**: `USERNAME_ANDA/LAB-AP-14-2026` (compare: `NIM_ANDA`)
4. Berikan judul Pull Request yang jelas, contoh: `[TP-1] H071261026`.
5. Klik **Create pull request**.

> [!WARNING]
> **JANGAN PERNAH MELAKUKAN MERGE SENDIRI!**
> Setelah membuat Pull Request, biarkan status PR tetap **Open**. Asisten Laboratorium (Aslab) yang bertugas memeriksa kode, memberikan nilai/review, serta melakukan *merge* atau *close* pada PR Anda.

---

## 🔑 Autentikasi Push di GitHub (Personal Access Token / PAT)

Jika saat melakukan `git push` Anda diminta memasukkan Password, **GitHub tidak lagi menerima password akun biasa**. Anda harus menggunakan **Personal Access Token (PAT)** sebagai password.

### Cara Membuat Personal Access Token (Classic):
1. Klik **Foto Profil** Anda di pojok kanan atas GitHub > **Settings**.
2. Gulir ke bawah pada menu sebelah kiri dan klik **Developer settings**.
3. Pilih **Personal access tokens** > **Tokens (classic)**.
4. Klik **Generate new token** > **Generate new token (classic)**.
5. Isi bagian **Note** (contoh: *Token untuk LAB-AP-14-2026*).
6. Tentukan masa berlaku (*Expiration*), misal: 90 hari / No expiration.
7. Pada bagian **Select scopes**, centang kotak **`repo`** (Full control of private repositories).
8. Klik **Generate token** di bagian paling bawah.
9. **Salin dan simpan token tersebut** (Token hanya ditampilkan sekali). Gunakan token ini sebagai *Password* ketika diminta di terminal/Git CLI.

---

## 💡 Tips & Troubleshooting

- **Cek Branch Aktif**: Selalu pastikan Anda berada di branch `NIM_ANDA` sebelum membuat/mengedit file dengan mengetik `git branch`.
- **Pesan Commit yang Jelas**: Gunakan pesan commit yang singkat dan padat menjelaskan apa yang diubah.
- **Sync Fork (Jika Repositori Utama Berubah)**:
  Jika ada pembaruan di repo utama, buka repo fork Anda di browser dan klik tombol **Sync fork** > **Update branch**, lalu lakukan `git pull origin main` di komputer Anda.
