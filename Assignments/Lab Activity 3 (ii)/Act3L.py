rows = int(input("Enter the number of rows:"))

#Print the space
k = 2 * rows - 2

#Outer loop-to print number of rows
for i in range(0, rows):
    #Inner loop-to print number of space
    for j in range(0, k):
        print(end=" ")
    #Decrement in k after each iteration
    k = k - 1
    #This inner loop-to print stars
    for j in range(0, i + 1):
        print("* ", end="")
    print("")

#Downward triangle Pyramid
#print the space
k = rows - 2
#Output for downward triangle pyramid
for i in range(rows, -1, -1):
    #inner loop-print the spaces
    for j in range(k, 0, -1):
        print(end=" ")
    #Increment in k after each ileration
    k = k + 1
    #Inner loop-print number of stars
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
