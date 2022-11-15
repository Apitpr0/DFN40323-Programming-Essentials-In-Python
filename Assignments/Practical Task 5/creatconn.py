#Import mysql connector
import mysql.connector

#declare smdb and check connection to db
smdb = mysql.connector.connect(host="localhost", user="root", password="")
#print the result
print(smdb)
