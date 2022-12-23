import tkinter as tk
from tkinter import ttk
# from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
import os
import database_garden as db

window = tk.Tk()
window.title("Tugas PBO - Tek Kheng - 20210801205")
window.configure(bg="DarkSlateGrey")
window.geometry("450x500")
window.resizable(False,False)

class Plant:
    frm = ttk.Frame(window,padding="10")
    frm.pack(padx=60,fil="x",expand=True)
    
    def __init__(self):
        self.__status = 0
        self.__AirDipakai = 0
        self.__PupukDipakai = 0
        self.__level = 0

        self.__jumlahAir = 0
        self.__jumlahPupuk = 0

        self.__statusTumbuh = "Benih"
        self.__imgPlant = "Benih.png"
        self.__condition = False

    @property
    def tampilImage(self):
        self.src_img = Image.open(f"img/{self.getImage}").resize((50, 50), Image.ANTIALIAS)
        self.img_plant = ImageTk.PhotoImage(self.src_img)
        return self.img_plant

    @property
    def getImage(self):
        return self.__imgPlant

    @property
    def getAirDipakai(self):
        return self.__AirDipakai

    @property
    def getJumlahAir(self):
        return self.__jumlahAir

    @property
    def TambahJumlahAir(self):
        self.__jumlahAir += 1

    @property
    def getPupukDipakai(self):
        return self.__PupukDipakai

    @property
    def getJumlahPupuk(self):
        return self.__jumlahPupuk

    @property
    def TambahJumlahPupuk(self):
        self.__jumlahPupuk += 1
    
    @property
    def getStatusTumbuh(self):
        return self.__statusTumbuh

    @property
    def setStatusBerbunga(self):
        self.__statusTumbuh = "Berbunga"
        self.__imgPlant = "Berbunga.png"
        self.__level = "Max"

    @property
    def tampilData(self):
        return "Level : {}\nStatus Tanaman : {}\nBeri Air : {}/3 \nBeri Pupuk : {}/1\n\nJumlah Air : {}\nJumlah Pupuk :{}".format(self.__level,self.__statusTumbuh,self.__AirDipakai,self.__PupukDipakai,self.__jumlahAir,self.__jumlahPupuk)

    @property
    def getDataToko(self):
        return "Jumlah Air : {}\nJumlah Pupuk : {}".format(self.__jumlahAir,self.__jumlahPupuk)

    def beriAir(self):
        self.__AirDipakai += 1
        self.__jumlahAir -= 1
        self.cek_kondisi_tumbuh()
    
    def beriPupuk(self):
        self.__PupukDipakai += 1
        self.__jumlahPupuk -= 1
        self.cek_kondisi_tumbuh()

    def cek_kondisi_tumbuh(self):
        if self.__status < 4:
            if self.__AirDipakai >= 3 and self.__PupukDipakai >= 1 :
                self.tumbuh()

    def tumbuh(self):
        self.__AirDipakai -= 3
        self.__PupukDipakai -= 1
        self.__status += 1
        self.__level += 1
        self.__statusTumbuh = self.getStatusTumbuhText()
        self.__imgPlant = self.getStatusTumbuhText() + ".png"

    def getStatusTumbuhText(self):
        if self.__status == 0:
            return "Benih"
        elif self.__status == 1:
            return "Tunas"
        elif self.__status == 2:
            return "Tanaman Kecil"
        elif self.__status == 3:
            return "Tanaman Besar"
        return "Berbunga"
    
    @property
    def getCondition(self):
        return self.__condition 
    @property
    def setCondition(self):
        self.__condition = True

class Anggrek(Plant):
    def __init__(self,jenis_bunga):
        super().__init__()
        self.__jenis = jenis_bunga

    def getJenis(self):
        return self.__jenis

class Mawar(Plant):
    def __init__(self,jenis_bunga):
        super().__init__()
        self.__jenis = jenis_bunga
    
    def getJenis(self):
        return self.__jenis

class Melati(Plant):
    def __init__(self,jenis_bunga):
        super().__init__()
        self.__jenis = jenis_bunga
  
    def getJenis(self):
        return self.__jenis

bunga_anggrek = Anggrek("Anggrek")
bunga_mawar = Mawar("Mawar")
bunga_melati = Melati("Melati")

def aksi(dataShow,label_tunas,jenis,btn,info):
    if jenis.getStatusTumbuh != "Tanaman Besar" and jenis.getStatusTumbuh != "Berbunga":
        if "1.Beri Air" in btn["text"]:
            if jenis.getJumlahAir > 0:
                if jenis.getAirDipakai < 3 :
                    jenis.beriAir()
                    info["text"] = ""
                else:
                    info["text"] = "Info : Air Sudah Cukup!"
            else:
                info["text"] = "Jumlah Air 0, beli dulu di Toko Garden!"

        elif "2.Beri Pupuk" in btn["text"]:
            if jenis.getJumlahPupuk > 0:
                if jenis.getPupukDipakai < 1:
                    jenis.beriPupuk()
                    info["text"] = ""
                else:
                    info["text"] = "Info : Pupuk Sudah Cukup!"
            else:
                info["text"] = "Jumlah Pupuk 0, beli dulu di Toko Garden!"
    else:
        jenis.setStatusBerbunga
        info["text"] = f"{jenis.getJenis()} Sudah Besar! silahkan urus tanaman Lainnya"
        
        if jenis.getCondition == False:
            db.insertData(jenis.getJenis(),jenis.getStatusTumbuh) 
            return jenis.setCondition

    dataShow["text"] = f"{jenis.tampilData}"
    label_tunas["image"] = f"{jenis.tampilImage}"

def aksi_Toko(jenis,Data,info,btn):
    if "1.Membeli Air" in btn["text"]:
        if jenis.getJumlahAir < 9:
            jenis.TambahJumlahAir
            info["text"] = f""
        else:
            info["text"] = "Jumlah Air Maksimal 9"
    elif "2.Membeli Pupuk" in btn["text"]:
        if jenis.getJumlahPupuk < 3:
            jenis.TambahJumlahPupuk
            info["text"] = f""
        else:
            info["text"] = "Jumlah Pupuk Maksimal 3"
    Data["text"] = f"{jenis.getDataToko}"

def TokoGarden(jenis,*data):
    for i in data:
        i.destroy()

    frm = Plant.frm
    judul = ttk.Label(frm,text=f"Toko Tanaman {jenis.getJenis()} ")
    judul.pack(padx="10",pady="10",fil="x",expand=True)

    info = ttk.Label(frm,text="")
    info.pack(padx="10",pady="5",fil="x",expand=True)
    
    Data = ttk.Label(frm,text=f"{jenis.getDataToko}")
    Data.pack(padx="10",pady="5",fil="x",expand=True)

    btn_beliAir = ttk.Button(frm,text="1.Membeli Air",command=lambda : aksi_Toko(jenis,Data,info,btn_beliAir))
    btn_beliAir.pack(padx=10,pady=5,fil="x",expand=True)

    btn_beliPupuk = ttk.Button(frm,text="2.Membeli Pupuk",command=lambda : aksi_Toko(jenis,Data,info,btn_beliPupuk))
    btn_beliPupuk.pack(padx=10,pady=5,fil="x",expand=True)

    btn_back = ttk.Button(frm,text="3.Back",command=lambda:pilihBunga(jenis,judul,info,Data,btn_beliAir,btn_beliPupuk,btn_back))
    btn_back.pack(padx=10,pady=5,fil="x",expand=True)

def pilihBunga(jenis,*data):  
    for i in data:
        i.destroy()

    frm = Plant.frm
    judul2 = ttk.Label(frm,text=f"Menu Method {jenis.getJenis()} ")
    judul2.pack(padx="10",pady="10",fil="x",expand=True)

    info = ttk.Label(frm,text="")
    info.pack(padx="10",pady="5",fil="x",expand=True)
    
    label_tunas = ttk.Label(frm,image=jenis.tampilImage)
    label_tunas.pack(padx="10",pady="5",fil="x",expand=True)

    dataShow = ttk.Label(frm,text=f"{jenis.tampilData}")
    dataShow.pack(padx="10",pady="5",fil="x",expand=True)

    btn_beriAir = ttk.Button(frm,text="1.Beri Air",command=lambda: [aksi(dataShow,label_tunas,jenis,btn_beriAir,info)])
    btn_beriAir.pack(padx=10,pady=5,fil="x",expand=True)

    btn_beriPupuk = ttk.Button(frm,text="2.Beri Pupuk",command=lambda : aksi(dataShow,label_tunas,jenis,btn_beriPupuk,info))
    btn_beriPupuk.pack(padx=10,pady=5,fil="x",expand=True)

    btn_Toko = ttk.Button(frm,text="3.Toko Garden",command=lambda : TokoGarden(jenis,label_tunas,judul2,btn_beriAir,btn_beriPupuk,btn_Toko,btn_exit2,info,dataShow))
    btn_Toko.pack(padx=10,pady=5,fil="x",expand=True)

    btn_exit2 = ttk.Button(frm, text="4.Exit",command=lambda: [main(label_tunas,judul2,btn_beriAir,btn_beriPupuk,btn_Toko,btn_exit2,info,dataShow)])
    btn_exit2.pack(padx=10,pady=5,fill="x",expand=True)

def main(*data):
    if data:
        for i in data:
            i.destroy()

    frm = Plant.frm

    judul = ttk.Label(frm,text="Pilih Bunga")
    judul.pack(padx="10",pady="10",fil="x",expand=True)

    btn_anggrek = ttk.Button(frm,text="1.Anggrek",command=lambda: [pilihBunga(bunga_anggrek,judul,btn_anggrek,btn_mawar,btn_melati,btn_exit)])
    btn_anggrek.pack(padx=10,pady=5,fil="x",expand=True)

    btn_mawar = ttk.Button(frm,text="2.Mawar",command=lambda: [pilihBunga(bunga_mawar,judul,btn_anggrek,btn_mawar,btn_melati,btn_exit)])
    btn_mawar.pack(padx=10,pady=5,fil="x",expand=True)

    btn_melati = ttk.Button(frm,text="3.Melati",command=lambda: [pilihBunga(bunga_melati,judul,btn_anggrek,btn_mawar,btn_melati,btn_exit)])
    btn_melati.pack(padx=10,pady=5,fil="x",expand=True)

    btn_exit = ttk.Button(frm, text="4.Exit",command=window.destroy)
    btn_exit.pack(padx=10,pady=5,fill="x",expand=True)

    window.mainloop()

if __name__ == "__main__":
    os.system("clear")
    main()





