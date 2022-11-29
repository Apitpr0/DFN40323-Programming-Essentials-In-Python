import mysql.connector

cms = mysql.connector.connect(host="localhost", user="root", password="")
executor = cms.cursor()
executor.execute("CREATE DATABASE CinemaManagementSystem")