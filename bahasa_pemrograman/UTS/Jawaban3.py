"""
JAWABAN NOMOR 3
"""
def header():
    print("="*25)
    print("PROGRAM QUIZ")
    print("="*25)

def inputdt():
    nama = input("Masukkan Nama : ")
    nim = int(input("Masukkan Nim : "))
    return nama,nim

def main():
    header()
    nama,nim = inputdt()
    print(f"\nNama : {nama}\nNim : {nim}")
main()