#import volume.py from pack2
from pack2 import volume

#Ask input from user for height and radius
cylHeight = int(input("Please enter the height of your cylinder:"))
cylRadius = int(input("Please enter the radius of your cylinder:"))
#call calcVolume and pass cylHeight and cylRadius and output the answer
volume.calcVolume(cylHeight, cylRadius)
