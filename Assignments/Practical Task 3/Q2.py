#Write a program to accept a number from the user and store first 12 multiples of number in a tuple.
#Display the tuple.
number = int(input("Enter a number: "))
currentTuple = ()
for i in range(1, 13):
    currentTuple += (number * i, )
print(currentTuple)
print("\n")

#a. Determine how many items a tuple has.
print("Determine how many items a tuple has.")
print("There is", len(currentTuple), "items in the tuple")
print("\n")

#b. Print item in index 4.
print("Print item in index 4.")
print(currentTuple[4])
print("\n")

#c.	Change the item in index 5 to “Python”.
print("Change the item in index 5 to “Python”.")
myList = list(currentTuple)
myList[5] = "Python"
currentTuple = tuple(myList)
print(currentTuple)
print("\n")

