a=1
while a<=3:
    b=int(input("Enter a number:"))
    if b==0:
        print("Exiting loop with break command, 'else' is not executed")
        break
    a+=1

else:
    print("Loop exited without executing break command")