#program menggunakan fungsi input()

ulang_2023 = int(input("Masukkan jumlah perulangan: "))
print("Perulangan ke-0 sampai ke-", ulang_2023 - 1)
for i in range(ulang_2023):
    print(i, end=" ")
print()
print("Perulangan ke-1 sampai ke-", ulang_2023)
for i in range(1,ulang_2023 + 1):
    print(i, end=" ")