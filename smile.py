from turtle import *


colormode(255)
bgcolor("black")
shape("turtle")

color(29,172,214)
begin_fill()
up()
goto(0,-150)
down()
circle(150)
end_fill()


color("white")
up()
goto(-40,30)
down()
begin_fill()
circle(20)
end_fill()
color("black")
up()
goto(-32,40)
down()
begin_fill()
circle(9)
end_fill()


color("white")
up()
goto(48,38)
down()
begin_fill()
circle(20)
end_fill()
color("black")
up()
goto(44,44)
down()
begin_fill()
circle(9)
end_fill()



up()
goto(-70,-51)
down()
right(45)
for i in range(2):
    circle(100,50)

up()
goto(-129.0,-211.0)
down()
color(29,172,214)
write("keep smiling",font=("Calisto MT",40,"bold"))

hideturtle()


