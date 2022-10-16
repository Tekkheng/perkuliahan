# NIM : 20210801205
# NAMA : Tek kheng

# int => input angka
# float => input angka koma
# print => output hasil

nim = input("isi Nim : ")
nama = input("isi Nama : ")
jenis_kelamin = input("isi Gender : ")
tgl_input = input("Tanggal Input : ")
matkul = input("Mata Kuliah : ")

absensi = float(input("absensi : "))
tugas = float(input("Tugas : "))
uts = float(input("Uts : "))
uas = float(input("Uas : "))

abs = float(absensi * 20/100)
tgs = float(tugas * 25/100)
ut = float(uts * 25/100)
us = float(uas * 30/100)

nilai_akhir = abs + tgs + ut + us
print("\n")

print("================== Info Mahasiswa ==================")
print("Nim : ", nim)
print("Nama : ", nama)
print("Jenis_kelamin : ", jenis_kelamin)
print("Tanggal Input : ", tgl_input)
print("Matkul : ", matkul)
print("Nilai Akhir : ", nilai_akhir)

if nilai_akhir >= 80 and nilai_akhir <= 100:
    print("Grade A")
elif nilai_akhir >= 77 and nilai_akhir <= 79.9:
    print("Grade A-")
elif nilai_akhir >= 74 and nilai_akhir <= 76.9:
    print("Grade B+")
elif nilai_akhir >= 71 and nilai_akhir <= 73.9:
    print("Grade B")
elif nilai_akhir >= 68 and nilai_akhir <= 70.9:
    print("Grade B-")
elif nilai_akhir >= 64 and nilai_akhir <= 67.9:
    print("Grade C+")
elif nilai_akhir >= 60 and nilai_akhir <= 63.9:
    print("Grade C")
elif nilai_akhir >= 50 and nilai_akhir <= 59:
    print("Grade D")
elif nilai_akhir >=0 and nilai_akhir <= 49:
    print("Grade E")


if nilai_akhir >= 60 and nilai_akhir <= 100:
    print("Anda Lulus")
elif nilai_akhir >= 0 and nilai_akhir < 60:
    print("Anda Tidak Lulus")
else:
    print("Nilai salah")
