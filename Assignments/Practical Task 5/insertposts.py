#Import mysql connector
import mysql.connector

#Connect to database named sm_app
smdb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="",
                               database="sm_app")
executor = smdb.cursor()

#Insert multiple sql exec at once
comm = "INSERT INTO posts (ID, TITLE, DESCRIPTION, USER_ID) VALUES (%s, %s, %s, %s)"
val = [(111, "Anda Mahu Makan?", "Makanan", 1),
       (112, "Anda Mahu Tidur?", "Tidur", 2),
       (115, "Anda Lapar?", "Masak Nasik", 3),
       (114, "Anda mahu jadi pro?", "training ah", 4)]

#Exec more then one command
executor.executemany(comm, val)
#Confirm the changes
smdb.commit()
#show how much record are inserted
print(executor.rowcount, "Record inserted")
