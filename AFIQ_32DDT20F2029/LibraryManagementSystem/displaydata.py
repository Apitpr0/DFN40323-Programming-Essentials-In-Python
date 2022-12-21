import mysql.connector 
lms=mysql.connector.connect(host="localhost",user="root",password="",database="LibraryManagementSystem")

executor=lms.cursor()

comm="select * from tblStudent"

executor.execute(comm)
output = executor.fetchall()

for f in output:
	print(f)