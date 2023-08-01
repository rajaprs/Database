import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Rajasella@16",
    database="KIETW"
    )

mycursor = db.cursor()

mycursor.execute("ALTER TABLE KIET_CSE ADD COLUMN id1 INT")






