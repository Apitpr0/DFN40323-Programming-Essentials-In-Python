import mysql.connector

carwashdb = mysql.connector.connect(host="localhost",
                                    user="root",
                                    password="",
                                    database="carwash")
executor = carwashdb.cursor()

print("")
executor.execute("SELECT  * FROM custinfo")
result = executor.fetchall()

for x in result:
    print(x)
