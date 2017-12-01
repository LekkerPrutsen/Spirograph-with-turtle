from turtle import *
import time

speed(0)
colormode(255)
r=108
g=45
b=12


time.sleep(2)


for i in range(18):
    
    pencolor((r,g,b))

    for j in range(36):

        
        forward(100)
        right(90)
        forward(30)
        right(100)
        forward(101.118742)
        
    penup()
    forward(45)
    right(20)
    pendown()
    r = r + 8
    g = g + 4


    
exitonclick()
