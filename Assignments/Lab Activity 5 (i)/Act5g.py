'''Create a simple program to calculate area and circumference of a circle by using the pi math library'''

import math

rad = int(input("Enter circle radius: "))
area = math.pi * rad * rad
circumference = math.pi * (rad * 2)

print("Area of circle=" + str(format(area, ".2f")))
print("Circumference of circle=" + (format(circumference, ".2f")))
