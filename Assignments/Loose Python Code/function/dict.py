#Create and print dictionary
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(thisdict)

#Print specific key in dictionary
specificDict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(specificDict["brand"])

#Access dictionary items
car = {"brand": "Ford", "model": "Mustang", "year": 1964}

x = car.keys()
print(x)  #before the change

car["color"] = "white"
print(x)  #after the change



