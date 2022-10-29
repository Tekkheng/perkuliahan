# class Abc:
#     def __init__(self,jnis):
#      self.jenis = jnis

#     def data(self):
#         print("hello",self.jenis)

# a = Abc("roda empat")
# print(a.__dict__)

# a.data()

#====================================================================================================
# class Product:
#     # __init__() adalah metode konstruktor :
#     # Method untuk Setter
#     def __init__(self, productID, productName,price,qty):
#         self.mProductID = productID
#         self.mProductName = productName
#         self.mPrice = price
#         self.mQuantity = qty

# # Isi data dalam method Setter
# a = Product(0,"Aqua Botol",4000,23)

# # Method Getter
# print("IdProduct  NamaProduk  Harga  Jumlah")
# print("  {}\t  {}\t{}\t{}".format( a.mProductID, a.mProductName, a.mPrice, a.mQuantity))

#====================================================================================================
# class Product:
#     # __init__ => Merupakan Method Konstruktor
#     # Method untuk Setter
#     def __init__(self,id,produk,harga,jumlah):
#         self. id_Product = id 
#         self. Product = produk
#         self. Price = harga
#         self. Quantity = jumlah 
    
# # Isi data ke dalam method Setter
# Data_Produk = Product(0, "Aqua Botol",4000,23)

# # Method untuk Getter
# print("Id_Produk : {}\nNama_Produk : {}\nHarga : {}\nJumlah : {} ".format( Data_Produk.id_Product, Data_Produk.Product, Data_Produk.Price, Data_Produk.Quantity))

#====================================================================================================

# class Product:
#     # __init__ => Merupakan Method Konstruktor
#     # Method untuk Setter
#     def __init__(self,id,produk,harga,jumlah):
#         self. id_Product = id 
#         self. Product = produk
#         self. Price = harga
#         self. Quantity = jumlah 
    
#     # Method untuk Getter
#     def tampil_data(self):
#         print(f"""
#         Id_Produk : {self.id_Product}
#         Nama_Produk : {self.Product}
#         Harga : {self.Price}
#         Jumlah : {self.Quantity}
#         """)
# # Isi data ke dalam method Setter
# Data_Produk = Product(0, "Aqua Botol",4000,23)

# Data_Produk.tampil_data()

#====================================================================================================


class Product:
    # __init__ => Merupakan Method Konstruktor
    # Method untuk Setter
    def __init__(self,ID_Produk,Nama_Produk,Harga,Jumlah):
        self.IDProduk = ID_Produk 
        self.Nama_Produk = Nama_Produk
        self.Harga = Harga
        self.Jumlah = Jumlah 

# Isi data dalam method Setter
a = Product(0,"teh Botol",1323,445)

# Method untuk Getter
print("Id_Produk : {}\nNama_Produk : {}\nHarga : {}\nJumlah : {} "
.format( a.IDProduk, a.Nama_Produk, a.Harga, a.Jumlah))
