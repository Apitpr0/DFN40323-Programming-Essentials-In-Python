#Import mysql connector
import mysql.connector

#Connect to databased named sm_app
smdb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="",
                               database="sm_app")
executor = smdb.cursor()
#Declare userRecord to create table named comments
userRecord = """
create table comments(
    id int(11) auto_increment not null,
    text varchar(255),
    user_id int(11),
    post_id int(11),
    primary key (id),
    foreign key (post_id) references posts (id),
    foreign key (user_id) references users (id) 
)"""
#Execute the command
executor.execute(userRecord)
#Close the connection
smdb.close()



