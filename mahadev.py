from turtle import *

color('black','grey')
begin_fill()
pensize(1.5)

hideturtle()
for i in range(3):
    forward(100)
    circle(5,180)

forward(5)
right(90)
circle(-100,60)
setheading(90)
forward(10)
print(heading())

print(heading())
setheading(0)
forward(130)
circle(5,180)
setheading(90)



left(90)
forward(320)
left(90)
forward(10)
left(90)
forward(15)



setheading(0)
right(90)
forward(15)
print(heading())
left(50)
circle(-100,52)
print(heading())


end_fill()
begin_fill()


setheading(0)
up()
goto(-9.0,117.0)
down()
forward(120)


setheading(0)
up()
goto(111.0,117.0)
down()

setheading(90)
forward(100)
circle(60,180)
forward(100)

end_fill()


color('yellow')
pensize(4)
right(90)
up()
goto(25.0,180.0)
down()
begin_fill()
forward(-50)
end_fill()

up()
goto(25.0,190.0)
down()
begin_fill()
forward(-50)
end_fill()

up()
goto(25.0,200.0)
down()
begin_fill()
forward(-50)
end_fill()


color('red')
pensize(5)
left(90)
up()
goto(50.0,170.0)
down()
begin_fill()
forward(-2)
pensize(8)
forward(-35)
pensize(5)
forward(-5)
end_fill()

up()
goto(-35.0,-53.0)
down()

color('brown')
write('हर हर महादेव',font=('Bernard MT Condensed',25,'bold'))

done()
