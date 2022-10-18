from packages.req import SayHello
import turtle

name = input("Masukkan nama:")
SayHello(name)
wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Star Creator")
star = turtle.Turtle()
star.right(75)
star.forward(100)

for i in range(4):
    star.right(144)
    star.forward(100)

turtle.done()