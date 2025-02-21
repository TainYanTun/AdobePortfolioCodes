import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=800)

pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(0)

colors = ["red", "orange", "yellow", "green", "blue", "purple", "violet", "indigo"]

def draw_flower(size):
    for _ in range(36):
        pen.color(colors[_ % len(colors)])
        pen.forward(size)
        pen.left(45)
        pen.forward(size)
        pen.left(45)
        pen.left(10)

def draw_spiral():
    size = 10
    for i in range(100):
        pen.color(colors[i % len(colors)])
        pen.forward(size + i * 2)
        pen.left(91)

def draw_art():
    for i in range(72):
        draw_flower(100 + i * 2)
        pen.left(5)

def draw_circles():
    for i in range(36):
        pen.color(colors[i % len(colors)])
        pen.circle(100 + i * 10)
        pen.left(10)

pen.penup()
pen.setpos(0, -250)
pen.pendown()

draw_spiral()

pen.penup()
pen.setpos(-200, 0)
pen.pendown()
draw_art()

pen.penup()
pen.setpos(200, 0)
pen.pendown()
draw_circles()

pen.hideturtle()

turtle.done()
