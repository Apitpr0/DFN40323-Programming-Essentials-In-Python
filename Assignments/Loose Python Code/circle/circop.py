import math
def pie(radius):
    diameter=radius*2
    diam="{:.2f}".format(diameter)
    print("Diameter circle:",diam)

    Circumference=math.pi*diameter
    circ="{:.2f}".format(Circumference)
    print("Circumference of circle",circ)

    Area_of_circle=math.pi*radius*radius
    area="{:.2f}".format(Area_of_circle)
    print("Area of circle is:",area)