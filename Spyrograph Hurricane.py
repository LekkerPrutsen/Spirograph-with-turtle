from turtle import *
import time

speed(0)
colormode(255)
clrs = ["Darkred", "Firebrick", "Crimson", "IndianRed"]

cn=0

time.sleep(2)

for j in range(120):
    
    c=40
    f=70
    h=3
    pencolor(clrs[cn])
    
    for i in range(14):

        
        circle(c)
        left(90)
        penup()
        forward(f)
        right(90)
        forward(h)
        pendown()
        c = c*0.8
        f = f*0.8
        h = h*1.2
        circle(c)
        

    penup()
    goto(0,0)
    forward(5)
    right(3)
    pendown()

    
    if cn < 3:
        cn = cn+1

    else:
        cn = 0
    
    
    
  
exitonclick()
