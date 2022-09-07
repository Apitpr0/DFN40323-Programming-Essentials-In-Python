#Ask user for name age weight and height
name = str(input("Enter your name:"))
age = float(input("Enter your age:"))
weight = float(input("Enter your weight in KG:"))
height = float(input("Enter your height in Meter:"))


#BMI formula
BMI = weight / (height*height)

print("Hi",name,".""Your age is",int(age),"years old""."" Your BMI is",float(BMI),"and the category is")

#Start of if statement
if (BMI < 18.5):
    print("Underweight")
elif (BMI >= 18.5) & (BMI <= 24.9):
    print("Normal")
elif (BMI >= 25) & (BMI <= 30):
    print("Overweight")
elif (BMI > 30):
    print("Obese")
else:
    print("Please Try Again")


