# Jawaban Nomor 4 :
import os 
print("NOMOR 4")
def inputDt():
    nim = int(input("Nim : "))
    nama = input("Nama : ")
    os.system("clear")
    return nim,nama

def menu():
    print("Pilihan : ")
    for index,i in enumerate(["Cappucino","Teh","exit"]):
        print(f"{index+1}.{i}")
    print("=".center(30,"="))

def inputHarga(m,ppn):
    while True :
        print(f"Memilih {m}")
        harga = int(input(f"Masukkan Harga {m} : "))
        print(f"Harga input {m} : {harga:,}")
        hasil = harga + (harga * ppn)
        ganti = input(f"\nGanti harga {m}? y/n : ")
        if ganti == "y":
            os.system("clear")
            continue
        elif ganti != "y" and ganti != "n":
            os.system("clear")
            print("Pilihan tidak ada")
            continue
        else:
            os.system("clear")
            return hasil,harga

def header(nim,nama):
    print("Program Sederhana".center(30,"="))
    print(f"Nim : {nim}")
    print(f"Nama : {nama}")
    print("")

def program_sederhana():
    ppn = 10/100
    nim,nama = inputDt()
    while True:
        header(nim,nama)
        menu()
        pil = int(input("Masukkan Pilihan : "))
        if pil == 1:
            os.system("clear")
            hasil,h_input = inputHarga("Cappucino",ppn)
            print(f"Harga Input Cappucino: {h_input:,}")
            print(f"Harga Akhir : {hasil:,}")
            print("")
        elif pil == 2:
            os.system("clear")
            hasil,h_input = inputHarga("Teh",ppn)
            print(f"Harga Input Teh : {h_input:,}")
            print(f"Harga Akhir : {hasil:,}")
            print("")
        elif pil == 3:
            print("AKHIR PROGRAM\n")
            break
        else:
            os.system("clear")
            print("pilihan tidak ada")
            continue
program_sederhana()