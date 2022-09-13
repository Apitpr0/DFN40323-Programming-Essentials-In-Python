#First function use
def greet(name):
    '''This function greets the person passed in as a parameter'''
    print("Hello, "+name+". Good morning!")

greet("DDT4")

#Second function use (Pass args)
def my_function(fname,lname):
    '''This fuction expects 2 args and gets 2 args'''
    print(fname+""+lname)

my_function("Bob", "Ramen")

#Second type of passing args (same as wildcard)
def wildcard_function(*kids):
    '''Second type of passing args (same as wildcard)'''
    print("The youngest child is "+kids[2])
wildcard_function("Sarah","Amy","Cristy")

#Third type of passing args (but we declare each one by one)
def deconebyone(child3,child2,child1):
    '''Third type of passing args (but we declare each one by one)'''
    print("The youngest child is "+child3)
deconebyone(child1="Sarah",child2="Amy",child3="Cristy")

#Fourth type of passing args (Passing list as an args)
def passlist(food):
    '''Fourth type of passing args (Passing list as an args)'''
    for x in food:
        print(x)
fruits=["apple","banana","cherry"]
passlist(fruits)

#Return statement in function = exits a function/optionally passing back an expression to the caller
#Function definition is here
def sum(arg1,arg2):
    '''Add both the parameter and return them'''
    total=arg1+arg2
    print("Inside the function:",total)
    return(total)

#Now You can call sum function
total=sum(10, 20)
print("Outside the function:",total)