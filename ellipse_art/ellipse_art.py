import turtle
from math import pi, radians, cos, sin
import numpy as np
import time

screen = turtle.Screen()
screenTk = screen.getcanvas().winfo_toplevel()
screenTk.attributes("-fullscreen", True)
# monitor_width = screen.window_width()
# monitor_height = screen.window_height()

bob = turtle.Turtle()
bob.hideturtle()
bob.speed(0)
turtle.delay(0)
turtle.bgcolor("black")
turtle.colormode(255)


def rotate_by_deg(x, y, rotation_deg):
    theta = radians(rotation_deg)
    return (x * cos(theta) - y * sin(theta), x * sin(theta) + y * cos(theta))


def draw_ellipse(obj, major_axis, minor_axis, rotation_deg=0, origin=(0, 0)):
    og = np.array(origin)  # centre of ellipse

    a, b = major_axis / 2, minor_axis / 2

    ticks = np.linspace(0, 2 * pi, num=3600)

    obj.penup()
    obj.goto(
        og + np.array(rotate_by_deg(a * cos(ticks[0]), b * sin(ticks[0]), rotation_deg))
    )

    obj.pendown()
    for t in ticks:
        x, y = og + np.array(rotate_by_deg(a * cos(t), b * sin(t), rotation_deg))
        obj.goto(x, y)
        bob.dot(1)

    obj.penup()


time.sleep(4)
bob.pencolor(57, 255, 20)
k = 23
for n in range(k):
    draw_ellipse(bob, 1800 * (k - n / 10) / k, 300 * (k - n) / k, 30 + n * 5)
h = 19
for n in range(h):
    draw_ellipse(bob, 2400 * (h - n / 10) / h, 200 * (h - n) / h, 15 - n * 7)
