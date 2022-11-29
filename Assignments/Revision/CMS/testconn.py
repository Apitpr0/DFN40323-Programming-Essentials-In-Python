import mysql.connector

cms = mysql.connector.connect(host="localhost", username="root", password="")
print(cms)