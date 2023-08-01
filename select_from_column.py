import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Rajasuku@16",
    database="k20yk"
    )

mycursor = db.cursor()

mycursor.execute("SELECT name, address FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)










