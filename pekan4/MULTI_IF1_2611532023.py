#buat nama file dengan nama MULTI_IF1_2611532023.py
#buat program untuk kondisional if
#nama variabel ditambah 4 digit nim terakhir contoh: ipk_2023
#program ini menggunakan fungsi input()

umur_2023 = int(input("input umur Anda: "))
sim_2023 = input("Apakah Anda Sudah Punya SIM (y/t): ")[0]

if umur_2023 >= 17 and sim_2023 == "y":
    print("Anda Sudah dewasa dan boleh bawa motor")

if umur_2023 >= 17 and sim_2023 != "y":
    print("Anda Sudah dewasa tetapi tidak boleh bawa motor")

if umur_2023 < 17 and sim_2023 != "y":
    print("Anda Belum Cukup Umur bawa motor")

if umur_2023 < 17 and sim_2023 == "y":
    print("Anda Belum Cukup Umur punya SIM")