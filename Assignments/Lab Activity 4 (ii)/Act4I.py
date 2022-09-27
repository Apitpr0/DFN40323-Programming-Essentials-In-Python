#First example
y, z = 1, 2  #global variables in module


def all_global():
    global x  #declare globals assigned
    x = y + z  #no need to declare y,z
    print("x in function all_global:", x)

all_global()
print("x outside function:", x)

#------------------------------
#Second example

def f():
    global s  #declare globals assigned
    print(s)
    s = "Only in spring, but London is great as well!"
    print(s)

s = "I am looking for a course in Paris!"
f()
print(s)