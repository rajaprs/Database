import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Rajasuku@16",
    database="k20yk"
    )

mycursor = db.cursor()
sql ='''CREATE TABLE customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    address VARCHAR(255)
)'''
mycursor.execute(sql)




