# Buat file dengan nama Konstanta_2611532023
# Program ini menggunakan konstanta untuk menghitun luas lingkaran
# nama variabel ditambah 4 digit nim terakhir contoh: jari_2023

from typing import Final
PI: Final = 3.14
print("Pi: %f" % (PI))
jari_2023 = float(input("Masukkan nilai jari-jari: "))
luas_2023 = PI * jari_2023
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_2023,luas_2023))