import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Rajasuku@16",
    database="k20yr"
    )

mycursor = db.cursor()

sql = "SELECT * FROM customers WHERE address Like '%way%'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)












