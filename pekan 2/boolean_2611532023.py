# Buar file dengan nama Boolean_2611532023
# Nama variabel ditambah 4 digit nim terakhir contoh: nilai_1234
# Deklarasi variabel dengan tipe data Boolean
is_lulus_2023 = True
is_cumlaude_2023 = True

# Menggunakan Boolean
nilai_2023 = 85
batas_lulus_2023 = 75

# Menentukan nilai Boolean dari kondisi
status_kelulusan_2023 = nilai_2023 >= batas_lulus_2023 # Hasilnya akan True

print("=== Check Kelulusan ===")
print("Nilai: ",nilai_2023)
print("Apakah lulus?: ",status_kelulusan_2023)
if is_lulus_2023 and is_cumlaude_2023:
    print("Selamat, Anda lulus dengan predikat Cum Laude!")