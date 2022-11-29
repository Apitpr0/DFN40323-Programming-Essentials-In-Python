import mysql.connector

cms = mysql.connector.connect(host="localhost",
                              user="root",
                              password="",
                              database="CinemaManagementSystem")
executor = cms.cursor()

print("")
executor.execute("SELECT * FROM tblStaff")
result = executor.fetchall()

for x in result:
    print(x)