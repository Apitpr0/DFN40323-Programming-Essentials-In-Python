#create and display a dictionary
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(car)

#access and display a value based on the key
x = car.get("model")  #using get() method
print(x)

x = car["model"]  #using key and store in a new variable
print(x)

print(car["brand"])  #using key and display

#trying to duplicate the dictionary key
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964, "year": 2020}
print(thisdict)

#add a new item in the dictionary
car["color"] = "red"
print(car)

#update the value
car.update({"year": 2020})  #using update() method
print(car)

car["year"] = 2021  #using the key index
print(car)