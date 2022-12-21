from ticket.malaysian import *
from ticket.wp import *
from ticket.oth import *
print("Welcome to Ticket Admission into Zoo Negara Malaysia")
print("==================================================")
print("Please Select your citizenship:")
print("1 for Malaysian")
print("2 for Foreigner that have i-KAD/Working Permit/Dependant Pass")
print("3 for Foreigner (Others)")
name=input("Enter Name: ")
try:
	age=int(input("Enter Your Age: "))
	if type==1:
		if age < 36:
			human=print(infant)
			price=0
		elif (age <=3) and (age<=12):
			human=print("Children")
			price=18
		elif (age <=13) and (age<=59):
			human=print("Adult")
			price=45
		elif age > 60:
			human=print("Senior Citizen")
			price=23
	if type==2:
		if age < 36:
			human=print("Infant")
			price=0
		elif (age <=3) and (age<=12):
			human=print("Children")
			price=25
		elif (age <=13) and (age<=59):
			human=print("Adult")
			price=50
		elif age > 60:
			human=print("Senior Citizen")
			price=50
	if type==3:
		if age < 36:
			human=print("Infant")
			price=0
		elif (age <=3) and (age <=12):
			human=print("Children")
			price=43
		elif (age <=13) and (age <=59):
			human=print("Adult")
			price=88
		elif age <= 60:
			human=print("Senior Citizen")
			price=88
	quantity=int(input("Enter the quantity of the ticket that you want: "))
except:
	print("You entered string, please enter only numeric character")
else:
	print("Ticket Category: ")
	totalprice=price*quantity
	print("Total Price: ")

