import mysql.connector

mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="",
                               database="dbContoh")

mycursor = mydb.cursor()
studentRecord = """CREATE TABLE STUDENT(
    NAME VARCHAR (100) NOT NULL,
    COURSE VARCHAR (10),
    DEPT VARCHAR(10),
    MATRICNO VARCHAR (12) NOT NULL,
    PRIMARY KEY (MATRICNO)
)"""

mycursor.execute(studentRecord)
mydb.close()