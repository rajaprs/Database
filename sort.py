import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Rajasuku@16",
    database="k20yk"
    )

mycursor = db.cursor()

sql = "SELECT * FROM customers ORDER BY name "

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)














