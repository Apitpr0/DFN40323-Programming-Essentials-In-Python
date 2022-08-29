#1. Converting Strings to Numerics
#using int() function
x="37"
y="20"
z=int(x) - int(y)
print(z)

#Using float() function
w="23.23"
v="23.00"
a=float(w) - float(v)
print(a)

#2. Converting Numerics to Strings
#using the str() function
print(str(23))      #Integer to String
print(str(23.3))    #Float to String

#Using the format() function
print("My age is {}".format(21))