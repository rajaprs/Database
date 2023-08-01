import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Rajasella@16",
    database="KIETW"
    )

c=db.cursor()
c.execute("SHOW TABLES")
for i in c:
    print(i)
