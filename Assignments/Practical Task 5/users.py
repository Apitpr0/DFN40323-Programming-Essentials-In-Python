
#Import mysql connector
import mysql.connector

#Connect to database named sm_app
smdb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="",
                               database="sm_app")
executor = smdb.cursor()
#Declare userRecord to create table named users
userRecord = """create table users(
    id int(11) auto_increment not null,
    name varchar(255),
    age int(11),
    gender varchar(7),
    nationality varchar(100),
    primary key(id)
    )"""
#Execute the command
executor.execute(userRecord)
#Close the connection
smdb.close()


