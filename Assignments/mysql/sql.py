import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="bobramen",
    password="123456"
)

print(mydb)