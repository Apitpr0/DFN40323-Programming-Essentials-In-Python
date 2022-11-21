#Import mysql connector
import mysql.connector
#Connect to carwash db
carwashdb = mysql.connector.connect(host="localhost",
                                    user="root",
                                    password="",
                                    database="carwash")
#Declare cursor() to executor
executor = carwashdb.cursor()
#Ask user for plate number
plate = input("Enter the plate number that you want to update:")
print("+-------------+------+--------+-----------------+")
print("  | Type of Car | Wash | Vacuum | Wash and Vacuum |")
print("+-------------+------+--------+-----------------+")
print("1.| Sedan       |    8 |      4 |              12 |")
print("2.| MPV         |   12 |      5 |              17 |")
print("3.| SUV         |   13 |      5 |              18 |")
print("+-------------+------+--------+-----------------+")
#Ask user for car type
cartype = int(input("Enter the type of car that you want to update (1/2/3):"))
#Ask user for service type
service = str(
    input(
        "Enter the service that you want to update (Wash/Vacuum/WashVacuum):"))
#If statement for sedan
if cartype == 1:
    if service == "Wash":
        executor.execute(
            "UPDATE custinfo SET WASH_TYPE='WASH',WASH_PRICE=8 WHERE CARTYPE='SEDAN' AND PLATE_NUMBER='%s'"
            % (plate))
        carwashdb.commit()
        print("---------------------RECORD UPDATED---------------------")
    elif service == "Vacuum":
        executor.execute(
            "UPDATE custinfo SET WASH_TYPE='VACUUM',WASH_PRICE=4 WHERE CARTYPE='SEDAN' AND PLATE_NUMBER='%s'"
            % (plate))
        carwashdb.commit()
        print("---------------------RECORD UPDATED---------------------")
    elif service == "WashVacuum":
        executor.execute(
            "UPDATE custinfo SET WASH_TYPE='WASH AND VACUUM',WASH_PRICE=12 WHERE CARTYPE='SEDAN' AND PLATE_NUMBER='%s'"
            % (plate))
        carwashdb.commit()
        print("---------------------RECORD UPDATED---------------------")
#If statement for MPV
if cartype == 2:
    if service == "Wash":
        executor.execute(
            "UPDATE custinfo SET WASH_TYPE='WASH',WASH_PRICE=12 WHERE CARTYPE='MPV' AND PLATE_NUMBER='%s'"
            % (plate))
        carwashdb.commit()
        print("---------------------RECORD UPDATED---------------------")
    elif service == "Vacuum":
        executor.execute(
            "UPDATE custinfo SET WASH_TYPE='VACUUM',WASH_PRICE=5 WHERE CARTYPE='MPV' AND PLATE_NUMBER='%s'"
            % (plate))
        carwashdb.commit()
        print("---------------------RECORD UPDATED---------------------")
    elif service == "WashVacuum":
        executor.execute(
            "UPDATE custinfo SET WASH_TYPE='WASH AND VACUUM',WASH_PRICE=17 WHERE CARTYPE='MPV' AND PLATE_NUMBER='%s'"
            % (plate))
        carwashdb.commit()
        print("---------------------RECORD UPDATED---------------------")
#If statement for SUV
if cartype == 3:
    if service == "Wash":
        executor.execute(
            "UPDATE custinfo SET WASH_TYPE='WASH',WASH_PRICE=13 WHERE CARTYPE='SUV' AND PLATE_NUMBER='%s'"
            % (plate))
        carwashdb.commit()
        print("---------------------RECORD UPDATED---------------------")
    elif service == "Vacuum":
        executor.execute(
            "UPDATE custinfo SET WASH_TYPE='WASH',WASH_PRICE=5 WHERE CARTYPE='SUV' AND PLATE_NUMBER='%s'"
            % (plate))
        carwashdb.commit()
        print("---------------------RECORD UPDATED---------------------")
    elif service == "WashVacuum":
        executor.execute(
            "UPDATE custinfo SET WASH_TYPE='WASH',WASH_PRICE=18 WHERE CARTYPE='SUV' AND PLATE_NUMBER='%s'"
            % (plate), )
        carwashdb.commit()
        print("---------------------RECORD UPDATED---------------------")
