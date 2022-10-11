def completeSet():
    name = input("Enter Your Name:")
    celcius = float(input("Enter Your Temperature:"))
    if celcius > 39.0:
        status = "High Fever"
        print("Status = High Fever")
    elif celcius > 37.5:
        status = "Fever"
        print("Status = Fever")
    elif celcius > 36.3:
        status = "Normal"
        print("Status = Normal")
    else:
        status = "Hypothermia"
        print("Status = Hypothermia")
    return name, celcius


completeSet()