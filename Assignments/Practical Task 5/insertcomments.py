#Import mysql connector
import mysql.connector

#Connect to database named sm_app
smdb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="",
                               database="sm_app")
executor = smdb.cursor()

#Insert multiple sql exec at once
comm = "INSERT INTO comments (ID, TEXT, USER_ID, POST_ID) VALUES (%s, %s, %s, %s)"
val = [(561, "Ko nak makan apa?", 1, 111), (566, "Tido kat ane?", 2, 112),
       (571, "Training apa tu miska?", 3, 114),
       (545, "Nasi je ke, lauknya mana?", 4, 115)]

#Exec more then one command
executor.executemany(comm, val)
#Confirm the changes
smdb.commit()
#show how much record are inserted
print(executor.rowcount, "Record inserted")
