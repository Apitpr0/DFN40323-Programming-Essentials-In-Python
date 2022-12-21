import mysql.connector 
lms=mysql.connector.connect(host="localhost",user="root",password="",database="LibraryManagementSystem")

executor=lms.cursor()

comm="update tblStudent set StudentPassword='Generate22@anonyms' where StudID='DDV20F1001'"

executor.execute(comm)
lms.commit()
