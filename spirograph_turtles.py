#!/usr/bin/env python3
"""
Spirograph Blue Shades drawing with Turtle Graphics
"""

__author__ = "LekkerPrutsen, nstickney"
__version__ = "0.2.0"
__license__ = "MIT"

import sys
import turtle


def blue_shades():
    t = turtle.Turtle()

    t.speed(0)
    t.hideturtle()
    clrs = ["MidnightBlue", "Navy", "DarkBlue", "MediumBlue", "RoyalBlue",
            "MediumSlateBlue", "CornflowerBlue", "DodgerBlue", "DeepskyBlue",
            "LightSkyBlue", "SkyBlue", "LightBlue"]

    for i in range(120):
        t.forward(5)
        t.right(3)
        c = 30
        f = 70
        for i in clrs:
            t.pencolor(i)
            t.circle(c)
            t.left(90)
            t.penup()
            t.forward(f)
            t.right(90)
            t.pendown()
            c *= 0.8
            f *= 0.8
            t.circle(c)
        t.penup()
        t.goto(0, 0)
        t.pendown()


def hurricane():
    t = turtle.Turtle()

    t.speed(0)
    clrs = ["Darkred", "Firebrick", "Crimson", "IndianRed"]

    for i in range(120):
        t.forward(5)
        t.right(3)
        c = 40
        f = 70
        h = 3
        t.pencolor(clrs[i % 4])
        for i in range(14):
            t.circle(c)
            t.left(90)
            t.penup()
            t.forward(f)
            t.right(90)
            t.forward(h)
            t.pendown()
            c *= 0.8
            f *= 0.8
            h *= 1.2
            t.circle(c)
        t.penup()
        t.goto(0, 0)
        t.pendown()


def purple_pentagons():
    t = turtle.Turtle()

    t.speed(0)
    h = 15
    for i in range(18):
        for j in range(5):
            t.forward(h)
            t.right(75)
        t.forward(10)
        t.right(5)
    t.penup()
    t.goto(-33, 40)
    t.pendown()
    h = 100
    t.pencolor("plum")
    for i in range(18):
        for j in range(5):
            t.forward(h)
            t.right(75)
        t.forward(10)
        t.right(5)
    t.penup()
    t.goto(-72, 88)
    t.pendown()
    h = 200
    t.pencolor("indigo")
    for i in range(18):
        for j in range(5):
            t.forward(h)
            t.right(75)
        t.forward(10)
        t.right(5)
    t.penup()
    t.goto(-143, 173)
    t.pendown()
    h = 380
    t.pencolor("blueviolet")
    for i in range(18):
        for j in range(5):
            t.forward(h)
            t.right(75)
        t.forward(10)
        t.right(5)


def silver_angles():
    t = turtle.Turtle()

    t.speed(0)
    clrs = ["Black", "Dimgray", "Gray", "Darkgray",
            "Silver", "Lightgrey", "Gainsboro"]
    h = 20
    a = 10
    for i in range(420):
        t.pencolor(clrs[i % len(clrs)])
        for j in range(3):
            t.forward(h)
            t.left(120)
        t.penup()
        t.forward(5)
        t.right(a)
        t.pendown()
        h *= 1.008
        a *= 0.995


def square_shell():
    t = turtle.Turtle()

    t.speed(0)
    t.pencolor("MediumAquamarine")
    h = 10
    for i in range(360):
        for j in range(4):
            t.forward(h)
            t.right(90)
        t.right(3)
        h *= 1.01


def print_usage():
    print("Usage: python" + sys.argv[0] + " [-a] " + "<drawing>")
    print("    [-a]: animate the drawing")
    print("    <drawing>: one of")
    print("        blue_shades")
    print("        hurricane")
    print("        purple_pentagons")
    print("        silver_angles")
    print("        square_shell")
    sys.exit()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    if (len(sys.argv) < 2 or
            (sys.argv[1] == '-a' and len(sys.argv) < 3) or
            (len(sys.argv) > 3)):
        print_usage()

    drawing = 2
    if sys.argv[1] != '-a':
        turtle.tracer(0)
        drawing -= 1

    if sys.argv[drawing] == 'blue_shades':
        blue_shades()
    elif sys.argv[drawing] == 'hurricane':
        hurricane()
    elif sys.argv[drawing] == 'purple_pentagons':
        purple_pentagons()
    elif sys.argv[drawing] == 'silver_angles':
        silver_angles()
    elif sys.argv[drawing] == 'square_shell':
        square_shell()
    else:
        sys.exit("ERROR: No such drawing (" + sys.argv[drawing] + ")")

    turtle.update()
    turtle.exitonclick()
