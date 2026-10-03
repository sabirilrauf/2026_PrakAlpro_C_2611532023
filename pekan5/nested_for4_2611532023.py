tinggi_2023 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_2023 %2  != 0:
    print("Tinggi harus bilangan genap!!")
else:
    a_2023 = tinggi_2023
    c_2023 = a_2023
    lebar_2023 = (2 * tinggi_2023 ) - 2

    for i_2023 in range (1, tinggi_2023 + 1):
        b_2023 = c_2023 + 1

        for j_2023 in range(1, lebar_2023 + 1):
            # baris atas dan bawah
            if i_2023 == 1 or i_2023 == tinggi_2023:
                if j_2023 == 1 or j_2023 == lebar_2023:
                    print("#", end="")
                else:
                    print("=", end="")
            else:
                if j_2023 == 1 or j_2023 == lebar_2023:
                    print("|", end="")
                else:
                    if j_2023 == c_2023:
                        print("<", end="")
                    elif j_2023 == b_2023:
                        print(">", end="")
                    elif j_2023 == (lebar_2023 - c_2023):
                        print("<", end="")
                    elif j_2023 == (lebar_2023 - c_2023 + 1):
                        print(">", end="")
                    elif j_2023 > b_2023 and j_2023 < (lebar_2023 - c_2023):
                        print(".", end="") 
                    else:
                        print(" ", end="")
        print()

# logika asli java
        a_2023 -= 2
        if a_2023 <= 0:
            c_2023  =  (-a_2023) + 2
        else:
            c_2023 = a_2023

                    
