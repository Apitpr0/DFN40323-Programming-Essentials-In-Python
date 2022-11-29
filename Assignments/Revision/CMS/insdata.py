import mysql.connector

cms = mysql.connector.connect(host="localhost",
                              user="root",
                              password="",
                              database="CinemaManagementSystem")
executor = cms.cursor()

comm = "INSERT INTO tblStaff(StaffID,StaffName,StaffPhone,StaffAddress) VALUES (%s,%s,%s,%s)"

val = [("A001", "Zafri bin Ahmad", "0124557846", "4112,Lahar Yooi"),
       ("A002", "Ahmad Hanif bin Zulfikar", "0115687785",
        "PT231, Jalan Mengelembu"),
       ("A003", "Nur Fatin bin Azman", "0195462254", "Blk 14, Lahar Kepar")]

executor.executemany(comm, val)
cms.commit()
print(executor.rowcount, "Record Inserted")