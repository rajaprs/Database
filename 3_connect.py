import mysql.connector
conn=mysql.connector.connect(host="localhost", user="root",
                             password="Rajasella@16")

c=conn.cursor()

c.execute("show databases ")

for i in c:
    print(i)
