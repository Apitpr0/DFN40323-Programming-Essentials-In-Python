#Import mysql connector
import mysql.connector

#Declare login info for db
carwashdb = mysql.connector.connect(host="localhost", user="root", password="")
executor = carwashdb.cursor()
#Create database for carwash
executor.execute("CREATE DATABASE carwash")