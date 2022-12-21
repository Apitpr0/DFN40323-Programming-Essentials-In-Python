import mysql.connector 
lms=mysql.connector.connect(host="localhost",user="root",password="",database="LibraryManagementSystem")

executor=lms.cursor()

comm=("insert into tblStudent (StudID,StudentName,Intake,StudentPassword) values (%s,%s,%s,%s)")

val=[("DDT19F1001","FARISHA SHUHADA BINTI AZIM","Dis2019","Extreme@m331"),("DDV20F1001","IRFAN HAKIM BIN MOHD","June2020","Generate@2022")]

executor.executemany(comm,val)
lms.commit()
print(executor.rowcount(), "record inserted")
