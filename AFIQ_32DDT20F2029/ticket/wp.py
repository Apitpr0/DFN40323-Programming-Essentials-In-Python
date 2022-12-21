def wp_price(type,age):
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
		return type,age
	

