#Import mysql connector and sys
import mysql.connector
import sys


#Define function named menu()
def menu():
    print("************************************")
    print("	   Welcome to Clean Car Wash System")
    print("************************************")
    print("	Menu Selection: ")
    print("	  1. Register Owner Car Record")
    print("	  2. View Car Record Slot")
    print("	  3. Update Booking Car Record")
    print("	  4. Delete Owner Car Record")
    print("	  5. Calculate Total Gross Income")

    print("To exit the system, press Q.")


#Call the function
menu()
#Ask user for input
opt = str(input("Enter Your Option:"))
#While loop for option
while opt != '0':
    if opt == '1':
        #Import module from modules folder
        from modules import regcust
    elif opt == '2':
        #Import module from modules folder
        from modules import listcust
    elif opt == '3':
        #Import module from modules folder
        from modules import updatedata
    elif opt == '4':
        #Import module from modules folder
        from modules import deletecust
    elif opt == '5':
        #Import module from modules folder
        from modules import grossincome
    elif opt == 'Q':
        print("Thank you for using Clean Car Wash")
        sys.exit()
    menu()
    opt = str(input("Enter Your Option:"))
