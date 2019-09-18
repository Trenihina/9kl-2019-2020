import turtle  # turtle.reset()
from turtle import *  # reset()

#    from turtle import as t

#    print(dir(turtle))   # список всех имён, определённых в модуле


turtle.reset()   # отобразить холст
turtle.shape("turtle")
turtle.shapesize(3, 3)

turtle.pensize(5)
turtle.color("red")
turtle.penup()

turtle.speed(1)
turtle.forward(10)
turtle.left(90)
turtle.forward(10)

turtle.done()
