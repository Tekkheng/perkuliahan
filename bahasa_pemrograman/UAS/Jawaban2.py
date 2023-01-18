"""
Jawaban Nomor 2, Function of Exception Handling Pada Python
"""

while True:
    try:
        bilangan = int(input("Masukkan angka: "))
        print(f"hasil : {bilangan}")
        break
    
    except:
        print("Input harus angka!")