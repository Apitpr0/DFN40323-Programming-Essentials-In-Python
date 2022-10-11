def completeSet(name, celcius):

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


name = input("Enter Your Name:")
temp = float(input("Enter Your Temperature:"))
completeSet(name, temp)
