import mysql.connector 
lms=mysql.connector.connect(host="localhost",user="root",password="")

executor=lms.cursor()

executor.execute("create database LibraryManagementSystem")
