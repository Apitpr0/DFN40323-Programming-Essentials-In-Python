def malaysianprice(type,age):
	
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
		return type,age

