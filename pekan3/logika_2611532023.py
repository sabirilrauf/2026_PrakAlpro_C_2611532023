#buat file dengan nama logika_NIM.py
#nama variabel ditambah 4 digit nim terakhir contoh: a1_1234
#program ini menngunakan fungsi input()
#program operator logika dalam python

#memasukkan nilai boolean
#input tidak pela terhadap huruf besa dan kecil
a1_2023 = input("Input nilai boolean-1 (True/False): ").strip().lower() == "true"
a2_2023 = input("Input nilai boolean-2 (True/False): ").strip().lower() == "true"

print("\nA1=", a1_2023)
print("A2=", a2_2023)

#Konjungsj: bernilai true jika kedua nilai bernilai true
hasil_2023 = a1_2023 and a2_2023
print("\nKonjungsi (AND):", hasil_2023)

# Disjungsi: bernilai True jika salah satunya False
hasil_2023 = a1_2023 or a2_2023 
print("\nDisjungsi (OR)")
print("A1 or A2 =",hasil_2023)

# Negasi A1: membalik nilai A1
hasil_2023 = not a1_2023
print("\nNegasi A1(NOT)")
print("not A1",hasil_2023)

# Negasi A2: membalik nilai A2
hasil_2023 = not a2_2023
print("\nNegasi A2(NOT)")
print("not A2",hasil_2023)

# XOR: bernilai True jika kedua nilai berbeda
hasil_2023 = a1_2023 != a2_2023
print("\nDisjungsi Ekslusif (XOR)")
print("A1 XOR A2",hasil_2023)