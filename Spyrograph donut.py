from turtle import *
import time


speed(0)

time.sleep(2)

for j in range(120):

    
    pencolor("coral")
    circle(100)
    right(180)
    pencolor("peachpuff")
    circle(100)
    right(180)

    penup()
    forward(3)
    pendown()

    left(3)
    
exitonclick()
