import mysql.connector

carwashdb = mysql.connector.connect(host="localhost", user="root", password="")
executor = carwashdb.cursor()
executor.execute("CREATE DATABASE carwash")