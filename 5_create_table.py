import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Rajasella@16",
    database="KIETW"
    )

c=db.cursor()

sql ='''CREATE TABLE KIET_CSE(
   Rno int not null primary key,
   Name varchar(30) not null,
   Branch CHAR(10),
   Percentage FLOAT,
   Email varchar(50),
   MobileNo int)'''
c.execute(sql)
