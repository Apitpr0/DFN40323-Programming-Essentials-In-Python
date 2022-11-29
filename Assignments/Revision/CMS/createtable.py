import mysql.connector

cms = mysql.connector.connect(host="localhost",
                              user="root",
                              password="",
                              database="CinemaManagementSystem")
executor = cms.cursor()

tablecreator = """create table tblStaff(
    StaffID varchar(10),
    StaffName varchar(50),
    StaffPhone varchar(12),
    StaffAddress varchar(100),
    primary key(StaffID)
    )"""
executor.execute(tablecreator)