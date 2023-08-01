import mysql.connector
conn=mysql.connector.connect(host="localhost", user="root", passwd="Rajasuku@16")
c=conn.cursor()
c.execute("SHOW DATABASES")
for i in c:
    print(i)
