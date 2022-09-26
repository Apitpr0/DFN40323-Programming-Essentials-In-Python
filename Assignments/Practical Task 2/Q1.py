print("Please select the math operation you would like to complete: ")
print(' "1" for addition')
print(' "2" for subraction')
print(' "3" for multiplication')
print(' "4" for division')

operation = int(input("the math operation you choose is: "))

if (operation == 1):
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))
    total = a + b
    print(a, " + ", b, " = ", total)

elif (operation == 2):
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))
    total = a - b
    print(a, "-", b, "=", total)

elif (operation == 3):
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))
    total = a * b
    print(a, "*", b, "=", total)

elif (operation == 4):
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))
    total = a / b
    print(a, "/", b, "=", total)

else:
    print("Wrong Calculation")
