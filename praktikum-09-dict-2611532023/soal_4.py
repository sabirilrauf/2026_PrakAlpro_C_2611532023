absen = input().split()
sudah = input().split()

pengumpul = set(sudah)
belum = set(absen) - pengumpul
print("submitted:",str(len(pengumpul)), "student")
print("not submitted:",str(len(belum)), "student")

for nomor in absen : #untuk setiap nomer absen yang belum mengumpulkan tugas 
    if nomor not in pengumpul:
        print(nomor)


    