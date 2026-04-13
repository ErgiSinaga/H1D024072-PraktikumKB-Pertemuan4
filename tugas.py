def sistem_pakar_diagnosa():
    print("Sistem Pakar Diagnosa Kerusakan Komputer")
    
    knowledge_base = {
        "RAM Rusak": {
            "gejala": ["Sering terjadi Blue Screen", "Terdengar bunyi beep berkali-kali saat booting", "Komputer sering restart sendiri tanpa sebab"],
            "solusi": "Coba cabut RAM dan bersihkan pin kuningannya dengan penghapus karet. Pastikan terpasang dengan rapat. Jika masih berlanjut, coba ganti RAM."
        },
        "Power Supply (PSU) Lemah": {
            "gejala": ["Komputer mati mendadak saat menjalankan beban berat (seperti game)", "Terkadang PC sulit dihidupkan", "Tercium bau hangus dari area casing"],
            "solusi": "Segera matikan PC. Cek kabel power, jika normal kemungkinan besar komponen dalam PSU bermasalah. Segera ganti PSU dengan watt yang mumpuni."
        },
        "Overheat (Prosesor)": {
            "gejala": ["Kipas pendingin berputar sangat kencang dan berisik", "Performa PC tiba-tiba menjadi sangat lambat (throttling)", "Komputer mati mendadak dan baru bisa dihidupkan setelah dingin"],
            "solusi": "Bersihkan debu pada kipas/heatsink prosesor dan oleskan ulang pasta termal (thermal paste). Pastikan sirkulasi udara casing lancar."
        },
        "VGA Bermasalah": {
            "gejala": ["Muncul garis-garis aneh (artefak) pada layar monitor", "Layar tiba-tiba blank hitam atau freeze saat bermain game", "Sering muncul pesan error driver grafis crash"],
            "solusi": "Coba update atau install ulang driver VGA. Bersihkan pin konektor jika menggunakan VGA Add-on. Jika masih artefak, kemungkinan besar hardware VGA rusak."
        },
        "Hardisk/SSD Corrupt": {
            "gejala": ["Proses booting atau membuka file terasa sangat lambat", "Sering muncul pesan error 'Disk Boot Failure'", "Terdengar bunyi 'klik' atau gesekan kasar dari dalam PC (khusus HDD)"],
            "solusi": "Segera backup data penting Anda. Lakukan pengecekan kesehatan disk (misal via chkdsk). Jika bad sector parah, segera ganti dengan SSD/HDD baru."
        }
    }

    daftar_gejala = []
    for data in knowledge_base.values():
        for g in data["gejala"]:
            if g not in daftar_gejala:
                daftar_gejala.append(g)

    print("\nSilakan pilih gejala yang dialami pada komputer/laptop Anda.")
    for i, gejala in enumerate(daftar_gejala):
        print(f"[{i + 1}] {gejala}")

    print("\nAnda bisa memilih lebih dari satu gejala (pisahkan dengan koma, contoh: 1,3,5)")
    input_user = input("Masukkan nomor gejala: ")

    try:
        pilihan_index = [int(x.strip()) - 1 for x in input_user.split(',')]
        gejala_user = [daftar_gejala[i] for i in pilihan_index if 0 <= i < len(daftar_gejala)]
    except ValueError:
        print("\n[Error] Input tidak valid. Harap masukkan angka yang dipisahkan dengan koma.")
        return

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

    print("HASIL DIAGNOSA")
    if hasil_diagnosa and max_kecocokan > 0:
        print(f"Kemungkinan Kerusakan : {hasil_diagnosa}")
        print(f"Solusi Singkat        : {knowledge_base[hasil_diagnosa]['solusi']}")
    else:
        # Menangani kondisi jika gejala tidak cocok dengan kerusakan apa pun
        print("Sistem tidak dapat mendeteksi kerusakan spesifik berdasarkan gejala tersebut.")
        print("Solusi Singkat        : Silakan bawa komputer/laptop Anda ke teknisi terdekat untuk pengecekan menyeluruh.")

if __name__ == "__main__":
    sistem_pakar_diagnosa()