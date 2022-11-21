#Import mysql connector
import mysql.connector

#connect to 'carwash' db
carwashdb = mysql.connector.connect(host="localhost",
                                    user="root",
                                    password="",
                                    database="carwash")

#Declare cursor() to executor
executor = carwashdb.cursor()
#Create tabe carRecord
carRecord = """CREATE TABLE custInfo(
    CARTYPE VARCHAR (6) NOT NULL,
    PLATE_NUMBER VARCHAR (10) NOT NULL,
    MODEL VARCHAR (100),
    OWN_NAME VARCHAR (255),
    OWN_PHN VARCHAR (12),
    OWN_EMAIL VARCHAR (60),
    WASH_TYPE VARCHAR (20),
    WASH_PRICE INT,
    PRIMARY KEY (PLATE_NUMBER)
)"""
#Execute the sql statement
executor.execute(carRecord)
#Close db connection
carwashdb.close()
