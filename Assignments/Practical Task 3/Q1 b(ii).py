#Program to calculate temperature
def tempMethod():
    if temp > 39.0:
        status = "High Fever"
        print("Status = High Fever")
    elif temp > 37.5:
        status = "Fever"
        print("Status = Fever")
    elif temp > 36.3:
        status = "Normal"
        print("Status = Normal")
    else:
        status = "Hypothermia"
        print("Status = Hypothermia")
    return temp


name = input("Enter Your Name:")
celcius = float(input("Enter Your Temperature:"))

temp = celcius
print(tempMethod())
