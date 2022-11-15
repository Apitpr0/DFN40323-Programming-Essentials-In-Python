#Import mysql connector
import mysql.connector

#Connect to database named sm_app
smdb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="",
                               database="sm_app")
executor = smdb.cursor()

#Insert multiple sql exec at once
comm = "INSERT INTO posts (title,description) VALUES (%s,%s)"
val = [("Bookeeping", "Use a book"), ("How to cook", "Use Fire"),
       ("How to eat", "Use Hands"), ("How to kill a bird", "Use Knife")]

#Exec more then one command
executor.executemany(comm, val)
#Confirm the changes
smdb.commit()
#show how much record are inserted
print(executor.rowcount, "Record inserted")
