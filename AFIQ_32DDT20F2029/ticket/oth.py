def other(type,age):
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
		return type,age
	