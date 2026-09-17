#buat nama file dengan nama assginment_nim.py
#nama variabel ditambah 4digit nim terakhir contoh: angka1_1234
#program ini menngunakan fungsi input()
#nilai yang dimasukkan akan dikonversi menjadi tipe data integer
#program operator assignment dalam python

angka1_2023 = int(input("Input angka-1: "))
angka2_2023 = int(input("Input angka-2: "))

print("\nNilai awal angka1 =", angka1_2023)
print("Nilai angka2 =", angka2_2023)

#assignment biasa 
hasil_2023 = angka1_2023
print("\nAssignment Biasa")
print("Hasil =",hasil_2023)

# Assigment penambahan
hasil_2023 = angka1_2023 
hasil_2023 += angka2_2023 
print("\nAssigment penambahan (+=)")
print("Hasil =",hasil_2023)

# Assigment pengurangan
hasil_2023 = angka1_2023 
hasil_2023 -= angka2_2023 
print("\nAssigment pengurangan (-=)")
print("Hasil =",hasil_2023)

# Assigment perkalian
hasil_2023 = angka1_2023 
hasil_2023 *= angka2_2023
print("\nAssigment perkalian (*=)")
print("Hasil =",hasil_2023)

# Assigment pembagian, pembagian bulat, dan sisa bagi
if angka2_2023 != 0:
    hasil_2023 = angka1_2023 
    hasil_2023 /= angka2_2023
    print("\nAssigment pembagian (/=)")
    print("Hasil =",hasil_2023)
    # Operator tambahan
    hasil_2023 = angka1_2023 
    hasil_2023 //= angka2_2023
    print("\nAssigment pembagian bulat (//=)")
    print("Hasil =",hasil_2023)
    hasil_2023 = angka1_2023 
    hasil_2023 %= angka2_2023
    print("\nOperator sisa bagi (%=)")
    print("Hasil =",hasil_2023)
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0.")

# Operator tambahan: assigment perpangkatan
hasil_2023 = angka1_2023 
hasil_2023 **= angka2_2023
print("\nOperator perpangkatan (**=)")
print("Hasil =",hasil_2023)