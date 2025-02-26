"""
The is a simple Turtle program that draws a square and writes a message. The
lines that start with a # are comments. They are not executed by Python. The
lines inside the three quotes are also comments, but of a different sort (
called "doc comments" ) Comments are used to explain what the code does. Read
the program and try to understand what each line does.

RUM ME! YOu can run this program by clicking on ▶️ icon ar the top of the editor
window.

"""
import random
import turtle




                          # Tell Python we want to work with the turtle
turtle.setup(width=600, height=600)     # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina




for i in range (4):
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    tina.shape('circle')                    # Set the shape of the turtle to a turtle
    tina.speed(3)                           # Make the turtle move as fast, but not too fast.
    tina.color("teal")
    tina.forward(190)
    tina.left(160)
    tina.forward(190)
    tina.left(25)
    tina.left(25)
    tina.forward(130)
    tina.left(150)
    tina.forward(100)
    tina.left(180)
    tina.forward(100)
    tina.color("blue")
    tina.left(90)
    tina.forward(170)
    tina.left(90)
    tina.forward(290)
    tina.left(90)
    tina.forward(175)
    tina.left(75)
    tina.forward(100)
    tina.right(80)
    tina.color("brown")
    tina.forward(130)
    tina.right(85)
    tina.forward(85)
    tina.right(90)
    tina.forward(155)
    tina.penup()
    tina.goto(x,y)
    tina.pendown()







turtle.exitonclick()