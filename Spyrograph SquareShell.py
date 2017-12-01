from turtle import *

speed(0)
colormode(255)
bgcolor("white") 
pencolor("MediumAquamarine")


h = 10

for j in range(360):
    
    for i in range(4):
        forward(h)
        right(90)

    right(3)
    h = h*1.01
   



    
exitonclick()
