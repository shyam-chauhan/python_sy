t.pensize(pensize)
t.up()
t.goto(starting_x,starting_y)       #going to specified position efault is (00,00)
t.down()
t.hideturtle()
t.color(border_color,fill_color)        #setting given color

t.begin_fill()          #filling given color

t.left(45)
t.forward(100 * size) 
t.circle(50*size,180)       #first curve

t.right(90)
t.circle(50*size,180)       #second curve

t.forward(100*size)


t.end_fill()            #filling complete

t.done          #drawing complte
