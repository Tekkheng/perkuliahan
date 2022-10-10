for i in range(1,11):
    print(i,'x',i,'=',i*i)
    if i == 5:
        break
    
def header():
    print("======================")
header()

for i in range(1,11):
    if i == 5:
        continue
    print(i,'x',i,'=',i*i)

def tes(a) :
    nama=print("nama: ",a)
    umur=int(input("umur: "))

tes("akheng")



def input_alas_dan_tinggi ():
  alas = float(input('Masukkan alas: '))
  tinggi = float((input('Masukkan tinggi: ')))

  return alas, tinggi

def hitung_luas (alas, tinggi):
  return 0.5 * alas * tinggi

"""kalau fungsional, kita sendiri yang mengelola
hasil kembaliannya"""

# satu fungsi bisa dipanggil secara independen
#print(hitung_luas(5, 10))

# contoh dengan inputan alas dan tinggi
alas, tinggi = input_alas_dan_tinggi()
print(hitung_luas(alas, tinggi))



def testing():
    listCity = ['Kalimantan', 'Sumatra', 'Sulawesi']
    listPlace = ['West', 'North', 'South']
    for city in listCity:
        for place in listPlace:
            print(city, place)

testing()