#import turtle  # turtle.reset()
#from turtle import *  # reset()

#    from turtle import as t

#    print(dir(turtle))   # список всех имён, определённых в модуле


import turtle


def house(x: int, y: int) -> object:
    """ рисует домик """

    turtle.forward(x)
    turtle.left(90)
    turtle.fd(y)
    turtle.left(45)
    turtle.forward(x//2*(2**0.5))
    turtle.left(90)
    turtle.forward(x//2*(2**0.5))
    turtle.left(45+90)
    turtle.fd(x)
    turtle.penup()
    turtle.left(180)
    turtle.fd(x)
    turtle.left(90)
    turtle.pendown()
    turtle.fd(y)
    turtle.left(90)


t = turtle.Turtle()
t.shape('turtle')
turtle.goto(0,0)
house(100,100)

turtle.penup()
turtle.goto(150,0)
turtle.pendown()


house(50,50)



turtle.done()
