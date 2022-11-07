# Jawaban Nomor 5 :
import os 
class waktu():

    def __init__(self,jam,menit,detik):
        self.jm = jam
        self.mnt = menit
        self.dtk = detik

def inputDt():
    print(f"{'Waktu':=^30}")
    jam = int(input("Jam : "))
    menit = int(input("Menit : "))
    detik = int(input("Detik : "))
    return jam,menit,detik

def tampil():
    os.system("clear")
    print("NOMOR 5")
    jam,menit,detik = inputDt()
    if jam <= 24 and menit <= 59 and detik <= 59:    
        wktu = waktu(jam,menit,detik)
        print(f"\n{'Jam':^10} {'Menit':^10} {'Detik':^10}")
        print(f"{'{}':^10}:{'{}':^10}:{'{}':^10}".format(wktu.jm,wktu.mnt,wktu.dtk))
    else:
        print("Format Input Salah")
    print(f"\n{'Akhir Program':=^30}")
tampil()