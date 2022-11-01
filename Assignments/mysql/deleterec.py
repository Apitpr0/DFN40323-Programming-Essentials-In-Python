import mysql.connector

mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="",
                               database="dbContoh")

mycursor = mydb.cursor()
sql = "DELETE FROM student WHERE matricno='01DKM21F1002'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")