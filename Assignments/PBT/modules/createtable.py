import mysql.connector

carwashdb = mysql.connector.connect(host="localhost",
                                    user="root",
                                    password="",
                                    database="carwash")

executor = carwashdb.cursor()
carRecord = """CREATE TABLE custInfo(
    CARTYPE VARCHAR (6) NOT NULL,
    PLATE_NUMBER VARCHAR (10) NOT NULL,
    MODEL VARCHAR (100),
    OWN_NAME VARCHAR (255),
    OWN_PHN VARCHAR (12),
    OWN_EMAIL VARCHAR (60),
    PRIMARY KEY (PLATE_NUMBER)
)"""

executor.execute(carRecord)
carwashdb.close()