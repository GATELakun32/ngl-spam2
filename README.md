# NGL Spammer

Program Python untuk mengirim pesan ke NGL (ngl.link) dengan fitur multi-threading.

## ⚠️ Peringatan
Program ini dibuat untuk tujuan edukasi. Gunakan dengan bijak dan sesuai dengan ketentuan layanan NGL.

## 📋 Persyaratan
- Python 3.x
- Library `requests`
- File `user-agents.txt`
- File `proxies.txt` (opsional)

## 🛠️ Instalasi

1. Clone atau download repository ini
2. Install dependencies yang diperlukan:
```bash
pip install requests
```

3. Siapkan file-file yang diperlukan:
   - `user-agents.txt`: Berisi daftar User-Agent
   - `proxies.txt`: Berisi daftar proxy (opsional)

## 🐧 Panduan Khusus Kali Linux

1. Buka Terminal dan update sistem:
```bash
sudo apt update && sudo apt upgrade -y
```

2. Install Python dan pip jika belum ada:
```bash
sudo apt install python3 python3-pip -y
```

3. Install library yang diperlukan:
```bash
pip3 install requests
```

4. Buat file user-agents.txt:
```bash
nano user-agents.txt
```
Salin beberapa user agent berikut:
```
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36
Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0
```

5. Buat file proxies.txt (opsional):
```bash
nano proxies.txt
```
Tambahkan proxy yang ingin digunakan (satu proxy per baris)

6. Jalankan program:
```bash
python3 spamngl.py
```

Catatan untuk Kali Linux:
- Pastikan Anda memiliki hak akses root jika diperlukan
- Gunakan `python3` alih-alih `python` untuk menjalankan program
- Jika mengalami masalah permission, gunakan:
```bash
chmod +x spamngl.py
```

## 🚀 Cara Penggunaan

1. Jalankan program:
```bash
python spamngl.py
```

2. Masukkan informasi yang diminta:
   - Username NGL target (tanpa @)
   - Pesan yang akan dikirim
   - Jumlah pesan yang akan dikirim
   - Jeda waktu antar pengiriman (dalam detik)
   - Pilihan menggunakan proxy (y/n)

## ⚙️ Konfigurasi

Anda dapat mengubah beberapa pengaturan di dalam file `spamngl.py`:
- `THREADS`: Jumlah thread yang berjalan bersamaan (default: 10)
- `MAX_RETRIES`: Jumlah percobaan ulang jika gagal (default: 3)

## 📝 Log

Program akan mencatat semua pesan yang berhasil dikirim ke dalam file `spam_log.txt`.

## 🔧 Troubleshooting

1. Jika muncul error "File not found":
   - Pastikan file `user-agents.txt` dan `proxies.txt` ada di folder yang sama
   - Jika tidak menggunakan proxy, file `proxies.txt` bisa kosong

2. Jika koneksi gagal:
   - Periksa koneksi internet Anda
   - Pastikan proxy yang digunakan valid (jika menggunakan proxy)
   - Coba tambah jeda waktu antar pengiriman

## 📜 Lisensi

Program ini dibuat oleh KARTO. Gunakan dengan tanggung jawab.

## ⚠️ Disclaimer

Penulis tidak bertanggung jawab atas penyalahgunaan program ini. Gunakan sesuai dengan ketentuan layanan NGL. 