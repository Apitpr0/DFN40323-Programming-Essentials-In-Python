#Import mysql connector
import mysql.connector

#Connect to database named sm_app
smdb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="",
                               database="sm_app")
executor = smdb.cursor()
#Declare userRecord to create table named likes
userRecord = """create table likes(
    id int (11)auto_increment not null,
    user_id int(11),
    post_id int(11),
    primary key(id),
    foreign key(post_id) references posts(id),
    foreign key(user_id) references users(id)
    )"""
#Execute the command
executor.execute(userRecord)
#Close the connection
smdb.close()
