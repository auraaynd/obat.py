BATAS_STOK_MINIMAL = 15

daftar_obat = [
    "Paracetamol", "Amoxicillin", "Ibuprofen", "CTM", "Vitamin C",
    "Omeprazole", "Metformin", "Amlodipine", "Antasida", "Cefadroxil"
]

print("=== PENGECEKAN STOK OBAT APOTEK (OPERATOR PEMBANDING) ===")
print(f"Batas Minimal Stok (BATAS_STOK_MINIMAL): {BATAS_STOK_MINIMAL} unit\n")

for i in range(10):
    nama_obat = daftar_obat[i]
    print(f"--- Obat ke-{i+1}: {nama_obat} ---")
    
    stok = int(input(f"Masukkan jumlah stok {nama_obat}: "))
    
    print(f"Apakah stok {nama_obat} aman ? {stok >= BATAS_STOK_MINIMAL}")
    print(f"Apakah stok {nama_obat} kurang dari batas ? {stok < BATAS_STOK_MINIMAL}")
    print(f"Apakah stok {nama_obat} persis sama dengan batas ? {stok == BATAS_STOK_MINIMAL}")
    print("-" * 60)