import os
# function buatan :
# function tampilData dengan parameter nama,nim yang diterima dari argument yg dikirimkan
def tampilData(nama,nim):
  print(f"\n{'Data':=^20}")
  print(f"Nama : {nama}\nNim : {nim}")
  print("="*20)

# function inputan
def inputan():
    os.system("clear")
    nama = input("Nama : ")
    while True:
      os.system("clear")
      print(f"Nama : {nama}")
      try:
        nim = int(input("Nim : "))
        return nama,nim
      except:
        print("Nim harus Angka! ")
        e=input("enter: ")

# function main
def main():
  # memanggil function inputan untuk digunakan
  nama,nim = inputan()
  # memanggil function tampilData dengan mengirimkan argument nama dan nim
  tampilData(nama,nim)

  # contoh memanggil function sum yg sudah disediakan :
  a = [6,7,2,3,9,8]
  h = sum(a)
  print(h)
  # output = 35

# memanggil function main
main()