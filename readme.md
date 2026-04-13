# Penjelasan Kode

## 1. Basis Pengetahuan (Knowledge Base)
knowledge_base = {
    "RAM Rusak": {
        "gejala": ["Sering terjadi Blue Screen (BSOD)", ...],
        "solusi": "Coba cabut RAM..."
    }
}
Bagian ini adalah otak dari sistem pakar. Data tidak disimpan menggunakan percabangan if-else yang panjang, melainkan menggunakan struktur data Dictionary

daftar_gejala = []
for data in knowledge_base.values():
    for g in data["gejala"]:
        if g not in daftar_gejala:
            daftar_gejala.append(g)
Blok kode ini bertujuan untuk mengambil semua gejala yang ada di dalam knowledge_base dan mengumpulkannya ke dalam satu list bernama daftar_gejala. Pengecekan if g not in daftar_gejala untuk memastikan tidak ada gejala yang terduplikasi saat ditampilkan ke layar pengguna.

input_user = input("Masukkan nomor gejala: ")
try:
    pilihan_index = [int(x.strip()) - 1 for x in input_user.split(',')]
    gejala_user = [daftar_gejala[i] for i in pilihan_index if 0 <= i < len(daftar_gejala)]
except ValueError:
* input_user.split(','): memecah inputan teks pengguna yang dipisahkan oleh koma menjadi list (contoh: "1, 3" menjadi ["1", " 3"]).
* int(x.strip()) - 1: menghapus spasi (strip()), mengubah teks menjadi angka (int()), dan dikurangi 1 karena indeks List di Python dimulai dari 0, sedangkan menu di layar dimulai dari 1.
* gejala_user: list baru yang berisi teks gejala aktual berdasarkan nomor yang dipilih pengguna. Blok try-except digunakan untuk mencegah program crash jika pengguna memasukkan huruf, bukan angka

hasil_diagnosa = None
max_kecocokan = 0

for kerusakan, data in knowledge_base.items():
    kecocokan = 0
    for g in gejala_user:
        if g in data["gejala"]:
            kecocokan += 1
    
    if kecocokan > max_kecocokan:
        max_kecocokan = kecocokan
        hasil_diagnosa = kerusakan
* Program melakukan looping untuk mengecek setiap jenis kerusakan di dalam knowledge_base.
* Variabel kecocokan digunakan sebagai counter. Program akan mengecek, apakah gejala yang dialami pengguna (gejala_user) ada di dalam list gejala kerusakan tersebut (data["gejala"]). Jika ada, nilai kecocokan bertambah 1.
* Logika if kecocokan > max_kecocokan: berfungsi untuk mencari kerusakan dengan jumlah gejala yang paling banyak cocok (irisan terbesar). Kerusakan dengan nilai tertinggi tersebut akan disimpan di dalam variabel hasil_diagnosa

if hasil_diagnosa and max_kecocokan > 0:
    print(f"Kemungkinan Kerusakan : {hasil_diagnosa}")
    # ... cetak solusi ...
else:
    print("Sistem tidak dapat mendeteksi kerusakan...")
Jika max_kecocokan > 0 (minimal ada 1 gejala yang cocok), maka program akan menampilkan nama kerusakan beserta solusi dari dictionary. Namun, jika pengguna memasukkan gejala acak yang tidak membentuk pola kerusakan apa pun (atau nilai max_kecocokan tetap 0), blok else akan tereksekusi, memenuhi kriteria tugas bahwa program harus bisa menangani kondisi jika tidak ada gejala yang cocok