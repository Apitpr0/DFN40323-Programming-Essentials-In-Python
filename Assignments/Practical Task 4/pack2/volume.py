#import math module for pi and pow
import math


#define function for calcVolume
def calcVolume(height, radius):
    #formula for volume
    vol = math.pi * math.pow(radius, 2) * height
    #Format to 2 decimal points
    twodecfloat = "{:.2f}".format(vol)
    #Print cylinder volume with 2 decimal points
    print("The volume of cylinder is", twodecfloat)
