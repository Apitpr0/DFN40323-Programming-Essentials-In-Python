def getLastStringCharacter(s):
    l = len(s)  #get string length
    return s[l - 1]  #Get last character of the string


i = input("Insert a string:")
print("Last character is", getLastStringCharacter(i))  #Call function
