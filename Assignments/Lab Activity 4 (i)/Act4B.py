#Python function to multiply all the numbers in a list
num = [8, 2, 3, 6, 7]

def multiply(num):
    total = 1
    for x in num:
        total *= x
    return total

print(multiply(num))
