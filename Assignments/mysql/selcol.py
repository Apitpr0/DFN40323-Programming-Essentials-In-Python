import mysql.connector

mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="",
                               database="dbContoh")

mycursor = mydb.cursor()

print("Displaying all data: ")
mycursor.execute("SELECT name, course FROM student")
result = mycursor.fetchall()

for x in result:
    print(x)