keep_asking=True

while keep_asking:
    try:
        x=int(input("Please Enter a number: "))
    except ValueError:
        print("The input was not a valid integer. Please try again...")
    else:
        print("Dividing 30 by",x,"will give you:",30/x)