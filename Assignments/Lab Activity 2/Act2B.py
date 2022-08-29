#Program to calculate area of rectangle
#Get input from use
width=input("Please input width:")
height=input("Please input height:")

#Calculate Area
width=float(width)
height=float(height)
area=width*height
area=round(area,2)      #to format to 2 decimal places

#Display Output
print("Width=",width)
print("Height=",height)
print("Area of rectangle:",area)
