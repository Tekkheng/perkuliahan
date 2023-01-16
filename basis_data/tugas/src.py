class Jam :
    def __init__(self,jam,menit,detik):
        self.jm = jam
        self.mnt = menit
        self.dtk = detik 

def hasil():
    jam = int(input("Jam : "))
    menit = int(input("Menit : "))
    detik = int(input("Detik: "))
    return jam,menit,detik

def tampil():
    while True : 
        [jam,menit,detik] = hasil()
        if jam <=24 and menit <= 59 and detik <= 59:
            fJam = Jam(jam,menit,detik) 
            print("Tugas Jam".center(30,"="))
            print("""
            Jam : {}
            Menit : {}
            Detik : {}
            """.format(fJam.jm,fJam.mnt,fJam.dtk))
            print("=".center(30,"="))
            break
        else: 
            print("Format Input Salah\n")
    
tampil()