import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Rajasuku@16",
    database="KIET_ECE"
    )

mycursor = db.cursor()

sql = "DELETE FROM KIET_ece WHERE Name = 'Raju'"

mycursor.execute(sql)

db.commit()

print(mycursor.rowcount, "record(s) deleted")
