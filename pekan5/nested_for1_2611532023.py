batas_2023 = int(input("Masukkan nilai batas: "))
for line_2023 in range(1, batas_2023 + 1):
    for j_2023 in range(1, (-1 * line_2023 + batas_2023) + 1):
        print(".", end="")
    print(line_2023)