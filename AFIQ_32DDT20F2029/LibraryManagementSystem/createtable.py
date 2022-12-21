import mysql.connector 
lms=mysql.connector.connect(host="localhost",user="root",password="",database="LibraryManagementSystem")

executor=lms.cursor()

tblStudent="""create table tblStudent(
	StudID varchar(10) not null,
	StudentName varchar(100),
	Intake varchar (20),
	StudentPassword varchar(20),
	primary key (StudID)
	)"""
executor.execute(tblStudent)
