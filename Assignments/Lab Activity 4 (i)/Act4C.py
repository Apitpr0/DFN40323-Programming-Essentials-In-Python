#Program to calculate area of rectangle
#get input from user
width = input("Please input width:")
height = input("Please input height:")
width = int(width)
height = int(height)

#Function to calculate area
def calculateArea():
    area = width * height
    return area

#Display output
print("Width :", width)
print("Height :", height)
print("Area of rectangle:", calculateArea())
