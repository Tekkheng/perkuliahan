def tambah():
    a=int(input("bil1 : "))
    b=int(input("bil2 : "))
    hasil = a + b
    print("hasil tambah : ",hasil)
    print("\n")

def kurang():
    a=int(input("bil1 : "))
    b=int(input("bil2 : "))
    hasil = a - b
    print("hasil kurang : ",hasil)
    print("\n")

def kali():
    a=int(input("bil1 : "))
    b=int(input("bil2 : "))
    hasil = a * b
    print("hasil kali : ",hasil)
    print("\n")

def bagi():
    a=int(input("bil1 : "))
    b=int(input("bil2 : "))
    hasil = a / b
    print("hasil bagi : ",hasil)
    print("\n")


while True:
    print("======== MENU ========")
    print("1.penjumlahan")
    print("2.Pengurangan")
    print("3.Perkalian")
    print("4.Pembagian")
    print("5.Exit")
    print("======================")

    pilih = int(input("Pilih(1-5) : "))
    
    if pilih == 1:
        tambah()
    elif pilih == 2:
        kurang()
    elif pilih == 3:
        kali()
    elif pilih == 4:
        bagi()
    elif pilih == 5:    
        break
    else:
        print("pilihan salah")