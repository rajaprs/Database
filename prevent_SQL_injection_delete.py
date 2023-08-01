import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Rajasuku@16",
    database="prs"
    )

mycursor = db.cursor()

sql = "DELETE FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

db.commit()

print(mycursor.rowcount, "record(s) deleted")

















