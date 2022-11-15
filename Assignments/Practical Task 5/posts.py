#Import mysql connector
import mysql.connector

#Connect to database named sm_app
smdb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="",
                               database="sm_app")
executor = smdb.cursor()
#Declare userRecord to create table named posts
userRecord = """create table posts(
    id int (11) auto_increment not null,
    title varchar (60),
    description varchar (255),
    user_id int (11),
    primary key (id),
    foreign key (user_id) references users (id)
    )"""
#Execute the command
executor.execute(userRecord)
#Close Connection
smdb.close()
