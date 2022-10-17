#Power of number
import mypackage.functions

print(mypackage.functions.power(3, 2))

#Check sum of 2 numbers
from mypackage import functions

print(functions.sum(10, 20))

#Greet
from mypackage.greet import SayHello

name = input("Masukkan nama:")
SayHello(name)