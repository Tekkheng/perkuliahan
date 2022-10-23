# Tek kheng - 20210801205 (Tugas PBO Pert5)
class Product:
    # __init__ => Merupakan Method Konstruktor
    # Method untuk Setter
    def __init__(self,id,produk,harga,jumlah):
        self.id_Product = id 
        self.Product = produk
        self.Price = harga
        self.Quantity = jumlah 

# Isi data dalam method Setter
Data_Produk = Product(0,"Aqua Botol",4000,23)

# Method untuk Getter
print("Id_Produk : {}\nNama_Produk : {}\nHarga : {}\nJumlah : {} "
.format( Data_Produk.id_Product, Data_Produk.Product, Data_Produk.Price, Data_Produk.Quantity))
