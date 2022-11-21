#Import mysql connector
import mysql.connector
#connect to 'carwash' db
carwashdb = mysql.connector.connect(host="localhost",
                                    user="root",
                                    password="",
                                    database="carwash")
#Declare cursor() to executor
executor = carwashdb.cursor()

print("")
#Output all data from custinfo
executor.execute("SELECT  * FROM custinfo")
result = executor.fetchall()

#Print the result
for x in result:
    print(x)
