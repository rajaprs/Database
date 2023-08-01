import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Rajasella@16",
    database="KIETW"
    )

mycursor = db.cursor()

sql = "INSERT INTO KIET_CSE (Rno, Name, Branch,Percentage, Email, MobileNo) VALUES (%s, %s, %s, %s, %s, %s)"
val = ("61", "Sameera", "CSE", "72",
       "asd@gmail.com", "1234567890")

mycursor.execute(sql, val)

db.commit()

print(mycursor.rowcount, "record inserted.")







