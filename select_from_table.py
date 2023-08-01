import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Rajasella@16",
    database="KIETW"
    )

mycursor = db.cursor()

mycursor.execute("SELECT * FROM KIET_CSE")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)









