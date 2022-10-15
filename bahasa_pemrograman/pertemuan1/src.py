print("HAI Tek kheng");

def hitung():
    pilih=input("tambah,kurang,bagi,kali: ")
    bil1=int(input("Angka 1 : "))
    bil2=int(input("Angka 2 : "))

    if pilih == "tambah":
        tambah(bil1,bil2)
    elif pilih == "kurang":
        kurang(bil1,bil2)
    elif pilih == "kali":
        kali(bil1,bil2)
    elif pilih == "bagi":
        bagi(bil1,bil2)

def tambah(a,b):
    hasil = int(a + b)
    print(hasil)
def kurang(a,b):
    hasil = int(a - b)
    print(hasil)
def bagi(a,b):
    hasil = int(a / b)
    print(hasil)
def kali(a,b):
    hasil = int(a * b)
    print(hasil)

hitung()


