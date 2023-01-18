import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  port=23306,
  user="root",
  password="p455w0rd",
  database="Tekkheng_Garden"
)

db = mydb.cursor()
db.execute("SHOW DATABASES")

for i in db:
    print(i)
