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
                print("ssss")
                self.tumbuh()

    def tumbuh(self):
        self.jumlahAir -= 3
        self.jumlahPupuk -= 1
        self.statusTumbuh += 1
        self.statusText = self.getStatusText()

        self.displayPlant()

    def getStatusText(self):
        match self.statusTumbuh:
            case 0: return "Benih"
            case 1: return "Tunas"
            case 2: return "Tanaman Kecil"
            case 3: return "Tanaman Besar"
        return "berbunga"

    def displayPlant(self):
        print(f"\nStatus : {self.statusText}")
        print(f"Jumlah Air : {self.jumlahAir}")
        print(f"Jumlah Pupuk : {self.jumlahPupuk}")

class Anggrek(Plant):
    def get_Jenis(self):
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
        match sistem_operasi:
            case "posix" : os.system("clear")
            case "nt" : os.system("cls")

        print(f"{'=':=^30}")
        [print(f"{no+1}.{i}") for no,i in enumerate(["Beri Air","Beri Pupuk","Exit"])]

        jenis.displayPlant()
        pil = int(input("Pil : "))
        match pil:
            case 1 : 
                if jenis.statusTumbuh <= 3 and jenis.jumlahAir <= 2:
                    jenis.beriAir()
                elif "berbunga" in jenis.statusText:
                    print("Berbunga")
                    print("Tanaman Sudah Besar, Silahkan urus tanaman lainnya !")
                    e = input("Enter : ")
                else:
                    print("jumlah air sudah cukup,silahkan tambahkan pupuk!")
                    e = input("Enter : ")
            case 2 : 
                if jenis.statusTumbuh <= 3 and jenis.jumlahPupuk < 1:
                    jenis.beriPupuk()
                elif "berbunga" in jenis.statusText:
                    print("Berbunga")
                    print("Tanaman Sudah Besar, Silahkan urus tanaman lainnya !")
                    e = input("Enter : ")
                else:
                    print("jumlah pupuk sudah cukup,silahkan tambahkan air!")
                    e = input("Enter : ")
            case 3 : 
                break

if __name__ == "__main__":
    sistem_operasi = os.name
    
    while True:
        match sistem_operasi:
            case "posix" : os.system("clear")
            case "nt" : os.system("cls")

        print(f"{'=':=^30}")
        [print(f"{no+1}.{i}") for no,i in enumerate(["Anggrek","Mawar","Melati","Exit"])]
        print(f"{'=':=^30}")

        opsi = int(input("\nPilih Bunga : "))

        match opsi:
            case 1 :
                hasil(anggrek)
            case 2 :
                hasil(mawar)
            case 3 : 
                hasil(melati)
            case 4 :
                break
    print("Akhir Program")



# def doThis():
    # labelT.after(1000, labelT.destroy())
    # labelT.destroy()
    # anggrek.destroy()
    # mawar.destroy()
    
    # print(anggrek.__dict__)
    # anggrek.pack(padx=10,pady=5,fil="x",expand=True)
    # beriAir = ttk.Button(frm,text="Beri Air",command=anggrek.beriAir)
    # beriAir.pack(padx=10,pady=5,fil="x",expand=True)

    # beriPupuk = ttk.Button(frm,text="Beri Pupuk",command=mawar.beriAir)
    # beriPupuk.pack(padx=10,pady=5,fil="x",expand=True)

    # exit = ttk.Button(frm,text="Exit")
    # exit.pack(padx=10,pady=5,fil="x",expand=True)

# def menu():
#     anggrek = ttk.Button(frm,text="Anggrek",command=doThis)
#     anggrek.pack(padx=10,pady=5,fil="x",expand=True)

#     mawar = ttk.Button(frm,text="Mawar",command=doThis)
#     mawar.pack(padx=10,pady=5,fil="x",expand=True)

# def kurang():
#     value = int(angka["text"])
#     angka["text"] = f"{value - 1}"

# window = tk.Tk()
# window.geometry("450x500")
# window.configure(bg="DarkSlateGrey")

# frm = ttk.Frame(window,padding=10)
# frm.pack(padx=60,fil="x",expand=True)

# labelT = ttk.Label(frm,text="testing")
# labelT.pack(padx=10,pady=10,fil="x",expand=True)

# anggrek = ttk.Button(frm,text="Anggrek",command=doThis)
# anggrek.pack(padx=10,pady=5,fil="x",expand=True)

# mawar = ttk.Button(frm,text="Mawar",command=doThis)
# mawar.pack(padx=10,pady=5,fil="x",expand=True)

# melati = ttk.Button(frm,text="Melati",command=doThis)
# melati.pack(padx=10,pady=5,fil="x",expand=True)

# window.mainloop()



# def tambah():
#     value = int(angka["text"])
#     angka["text"] = f"{value + 1}"

# def kurang():
#     value = int(angka["text"])
#     angka["text"] = f"{value - 1}"

# window = tk.Tk()
# window.configure(bg="DarkSlateGrey")

# frm = ttk.Frame(window,padding=10)
# frm.pack(padx=10,fil="x",expand=True)

# btnTambah = ttk.Button(frm,text="+",command=tambah)
# btnTambah.pack(padx=10,pady=10,fil="x",expand=True)

# angka = ttk.Label(frm,text="0")
# angka.pack(padx="10",pady="10",fil="x",expand=True)

# btnKurang = ttk.Button(frm,text="-",command=kurang)
# btnKurang.pack(padx=10,pady=10,fil="x",expand=True)

# window.mainloop()


# window = tk.Tk()
# window.configure(bg="DarkSlateGrey")

# frm = ttk.Frame(window,padding=10)
# # frm.pack(padx=10,fil="x",expand=True)

# window.rowconfigure(0, minsize=50, weight=1)
# window.columnconfigure([0, 1, 2], minsize=50, weight=1)

# btnTambah = ttk.Button(window,text="+")
# btnTambah.grid(row=0, column=0, sticky="nsew")

# angka = ttk.Label(window,text="0")
# angka.grid(row=0, column=1)

# btnKurang = ttk.Button(window,text="-")
# btnKurang.grid(row=0, column=2, sticky="nsew")

# window.mainloop()