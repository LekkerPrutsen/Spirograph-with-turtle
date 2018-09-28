#!/usr/bin/env python3
"""
Spirograph Blue Shades drawing with Turtle Graphics
"""

__author__ = "LekkerPrutsen, nstickney"
__version__ = "0.2.0"
__license__ = "MIT"

import sys
import turtle


def blueShades():
    t = turtle.Turtle()

    t.speed(0)
    t.hideturtle()
    clrs = ["MidnightBlue", "Navy", "DarkBlue", "MediumBlue", "RoyalBlue",
            "MediumSlateBlue", "CornflowerBlue", "DodgerBlue", "DeepskyBlue",
            "LightSkyBlue", "SkyBlue", "LightBlue"]

    for j in range(120):
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


def main(animate):
    """ Main entry point of the app """
    if not animate:
        turtle.tracer(0)
    blueShades()
    turtle.update()
    turtle.exitonclick()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    if len(sys.argv) > 1 and sys.argv[1] == '-a':
        main(True)
    main(False)
