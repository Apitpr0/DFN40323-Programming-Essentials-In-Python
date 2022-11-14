import mysql.connector

carwashdb = mysql.connector.connect(host="localhost",
                                    user="root",
                                    password="",
                                    database="carwash")
plate_number = input("Enter plate number to delete:")
executor = carwashdb.cursor()

delinf = "DELETE FROM custinfo WHERE PLATE_NUMBER  = plate_number"

executor.execute(delinf)
carwashdb.commit()
print(executor.rowcount, "record(s) delete")