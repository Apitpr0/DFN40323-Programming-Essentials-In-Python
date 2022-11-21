#Import mysql connector
import mysql.connector
#connect to 'carwash' db

carwashdb = mysql.connector.connect(host="localhost",
                                    user="root",
                                    password="",
                                    database="carwash")
#Declare cursor() to executor
executor = carwashdb.cursor()

#Sum wash_price for gross income
executor.execute("SELECT SUM(WASH_PRICE) FROM custinfo")

#Output the total
print("Gross income for today is RM", executor.fetchall()[0][0])
