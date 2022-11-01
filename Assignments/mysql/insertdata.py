import mysql.connector

mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="",
                               database="dbContoh")

mycursor = mydb.cursor()
mycursor.execute(
    "INSERT INTO student(name,course,dept,matricno) VALUES (%s,%s,%s,%s)",
    ('Muhammad Haziq Zafran Bin Mohd Khairi', 'DDT', 'JTMK', '01DDT21F1001'))

mydb.commit()
print(mycursor.rowcount, "record inserted")
