class Abc:
    def __init__(self,jnis):
     self.jenis = jnis

    def data(self):
        print("hello",self.jenis)

a = Abc("roda empat")
print(a.__dict__)

a.data()
