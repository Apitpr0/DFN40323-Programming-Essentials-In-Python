#For loop and Range function
#Example 1:

for a in range(10):
    print(a, end=" ")

#------------------------
#Example 2

a = 5
for b in range(1, 5):
    print("%d * %d = %d" % (a, b, a * b))

#------------------------
#Example 3

a = [10, 20, 30, 40, 50]
for b in a:
    print(b + 5, end=" ")
