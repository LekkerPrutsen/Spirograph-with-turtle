from turtle import *

import time

speed(0)
colormode(255)
bgcolor("white")
clrs = ["saddlebrown", "saddlebrown", "gold", "gold", "darkorange", "forestgreen", "forestgreen"]


l = 280
a = 5
cn = 6


time.sleep(3)

for k in range(7):

    pencolor(clrs[cn])

    for j in range(72):

        left(90)
        forward(l)
        circle(15)
        right(180)
        forward(l)
        left(90)
        forward(2)
        right(a)

    l = l/1.5

    cn = cn-1



    
exitonclick()
