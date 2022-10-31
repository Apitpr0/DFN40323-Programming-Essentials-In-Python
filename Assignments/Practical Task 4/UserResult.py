#import pack1 and call grade.py
from pack1 import grade
#Ask for name and grade from user
Name = input("Enter Your Name: ")
Grade = int(input("Enter Your grade: "))
#Call the function to print out name and grade
grade.result(Name, Grade)
