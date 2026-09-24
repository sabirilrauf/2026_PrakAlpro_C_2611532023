umur_2023 = int(input("Input umur Anda: "))
sim_2023 = input("Apakah Anda Sudah Punya SIM C: ")[0]

if umur_2023 >= 17 and sim_2023 == "y":
    print("Anda Sudah dewasa dan boleh bawa motor")

elif umur_2023 >= 17 and sim_2023 != "y":
    print("Anda Sudah dewasa tetapi tidak boleh bawa motor")

elif umur_2023 < 17 and sim_2023 != "y":
    print("Anda Belum Cukup Umur bawa motor")

elif umur_2023 < 17 and sim_2023 == "y":
    print("Anda Belum Cukup Umur punya SIM")

else:
    print("Anda Belum Cukup Umur dan tidak boleh bawa motor")
    print("Program Selesai")
