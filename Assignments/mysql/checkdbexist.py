'''
list all
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="")
mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)
'''
'''
check one by one
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="",database="dbContoh")
'''