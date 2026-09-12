# List – akses & manipulasi
data = ["Python", 100, 3.14, "IL", 250, True]

print("List awal:", data)
print("Elemen pertama:", data[0])
print("Elemen terakhir:", data[-1])

print("Slicing di [1:5:2]:", data[1:5:2])

print("\nSebelum manipulasi:", data)

data.append("jaya")  
data.insert(2, "afifah")  
data.extend([99, "buku"])  
data.pop()
data.remove(100)

print("dilakukan beberapa aksi, maka data sesudah manipulasi:", data)

# Tuple – immutability & unpacking
kumpulan_angka = (10, 20, 30, 40, 50)

print("Tuple:", kumpulan_angka)
print("Panjangnya:", len(kumpulan_angka))
print("Akses indeks ke-2:", kumpulan_angka[2])

a, b, *sisa = kumpulan_angka
print(f"Unpackingnya -> a: {a}, b: {b}, sisa (*rest): {sisa}")

# Set – keunikan & operasi himpunan
set_a = {1, 2, 2, 3, 4, 5}
set_b = {4, 5, 5, 6, 7, 8}

print("Set A (duplikat angka 2 otomatis hilang):", set_a)
print("Set B (duplikat angka 5 otomatis hilang):", set_b)

print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference:", set_a - set_b)
print("Symmetric Difference:", set_a ^ set_b)

# Dictionary – key/value dasar
mahasiswa = {
    "nama": "pip",
    "nim": "A11.2023.12345",
    "angkatan": 2023,
    "kota": "batam",
}

print("Dict awal adalah:", mahasiswa)

mahasiswa["jurusan"] = "Teknik Informatika" 
mahasiswa["kota"] = "Jakarta"  
del mahasiswa["angkatan"] 

print("Dict setelah diubah:", mahasiswa)

print("Keys:", mahasiswa.keys())
print("Values:", mahasiswa.values())
print("Items:", mahasiswa.items())

print("\nIterasi key: value:")
for kunci, nilai in mahasiswa.items():
    print(f"- {kunci}: {nilai}")
    
# Nested structures
daftar_buku = [
    {"judul": "Belajar Python", "penulis": "Andi", "tahun": 2020},
    {"judul": "Algoritma Dasar", "penulis": "Budi", "tahun": 2018},
    {"judul": "Pemrograman Web", "penulis": "Citra", "tahun": 2022},
    {"judul": "Kecerdasan Buatan", "penulis": "Dewi", "tahun": 2024},
]

print("Semua Judul Buku:")
for buku in daftar_buku:
    print(f"- {buku['judul']}")

tahun_filter = 2021
buku_terbaru = [
    buku["judul"] for buku in daftar_buku if buku["tahun"] >= tahun_filter
]
print(f"Buku terbit >= {tahun_filter}:", buku_terbaru)

angka_1_5 = range(1, 6)
list_kuadrat = [x**2 for x in angka_1_5]
print("List Kuadrat:", list_kuadrat)

target = "Python"
if target in data:
    print(f"'{target}' ditemukan di indeks ke-{data.index(target)}")