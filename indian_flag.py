from turtle import *

up()
backward(200)
down()

color('orange')
begin_fill()
for i in range(0,2):
    forward(400)
    left(90)
    forward(100)
    left(90)

end_fill()

up()
right(90)
forward(200)
left(90)
down()

hideturtle()
color('green')
begin_fill()

for i in range(0,2):
    forward(400)
    left(90)
    forward(100)
    left(90)
end_fill()

up()
goto(0,-50)
down()

color("blue")
begin_fill()
circle(2,360)
end_fill()


pensize(3)
up()
goto(0,-100)
down()
circle(49,360)
end_fill()

up()
goto(0,-50)
down()

pensize(2)
for i in range(0,24):
    forward(49)
    left(360/24)
    up()
    goto(0,-50)
    down()

up()
goto(-50,-250)
down()
color('purple')
write('JAI HIND',font=('Bernard MT Condensed',25,'bold'))
    
