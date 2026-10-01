batas_2023= int(input("Masukkan tinggi segitiga: "))
for line_2023 in range(1, batas_2023 + 1):
    for i_2023 in range(batas_2023 - line_2023) :
        print(" ", end="")
    for j_2023 in range(line_2023):
        print("*", end=" ")
    print()    