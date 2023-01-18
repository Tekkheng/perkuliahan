"""
Jawaban Nomor 3, GUI (Graphical User Interface)
"""

import tkinter as tk
from tkinter import ttk

class Count:
    def __init__(self):
        self.__data = 0

    @property
    def getData(self):
        return self.__data

    def tambahData(self):
        if self.__data >= 0:
            self.__data += 1

    def kurangData(self):
        if self.__data >= 0:
            self.__data -= 1
    
    @property
    def tampil(self):
        return f"Counter : {self.getData}"

counter = Count()

def hitung(info,status):
    if "+" in status["text"]:
        if counter.getData >= 0:
            counter.tambahData()
    elif "-" in status["text"]:
        if counter.getData > 0:
            counter.kurangData()
    info["text"] = f"{counter.tampil}"

def main():
    window = tk.Tk()
    window.title("UAS BAHASA PEMROGRAMAN - Tek Kheng - 20210801205")
    window.geometry("500x450")
    window.configure(bg="DarkSlateGrey")
    window.resizable(False,False)
    frm = ttk.Frame(window,padding="10")
    frm.pack(padx=60,fil="x",expand=True)

    info = ttk.Label(frm,text=f"{counter.tampil}")
    info.pack(padx="10",pady="5",fil="x",expand=True)

    tambah = ttk.Button(frm, text = "+")
    tambah = ttk.Button(frm,text="+",command=lambda : hitung(info,tambah))
    tambah.pack(padx="10",pady="5",fil="x",expand=True)

    kurang = ttk.Button(frm, text = "-",command=lambda : hitung(info,kurang))
    kurang.pack(padx="10",pady="5",fil="x",expand=True)

    window.mainloop()

main()