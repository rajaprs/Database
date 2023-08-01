import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Rajasuku@16",
    database="KIET_ECE"
    )

mycursor = db.cursor()

sql ="DROP TABLE KIET_ece"
mycursor.execute(sql)

















