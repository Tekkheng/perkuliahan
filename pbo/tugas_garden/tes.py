import os
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.configure(bg="DarkSlateGrey")
window.geometry("450x500")
window.resizable(False,False) #=> (x,y)
window.title("Tugas PBO Garden")

frm = ttk.Frame(window, padding=10)
frm.pack(padx=10,fil="x",expand=True)


class Plant:
    def __init__(self,window):
        self.statusText = ttk.Label(frm,text="0")
        self.statusTumbuh = ttk.Label(frm,text="0")
        self.jumlahAir = ttk.Label(frm,text="0")
        self.jumlahPupuk = ttk.Label(frm,text="0")

    def beriAir(self):
        value = int(self.jumlahAir["text"]) 
        self.jumlahAir["text"] = f"{value + 1}"
        print(self.jumlahAir["text"])
        # self.cek_kondisi_tumbuh()
        
    def beriPupuk(self):
        value = int(self.jumlahPupuk["text"]) 
        self.jumlahAir["text"] = f"{value + 1}"
        print(self.jumlahPupuk["text"])
        # self.cek_kondisi_tumbuh()

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

anggrek = Anggrek(window)
mawar = Mawar(window)

def tampil_method():
    btn_anggrek.destroy()
    btn_mawar.destroy()

    btn_beriAir = ttk.Button(frm,text="Beri Air",command=anggrek.beriAir)
    btn_beriAir.pack(padx=10,pady=5,fil="x",expand=True)

    btn_beriPupuk = ttk.Button(frm,text="Beri Pupuk",command=mawar.beriPupuk)
    btn_beriPupuk.pack(padx=10,pady=5,fil="x",expand=True)


btn_anggrek = ttk.Button(frm,text="Anggrek",command=tampil_method)
btn_anggrek.pack(padx=10,pady=5,fil="x",expand=True)

btn_mawar = ttk.Button(frm,text="Mawar",command=tampil_method)
btn_mawar.pack(padx=10,pady=5,fil="x",expand=True)

window.mainloop()




