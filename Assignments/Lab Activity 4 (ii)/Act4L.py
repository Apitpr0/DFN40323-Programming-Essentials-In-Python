#create and display a dictionary
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(car)

#display all the items in the dictionary
x = car.items()
print(x)

#display all the values in the dictionary
x = car.values()
print(x)  #before the change

car["year"] = 2020
print(x)  #after the change

#display all the keys in the dictionary
x = car.keys()
print(x)  #before the change

car["color"] = "white"
print(x)  #after the change

#print key in dictionary using loop
for c in car:
    print(c)

#print value in dictionary using loop
for d in car:
    print(car[d])