Nama = "Tek kheng"
Nim = 20210801205

info = "sample operator in python"
print(info)

operator = input("ketikkan tambah/kurang/kali/bagi : ")
bil1 = int(input("isi bilangan 1 = "))
bil2 = int(input("isi bilangan 2 = "))

tambah = int(bil1 + bil2)
kurang = int(bil1 - bil2)
kali = int(bil1 * bil2)
bagi = int(bil1 / bil2)

if operator == "tambah":
    print("Hasil = ",tambah)
elif operator == "kurang":
    print("Hasil = ",kurang)
elif operator == "kali":
    print("Hasil = ",kali)
elif operator == "bagi":
    print("Hasil = ",bagi)