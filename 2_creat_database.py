import mysql.connector

mydb=mysql.connector.connect(host="localhost", user="root",
                             passwd="Rajasella@16")

my_cur=mydb.cursor()
my_cur.execute("CREATE DATABASE KIETW")
