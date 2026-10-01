<<<<<<< HEAD
#program ini menggunakan fungsi input()
ulang_2023 = int (input("Masukkan nilai batas: "))

jumlah_2023 = 0
for i_2023 in range(1,ulang_2023 + 1):
    if i_2023 % 2 == 0:
        print(i_2023,end=" ")
        jumlah_2023 = jumlah_2023 + i_2023

        if i_2023 < ulang_2023:
            print(" + ",end=" ")  
        else :
            print(" = ", jumlah_2023, end="")

print ()
print  ("jumlah =",jumlah_2023)
=======
#program ini menggunakan fungsi input()
ulang_2023 = int (input("Masukkan nilai batas: "))

jumlah_2023 = 0
for i_2023 in range(1,ulang_2023 + 1):
    if i_2023 % 2 == 0:
        print(i_2023,end=" ")
        jumlah_2023 = jumlah_2023 + i_2023

        if i_2023 < ulang_2023:
            print(" + ",end=" ")  
        else :
            print(" = ", jumlah_2023, end="")

print ()
print  ("jumlah =",jumlah_2023)
>>>>>>> e2c6ec5fd9f86723962f8bc8be37145094085115
