<<<<<<< HEAD
# Buat file dengan nama bitwise_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()

print("======================================")
print("3. OPERATOR BITWISE")
print("======================================")

angka1_2023 = int(input("Masukkan angka bitwise-1: "))
angka2_2023 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1 =",angka1_2023,"| biner =",bin(angka1_2023))
print("angka1 =",angka2_2023,"| biner =",bin(angka2_2023))

# Bitwise AND
hasil_2023 = angka1_2023 & angka2_2023
print("\nBitwise AND (&)")
print(angka1_2023,"&",angka2_2023,hasil_2023)
print("Biner hasil =",bin(hasil_2023))
print("Biner hasil (8 bit) =",format(hasil_2023,"08b"))

# Bitwise OR
hasil_2023 = angka1_2023 | angka2_2023
print("\nBitwise OR (|)")
print(angka1_2023,"|",angka2_2023,hasil_2023)
print("Biner hasil =",bin(hasil_2023))
print("Biner hasil (8 bit) =",format(hasil_2023,"08b"))

# Bitwise XOR
hasil_2023 = angka1_2023 ^ angka2_2023
print("\nBitwise XOR (^)")
print(angka1_2023,"^",angka2_2023,hasil_2023)
print("Biner hasil =",bin(hasil_2023))
print("Biner hasil (8 bit) =",format(hasil_2023,"08b"))

# Bitwise NOT
hasil_2023 = ~angka1_2023
print("\nBitwise NOT (~)")
print(angka1_2023,"~",angka2_2023,hasil_2023)
print("Biner hasil =",bin(hasil_2023))
print("Biner hasil (8 bit) =",format(hasil_2023,"08b"))

# Bitwise geser kiri
jumlah_geser_2023 = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil_2023 = angka1_2023 << jumlah_geser_2023
print("\nBitwise geser kiri (<<)")
print(angka1_2023,"<<",jumlah_geser_2023,"=",hasil_2023)
print("Biner hasil =",bin(hasil_2023))
print("Biner hasil (8 bit) =",format(hasil_2023,"08b"))

# Bitwise geser kanan
hasil_2023 = angka1_2023 >> jumlah_geser_2023
print("\nBitwise geser kiri (>>)")
print(angka1_2023,">>",jumlah_geser_2023,"=",hasil_2023)
print("Biner hasil =",bin(hasil_2023))
=======
# Buat file dengan nama bitwise_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()

print("======================================")
print("3. OPERATOR BITWISE")
print("======================================")

angka1_2023 = int(input("Masukkan angka bitwise-1: "))
angka2_2023 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1 =",angka1_2023,"| biner =",bin(angka1_2023))
print("angka1 =",angka2_2023,"| biner =",bin(angka2_2023))

# Bitwise AND
hasil_2023 = angka1_2023 & angka2_2023
print("\nBitwise AND (&)")
print(angka1_2023,"&",angka2_2023,hasil_2023)
print("Biner hasil =",bin(hasil_2023))
print("Biner hasil (8 bit) =",format(hasil_2023,"08b"))

# Bitwise OR
hasil_2023 = angka1_2023 | angka2_2023
print("\nBitwise OR (|)")
print(angka1_2023,"|",angka2_2023,hasil_2023)
print("Biner hasil =",bin(hasil_2023))
print("Biner hasil (8 bit) =",format(hasil_2023,"08b"))

# Bitwise XOR
hasil_2023 = angka1_2023 ^ angka2_2023
print("\nBitwise XOR (^)")
print(angka1_2023,"^",angka2_2023,hasil_2023)
print("Biner hasil =",bin(hasil_2023))
print("Biner hasil (8 bit) =",format(hasil_2023,"08b"))

# Bitwise NOT
hasil_2023 = ~angka1_2023
print("\nBitwise NOT (~)")
print(angka1_2023,"~",angka2_2023,hasil_2023)
print("Biner hasil =",bin(hasil_2023))
print("Biner hasil (8 bit) =",format(hasil_2023,"08b"))

# Bitwise geser kiri
jumlah_geser_2023 = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil_2023 = angka1_2023 << jumlah_geser_2023
print("\nBitwise geser kiri (<<)")
print(angka1_2023,"<<",jumlah_geser_2023,"=",hasil_2023)
print("Biner hasil =",bin(hasil_2023))
print("Biner hasil (8 bit) =",format(hasil_2023,"08b"))

# Bitwise geser kanan
hasil_2023 = angka1_2023 >> jumlah_geser_2023
print("\nBitwise geser kiri (>>)")
print(angka1_2023,">>",jumlah_geser_2023,"=",hasil_2023)
print("Biner hasil =",bin(hasil_2023))
>>>>>>> 52c64aa382874848ef580b0449d47e5add23e682
print("Biner hasil (8 bit) =",format(hasil_2023,"08b"))