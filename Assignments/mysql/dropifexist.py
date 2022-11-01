import mysql.connector

mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="",
                               database="dbContoh")
mycursor = mydb.cursor()
mycursor.execute("DROP TABLE IF EXIST STUDENT")