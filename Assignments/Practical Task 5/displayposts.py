#Import mysql connector
import mysql.connector

#Connect to database named sm_app
smdb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="",
                               database="sm_app")
executor = smdb.cursor()

#Execute command to list all posts from db
executor.execute("SELECT * FROM POSTS")
posts_list = executor.fetchall()
print(posts_list)
