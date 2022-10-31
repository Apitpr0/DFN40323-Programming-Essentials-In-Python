#Declare function named result and pass 2 args (name,marks)
def result(name, marks):
    #if else statement for marks
    if marks >= 90 and marks <= 100:
        print("Your Grade is A+")
    elif marks >= 80 and marks <= 89:
        print("Your Grade is A")
    elif marks >= 75 and marks <= 79:
        print("Your Grade is A-")
    elif marks >= 70 and marks <= 74:
        print("Your Grade is B+")
    elif marks >= 65 and marks <= 69:
        print("Your Grade is B")
    elif marks >= 60 and marks <= 64:
        print("Your Grade is B-")
    elif marks >= 55 and marks <= 59:
        print("Your Grade is C+")
    elif marks >= 50 and marks <= 54:
        print("Your Grade is C")
    elif marks >= 47 and marks <= 49:
        print("Your Grade is C-")
    elif marks >= 44 and marks <= 46:
        print("Your Grade is D+")
    elif marks >= 40 and marks <= 43:
        print("Your Grade is D")
    elif marks >= 30 and marks <= 39:
        print("Your Grade is E")
    elif marks >= 20 and marks <= 29:
        print("Your Grade is E-")
    elif marks >= 0 and marks <= 19:
        print("Your Grade is F")
    else:
        print("Invalid Input!")
    print("\n")
    print("***************************")
    print("Your Name is", name)
    print("Your Mark is", marks)
