import os

class Plant:
    def __init__(self):
        self.statusTumbuh = 0
        self.jumlahAir = 0
        self.jumlahPupuk = 0

    def beriAir(self,aksi):
        self.jumlahAir = aksi.jumlahAir + 1
    
    def beriPupuk(self,aksi):
        self.jumlahPupuk = aksi.jumlahPupuk + 1
    
    def status(self,aksi):
        self.jumlahAir = aksi.jumlahAir - 3
        self.jumlahPupuk = aksi.jumlahPupuk - 2
        self.statusTumbuh = aksi.statusTumbuh + 1

anggrek = Plant()
mawar = Plant()
melati = Plant()

def tumbuh(status,jenis):
    if status < 3 :
        jenis.status(jenis)

def cekKondisiTumbuh(jumlahAir,jumlahPupuk,status,jenis,bunga):
    if jumlahAir >=3 and jumlahPupuk >=2:
        tumbuh(status,jenis)
        
def header(text,*args):
    print(f"{text:=^40}")
    [print(f"{no+1:>16}.{i}") for no,i in enumerate([*args])]
    print("=".center(40,"="))

def tampil(*data):
    print(f"Status : {statusPlant(data[0])}")
    print(f"Jumlah Air : {data[1]}")
    print(f"Jumlah Pupuk : {data[2]}")

def statusPlant(status):
    match status:
        case 0: return "Benih"
        case 1: return "Tunas"
        case 2: return "Tanaman Kecil"
        case 3: return "Tanaman Dewasa"

def c_aksi(bunga,jenis):
    while True:
        match so:
            case "posix" : os.system("clear")
            case "nt" : os.system("cls")
        header(bunga,"Beri Air","Beri Pupuk","Exit")
        print("")

        status = jenis.statusTumbuh
        jumlahAir = jenis.jumlahAir
        jumlahPupuk = jenis.jumlahPupuk
        tampil(status,jumlahAir,jumlahPupuk)
        cekKondisiTumbuh(jumlahAir,jumlahPupuk,status,jenis,bunga)
        
        if jumlahAir != 3 or jumlahPupuk != 2:
            pil = int(input("\nPilih : "))
        else:
            s=input("\nStatus Plant Meningkat! enter: ")

        if status < 3:
            if pil == 1:
                if jumlahAir <=2:
                    jenis.beriAir(jenis)
            elif pil == 2:
                if jumlahPupuk <=1:
                    jenis.beriPupuk(jenis)
            elif pil == 3:
                break
        else:
            print("Tanaman Sudah Dewasa !!!")
            e = input("Enter : ")
            break

def pil_plant(p):
    if p == 1:
        c_aksi("Anggrek",anggrek)
    elif p == 2:
        c_aksi("Mawar",mawar)
    elif p == 3:
        c_aksi("Melati",melati)
    elif p == 4:
        return False

if __name__ == "__main__":
    so = os.name
    match so:
        case "posix" : os.system("clear")
        case "nt" : os.system("cls")
    while True:
        match so:
            case "posix" : os.system("clear")
            case "nt" : os.system("cls")

        header("Plant","Anggrek","Mawar","Melati","Exit")
        p = int(input("\nPilih 1-4 : "))

        if pil_plant(p) == False:
            break