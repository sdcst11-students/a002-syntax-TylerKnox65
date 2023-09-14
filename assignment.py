import turtle
import time
global s, t
s = turtle.getscreen()
turtle.screensize(340, 360)
t= turtle.Turtle


def house():
    turtle.speed(1000)
    turtle.shapesize(0.1,0.1,0.1)
    turtle.up()
    turtle.goto(-200, -250)
    turtle.down()
    turtle.pen(pencolor="black", fillcolor="red")
    turtle.begin_fill()
    turtle.forward(200)
    for i in range(3):
        turtle.rt(270)
        turtle.fd(200)
    turtle.end_fill()
    turtle.rt(180)
    turtle.fd(200)
    turtle.pen(pencolor="black", fillcolor="black")
    turtle.begin_fill()
    turtle.rt(45)
    turtle.fd(145)
    turtle.rt(91)
    turtle.fd(143)
    turtle.end_fill()
    turtle.up()
    turtle.goto(-70, -230)
    turtle.down()
    turtle.pen(pencolor="black", fillcolor="yellow")
    turtle.begin_fill()
    turtle.lt(46)
    turtle.fd(50)
    turtle.lt(90)
    turtle.fd(100)
    turtle.lt(90)
    turtle.fd(50)
    turtle.lt(90)
    turtle.fd(100)
    turtle.end_fill()
    turtle.lt(90)
    turtle.up()
    turtle.fd(40)
    turtle.lt(90)
    turtle.fd(40)
    turtle.down()
    turtle.dot(5)

def grass():
    turtle.up()
    turtle.pen(fillcolor="green")
    turtle.setheading(0)
    turtle.goto(-390, -300)
    turtle.down()
    for i in range(2):
        for i in range(17):
            turtle.begin_fill()
            turtle.circle(50)
            turtle.up()
            turtle.fd(75)

            turtle.end_fill()
        turtle.up()
        turtle.goto(-390, -350)
        turtle.down()
def sky():
    turtle.bgcolor("skyblue")

def speech():
    turtle.up()
    turtle.goto(-90, 150)
    turtle.down()
    turtle.write("Ouch I lost my arm and leg")
def guy():
    turtle.setheading(0)
    turtle.up()
    turtle.goto(-100, 50)
    turtle.down()
    turtle.lt(45)
    turtle.fd(30)
    turtle.lt(45)
    turtle.fd(50)
    turtle.rt(90)
    turtle.circle(10)
    turtle.rt(180)
    turtle.fd(50)
    turtle.lt(45)
    i = 1
    while i > 0:
       turtle.fd(10)
       time.sleep(0.5)
       turtle.undo()
       turtle.rt(90)
       turtle.fd(10)
       time.sleep(0.5)
       turtle.undo()
       turtle.lt(90)
        

def main():
    house()
    grass()
    sky()
    speech()
    guy()







if __name__ == "__main__":
    main()
i = input()