operator = input("isi Operator dengan tambah,kurang,kali, atau bagi : ")
angka1 = int(input("isi angka1 : "))
angka2 = int(input("isi angka2 : "))

hasil = angka1 + angka2
hasil2 = angka1 - angka2
hasil3 = angka1 * angka2
hasil4 = angka1 / angka2

if operator == "tambah":
    print("Hasil Pertambahan : ",hasil)
elif operator == "kurang":
    print("Hasil Pengurangan : ",hasil2)
elif operator == "kali":
    print("Hasil Perkalian : ",hasil3)
elif operator == "bagi":
    print("Hasil Pembagian : ",hasil4)

  

