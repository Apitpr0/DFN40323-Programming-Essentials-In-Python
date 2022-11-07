import mysql.connector

carwashdb = mysql.connector.connect(host="localhost",
                                    user="root",
                                    password="",
                                    database="carwash")

executor = carwashdb.cursor()