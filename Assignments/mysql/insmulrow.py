
import mysql.connector

mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="",
                               database="dbContoh")

mycursor = mydb.cursor()

sql = "INSERT INTO student (name,course,dept,matricno) VALUES (%s,%s,%s,%s)"

val = [("Ali Bin Abu", "DKE", "JKE", "01DKE21F1001"),
       ("Amy Mastura Binti Musa", "DKE", "JKE", "01DKE21F100M"),
       ("Heliza Binti Hilmi", "DKM", "JKM", "01DKM21F1001"),
       ("Vincent A/L Richard", "DKM", "JKM", "01DKM21F1002")]

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "Record inserted")
