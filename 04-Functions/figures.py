###
# Draw a square
#
import pen
import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

pen = turtle.Turtle()
pen.speed(3)   


def draw_square(length):
    for i in range(4):
        turtle.forward(length)
        turtle.right(90)
        pen.penup()
        pen.goto(-100, 100)
        pen.pendown()

def draw_traingle(length):
    for i in range(3):
        turtle.forward(length)
        turtle.right(60)
        pen.penup()
        pen.goto(-100, 100)
        pen.pendown()

def draw_rectangle(length_a, length_b):
    for i in range(2):
        turtle.forward(length_a)
        turtle.right(90)
        turtle.forward(length_b)
        turtle.right(90)
        pen.penup()
        pen.goto(-100, 100)
        pen.pendown()


draw_square(15)
draw_square(10)
draw_traingle(10)
draw_traingle(15)
draw_rectangle(10, 15)
draw_rectangle(15, 20)

pen.hideturtle()
window.mainloop()