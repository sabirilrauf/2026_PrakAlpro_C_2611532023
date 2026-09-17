print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")
nama_2023 = input("Masukkan Nama Mahasiswa : ")
kelamin_2023 = input("Masukkan Jenis Kelamin (L/P): ")
umur_2023 = int(input("Masukkan Umur : "))
skor_2023 = float(input("Masukkan Skor Tes Awal : "))

alamat_2023 = """
Irigasi,
Kecamatan Pauh,
Kota Padang,
Sumatera Barat,
Indonesia
"""
from typing import Final
kkm_2023: Final = 75.0
token_2023 = 100+3j
lulus_2023 = skor_2023 > kkm_2023

print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
print("Nama Mahasiswa : ",nama_2023," | ",type(nama_2023))
print("Jenis Kelamin : ",kelamin_2023," | ",type(kelamin_2023))
print("Alamat Domisili : ",alamat_2023," | ",type(alamat_2023))
print("Umur : ",umur_2023," tahun | ",type(umur_2023))
print("Skor Tes Awal : ",skor_2023," | ",type(skor_2023))
print("ID Token Sinyal: ",token_2023," | ",type(token_2023))

print("=== STATUS KELULUSAN PRAKTIKUM ===")
print("Batas Minimum Nilai: ",kkm_2023," | ",type(kkm_2023))
print("Apakah Dinyatakan Lulus?: ",lulus_2023," | ",type(lulus_2023))