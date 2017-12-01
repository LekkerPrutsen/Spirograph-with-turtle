from turtle import *
import time

speed(0)
colormode(255)
bgcolor("white")

clrs=["Black", "Dimgray", "Gray", "Darkgray", "Silver", "Lightgrey", "Gainsboro"]

time.sleep(2)

h = 20
a=10

cn=0

for j in range(380):

    pencolor(clrs[cn])
    
    for i in range(3):
        forward(h)
        left(120)

    penup()
    forward(5)
    right(a)
    pendown()
    
    h = h*1.008
    a = a*0.995

    if cn < 6:
        cn=cn+1
    else:
        cn = 0
        
    
exitonclick()
