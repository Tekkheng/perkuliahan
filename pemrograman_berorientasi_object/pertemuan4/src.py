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