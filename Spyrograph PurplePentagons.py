from turtle import *
import time


speed(0)
colormode(255)
bgcolor("white") 
pencolor("black")


h = 15

time.sleep(2)

for j in range(18):
    
    for i in range(5):
        forward(h)
        right(75)

    forward(10)
    right(5)
    
penup()   
goto(-33,40)
pendown()

h = 100
pencolor("plum")

for j in range(18):
    
    for i in range(5):
        forward(h)
        right(75)

    forward(10)
    right(5)


penup()   
goto(-72,88)
pendown()

h = 200
pencolor("indigo")

for j in range(18):
    
    for i in range(5):
        forward(h)
        right(75)

    forward(10)
    right(5)


penup()   
goto(-143,173)
pendown()

h = 380
pencolor("blueviolet")

for j in range(18):
    
    for i in range(5):
        forward(h)
        right(75)

    forward(10)
    right(5)



    
exitonclick()
