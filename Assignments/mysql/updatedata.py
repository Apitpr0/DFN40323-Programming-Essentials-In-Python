import mysql.connector

mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="",
                               database="dbContoh")

mycursor = mydb.cursor()

sql = "UPDATE student SET course='DDT',dept='JTMK' WHERE matricno='01DKE21F1002'"

mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")
