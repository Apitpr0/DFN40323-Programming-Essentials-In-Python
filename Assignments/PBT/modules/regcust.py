#Import mysql connector
import mysql.connector
#connect to 'carwash' db
carwashdb = mysql.connector.connect(host="localhost",
                                    user="root",
                                    password="",
                                    database="carwash")

#Ask input for db
cartype = input("Car Type [MPV/SUV/SEDAN]:")
plate_number = input("Car Plate Number:")
model = input("Car Model:")
own_name = input("Owner's Name:")
own_phn = input("Owner's Phone Number:")
own_email = input("Owner's Email:")

#Declare cursor() to executor
executor = carwashdb.cursor()
#Insert all data from user input to db
executor.execute(
    "INSERT INTO custInfo(CARTYPE,PLATE_NUMBER,MODEL,OWN_NAME,OWN_PHN,OWN_EMAIL) VALUES (%s,%s,%s,%s,%s,%s)",
    (cartype, plate_number, model, own_name, own_phn, own_email))

#Confirm the changes
carwashdb.commit()
print("Customer Record Inserted into the system")
