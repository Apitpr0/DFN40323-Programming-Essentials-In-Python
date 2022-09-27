#Program to find a factorial of a number using recursive function

def factorial(x):
    '''This is a recursive function
    to find the factorial of an integer'''

    if x == 1:
        return 1
    else:
        return (x * factorial(x - 1))  #It will recursively call itself

num = 3
print("The factorial of", num, "is", factorial(num))
