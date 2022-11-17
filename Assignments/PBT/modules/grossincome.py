import mysql.connector

carwashdb = mysql.connector.connect(host="localhost",
                                    user="root",
                                    password="",
                                    database="carwash")
executor = carwashdb.cursor()

executor.execute("SELECT SUM(WASH_PRICE) FROM custinfo")

print("Gross income for today is RM",executor.fetchall()[0][0])
