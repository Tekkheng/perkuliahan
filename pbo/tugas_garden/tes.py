import os
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class Plant:
    def __init__(self):
        self.statusText = ""
        self.statusTumbuh = 0
        self.jumlahAir = 0
        self.jumlahPupuk = 0

    def beriAir(self):
        self.jumlahAir += 1
        self.cek_kondisi_tumbuh()

    def beriPupuk(self):
        self.jumlahPupuk += 1
        self.cek_kondisi_tumbuh()

    def cek_kondisi_tumbuh(self):
        if self.statusTumbuh < 4:
            if self.jumlahAir >= 3 and self.jumlahPupuk >= 1 :
                self.tumbuh()

    def tumbuh(self):
        self.jumlahAir -= 3
        self.jumlahPupuk -= 1
        self.statusTumbuh += 1
        self.statusText = self.getStatusText()

        self.displayPlant()

    def getStatusText(self):
        if self.statusTumbuh == 0:
            return "Benih"
        elif self.statusTumbuh == 1:
            return "Tunas"
        elif self.statusTumbuh == 2:
            return "Tanaman Kecil"
        elif self.statusTumbuh == 3:
            return "Tanaman Besar"
        return "Berbunga"

    def displayPlant(self):
        print(f"\nStatus : {self.statusText}")
        print(f"Jumlah Air : {self.jumlahAir}")
        print(f"Jumlah Pupuk : {self.jumlahPupuk}")

class Anggrek(Plant):
    def get_jenis(self):
        jenis = "Anggrek"
        return jenis

class Mawar(Plant):
    def get_jenis(self):
        jenis = "Mawar"
        return jenis

class Melati(Plant):
    def get_jenis(self):
        jenis = "Melati"
        return jenis

anggrek = Anggrek()
mawar = Mawar()
melati = Melati()


def hasil(jenis):
    while True:
        if sistem_operasi == "posix":
            os.system("clear")
        elif sistem_operasi == "cls":
            os.system("cls")

        print(f"{jenis.get_jenis()}".center(30,"="))
        [print(f"{no+1}.{i}") for no,i in enumerate(["Beri Air","Beri Pupuk","Exit"])]

        jenis.displayPlant()
        pil = int(input("Pil : "))

        if pil == 1:
            if jenis.statusTumbuh <= 3 and jenis.jumlahAir <= 2:
                jenis.beriAir()
            elif "Berbunga" in jenis.statusText:
                print("Berbunga")
                print("Tanaman Sudah Besar, Silahkan urus tanaman lainnya !")
                e = input("Enter : ")
            else:
                print("jumlah air sudah cukup,silahkan tambahkan pupuk!")
                e = input("Enter : ")
        elif pil == 2:
            if jenis.statusTumbuh <= 3 and jenis.jumlahPupuk < 1:
                    jenis.beriPupuk()
            elif "Berbunga" in jenis.statusText:
                print("Berbunga")
                print("Tanaman Sudah Besar, Silahkan urus tanaman lainnya !")
                e = input("Enter : ")
            else:
                print("jumlah pupuk sudah cukup,silahkan tambahkan air!")
                e = input("Enter : ")
        elif pil == 3:
            break

if __name__ == "__main__":
    sistem_operasi = os.name
    
    while True:
        if sistem_operasi == "posix":
            os.system("clear")
        elif sistem_operasi == "cls":
            os.system("cls")

        print(f"{' Menu Plant ':=^30}")
        [print(f"{no+1}.{i}") for no,i in enumerate(["Anggrek","Mawar","Melati","Exit"])]
        print(f"{'=':=^30}")

        opsi = int(input("\nPilih Bunga : "))
        if opsi == 1:
            hasil(anggrek)
        elif opsi == 2:
            hasil(mawar)
        elif opsi == 3:
            hasil(melati)
        elif opsi == 4:
            break
    print("Akhir Program")