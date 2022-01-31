from turtle import *
import time

hideturtle()
color('black','red')

begin_fill()

left(45)
forward(100)
circle(50,180)

right(90)
circle(50,180)
forward(100)


end_fill()

time.sleep(0.7)

reset()
hideturtle()
#speed(0)
tracer(0,0)
setheading(0)

color('red','black')

begin_fill()

left(45)
forward(100)
circle(50,180)
left(70)
forward(30)
right(70)
forward(40)
left(70)
forward(40)
right(50)
forward(35)
left(60)
forward(25)
end_fill()


#left part
up()
right(110)
forward(10)
down()

color('black','red')

begin_fill()


right(60)
forward(100)
circle(-50,180)
right(20)
forward(25)
right(70)
forward(40)
left(70)
forward(40)
right(50)
forward(35)
left(60)
forward(25)


end_fill()

update()

