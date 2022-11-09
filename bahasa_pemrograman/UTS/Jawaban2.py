"""
JAWABAN NOMOR 2
"""
def inputDt():
    alas = float(input("Masukkan Alas : "))
    tinggi = float(input("Masukkan Tinggi : "))
    return alas,tinggi

def hitung():
    alas,tinggi = inputDt()
    luas = float(1/2 *alas * tinggi)
    return luas

def main():
    print("MENGHITUNG LUAS SEGITIGA")
    luas = hitung()
    print(f"Luas = {luas}")
main()