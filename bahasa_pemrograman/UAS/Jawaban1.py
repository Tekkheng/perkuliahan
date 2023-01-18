"""
Jawaban Nomor 1, Function Rekursif Pada Python
"""

def tampilData(data):
    nim,nama = inputData()
    print(f"\nNim : {nim}\nNama : {nama}")

    data += 1
    print(f"jumlah Data : {data}\n")
    if data < 2:
        tampilData(data)
    else:
        print("Akhir Program")


def inputData():
    nim = input("Masukkan Nim : ")
    nama = input("Masukkan Nama : ")
    return nim,nama

def main():
    data = 0
    tampilData(data)
main()