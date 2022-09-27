#create a function to calculate total of 'a' in a string
#if there are no 'a', a 'none' message will appear


#1st answer using count function
def findA(s):
    total = 0
    x = s.count('a')
    y = s.count('A')
    total = x + y
    if total == 0:
        print("none")
    return total


#2nd answer using loop
def findA2(s):
    n = 0
    for i in s:
        if ((i == 'a') or (i == 'A')):
            n += 1
    return n


inputdata = input("Please input a phrase: ")
print("Total of 'a' or 'A' character in your phrase is: ", findA(inputdata))
print("Total of 'a' or 'A' character in your phrase is: ", findA2(inputdata))
