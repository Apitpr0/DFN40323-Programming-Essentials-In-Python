#Import mysql connector
import mysql.connector

#Connect to database
carwashdb = mysql.connector.connect(host="localhost", user="root", password="")
#declare cursor as the worker for our database
executor = carwashdb.cursor()
#Create database named sm_app
executor.execute("CREATE DATABASE sm_app")
