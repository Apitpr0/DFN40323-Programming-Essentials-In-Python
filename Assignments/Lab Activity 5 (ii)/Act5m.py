keep_asking=True

while keep_asking:
    try:
        x=int(input("Please enter a number:"))
        print("Dividing 50 by",x,"will give you :",50/x)
    except(ZeroDivisionError,ValueError,TypeError):
        print("Something has gone wrong..")
        #Code to deal with the exception
    except:
        print("Other than ZeroDivisionError,ValueError,TypeError")