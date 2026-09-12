# Deklarasi Variabel dan Tipe Data
nama = "Afifah"  # string
umur = 20  # integer
tinggi_badan = 157.5  # float
mahasiswa = True  # boolean
hobi = ["Membaca", "Menonton"]  # list

# Manipulasi String
pesan = "Halo, " + nama + "!"
print(pesan)

print("Banyaknya huruf pada nama:", len(nama))

print("Uppercase:", nama.upper())
print("Lowercase:", nama.lower())

# Operasi Matematika Sederhana
a = 10
b = 3

print("misal nilai a & b secara berurutan adalah:", a, b)
print("Penjumlahan:", a + b)
print("Pengurangan:", a - b)
print("Perkalian:", a * b)
print("Pembagian:", a / b)
print("Pembagian Bulat:", a // b)
print("Sisa Bagi / Modulus:", a % b)

# List dan Akses Elemen
print("List:", hobi)

print("Hobi pertama:", hobi[0])
print("Hobi terakhir:", hobi[-1])

hobi.append("Menghujat")
print("hobi aku nambah, jadi:", hobi)

hobi.remove("Membaca")
print("Hobi membaca dihilangkan, menjadi:", hobi)

item_terhapus = hobi.pop()
print(f"Item {item_terhapus} akan dihapus dengan pop")
print("List akhir:", hobi)

# Penggunaan Input dari User
input_nama = input("Masukkan nama Anda: ")
input_umur = input("Masukkan umur Anda: ")

print(f"Halo, nama saya {nama} dan umur saya {input_umur} tahun.")