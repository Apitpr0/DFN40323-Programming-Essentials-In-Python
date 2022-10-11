#Program to calculate temperature
name = input("Enter Your Name:")
temp = float(input("Enter Your Temperature:"))

celsius = temp
print(temp)

if temp > 39.7:
	status="High Fever"
	print("status = High Fever")
elif temp > 37.7:
	status="Fever"
	print("status = Fever")
elif temp > 36.0:
	status="Normal"
	print("status = Normal")
else:
	status="Hypothermia"
	print("status = Hypothermia")