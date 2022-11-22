import mysql.connector

carwashdb = mysql.connector.connect(host="localhost", user="root", password="")
print(carwashdb)
