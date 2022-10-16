# =================== Soal Nomor 1 - Menghitung Usia ===================
def hitung_usia():
    tahun_sekarang = 2022
    tahun_lahir = 2002
    umur = tahun_sekarang - tahun_lahir

    return tahun_sekarang,tahun_lahir,umur

tahun_sekarang,tahun_lahir,umur = hitung_usia()

def data():
    print("Soal Nomor 1")
    print("=====================================")
    print("Tahun Sekarang : ",tahun_sekarang)
    print("Tahun Lahir : ", tahun_lahir)
    print("Umur Anda : ",umur)
    print("=====================================")
data()
# ======================================================================

# =========== Soal Nomor 2 - Menghitung PPN 10% Total Belanja ===========
def hitung():
    print("Soal Nomor 2")
    harga_belanja = int(input("Harga Belanja : "))
    ppn = 0.10 #10%
    total_ppn = harga_belanja * ppn
    hasil = float(harga_belanja + total_ppn)
    return harga_belanja,ppn,hasil,total_ppn

harga_belanja,ppn,hasil,total_ppn = hitung()

def printDat():
    print("------------------------")
    print("Total PPN : ",total_ppn)
    print("Total Belanja : ",hasil)

printDat()
# =========================================================================