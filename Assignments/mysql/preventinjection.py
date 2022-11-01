import mysql.connector

mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="",
                               database="dbContoh")

mycursor = mydb.cursor()

sql = "UPDATE student SET course = %s WHERE matricno = %s"
val = ("DJM", "01DKM21F1002")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")