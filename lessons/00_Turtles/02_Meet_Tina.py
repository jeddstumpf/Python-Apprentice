"""
The is a simple Turtle program that draws a square and writes a message. The
lines that start with a # are comments. They are not executed by Python. The
lines inside the three quotes are also comments, but of a different sort (
called "doc comments" ) Comments are used to explain what the code does. Read
the program and try to understand what each line does.

RUM ME! YOu can run this program by clicking on ▶️ icon ar the top of the editor
window.

"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup(width=600, height=600)     # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast.

tina.forward(190)
tina.left(160)
tina.forward(190)
tina.left(25)
tina.left(25)
tina.forward(130)
tina.left(150)
tina.forward(110)






























turtle.exitonclick()