import mysql.connector

cms = mysql.connector.connect(host="localhost",
                              user="root",
                              password="",
                              database="CinemaManagementSystem")
executor = cms.cursor()

staffid = str(input("Enter your staff ID: "))
address = str(input("Enter your new address: "))

executor.execute("UPDATE tblStaff SET StaffAddress='%s' WHERE StaffID='%s'" %
                 (address, staffid))
cms.commit()
print("---------------------RECORD UPDATED---------------------")