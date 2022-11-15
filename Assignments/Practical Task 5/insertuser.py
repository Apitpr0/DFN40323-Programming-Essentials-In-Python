#Import mysql connector
import mysql.connector

#Connect to database named sm_app
smdb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="",
                               database="sm_app")
executor = smdb.cursor()

#Insert multiple sql exec at once
comm = "INSERT INTO users (name,age,gender,nationality) VALUES (%s,%s,%s,%s)"
val = [("Abu", 19, "Male", "Malaysian"), ("Zaid", 20, "Male", "Indian"),
       ("Chong", 30, "Male", "Chinese"), ("Zalya", 25, "Female", "Malaysian")]

#Exec more then one command
executor.executemany(comm, val)
#Confirm the changes
smdb.commit()
#show how much record are inserted
print(executor.rowcount, "Record inserted")
