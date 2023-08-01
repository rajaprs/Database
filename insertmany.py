import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Rajasella@16",
    database="KIETW"
    )

mycursor = db.cursor()

sql = "INSERT INTO KIET_CSE (Rno, Name, Branch, Percentage, Email, MobileNo) VALUES (%s,%s, %s, %s, %s, %s)"
val = [
 ("01", "Anju", "ECE", "56", "abc@gmail.com", "1234565432"),
 ("02", "Kanwal", "ECE", "80", "abc@gmail.com", "1234565432"),
 ("03", "Sonu", "CSE", "85", "abc@gmail.com", "1234565432"),
 ("04", "Arun", "CSE", "83", "abc@gmail.com", "1234565432"),
 ("05", "Ravi", "CSE", "78", "abc@gmail.com", "1234565432"),
 ("06", "Anjali", "CSE", "65", "abc@gmail.com", "1234565432"),
 ("07", "Kesavan", "EEE", "95", "abc@gmail.com", "1234565432"),
 ("08", "Anu", "CSE", "55", "abc@gmail.com", "1234565432"),
 ]
mycursor.executemany(sql, val)
db.commit()
print(mycursor.rowcount, "record was inserted.")








