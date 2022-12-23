
from .koneksi import mydb,db

def insertData(jenis,status):
    try:
        sql = "INSERT INTO tanaman(jenis_tanaman,statusTanaman) VALUES(%s,%s)"
        value = (f"{jenis}",f"{status}")
        db.execute(sql,value)
        mydb.commit()
        print(db.rowcount, "Berhasil insert")
    except:
        print("Gagal Insert ke Database!")
