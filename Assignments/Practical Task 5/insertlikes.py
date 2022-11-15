#Import mysql connector
import mysql.connector

#Connect to database named sm_app
smdb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="",
                               database="sm_app")
executor = smdb.cursor()

#Insert multiple sql exec at once
comm = "INSERT INTO likes (ID, USER_ID, POST_ID) VALUES (%s, %s, %s)"
val = [(666, 1, 111), (777, 2, 115), (888, 3, 114), (999, 4, 112)]

#Exec more then one command
executor.executemany(comm, val)
#Confirm the changes
smdb.commit()
#show how much record are inserted
print(executor.rowcount, "Record inserted")
