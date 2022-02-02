import turtle as t



fill_color = "red"          #change filling color here if you want to for broken heart
border_color = "black"      #change border color here if you want to for broken heart
size = 2                    #you can chage heart size by here it will multiply to value !
starting_x = 00             #you can chage starting x cordinates of heart here
starting_y = 00             #you can chage starting y cordinates of heart here
pensize = 1                 #you can specify border or pen size here
speed = 3                   #change turtule speed here 1= fast 9 = slow


t.speed(speed)
t.pensize(pensize)
t.up()
t.goto(starting_x,starting_y)       #going to specified position efault is (00,00)
t.down()
t.hideturtle()


t.color(border_color,fill_color)    #setting up given color in broken heart right part  

t.begin_fill()                  #filling given color in broken heart right part

#right part of broken heart
t.left(45)
t.forward(100 * size)
t.circle(50* size,180)        # the curve of right side
t.left(70)          #from here all are zigzag lines
t.forward(30 * size)           
t.right(70)
t.forward(40 * size)
t.left(70)
t.forward(40 * size)
t.right(50)
t.forward(35 * size)
t.left(60)
t.forward(25 * size)           #zigzag lines finish
t.end_fill()            #filling complete in broken heart right part


#left part of broken heart
t.up()
t.right(110)
t.forward(10 * size)
t.down()

t.color(border_color,fill_color)      #setting up given color in broken heart left part 

t.begin_fill()          #filling given color in broken heart left part


t.right(60)
t.forward(100 * size)
t.circle(-50 * size,180)           # the curve of left side
t.right(20)                 #from here all are zigzag lines
t.forward(25 * size)
t.right(70)
t.forward(40 * size)
t.left(70)
t.forward(40 * size)
t.right(50)
t.forward(35 * size)
t.left(60)
t.forward(25 * size)           #zigzag lines finish

t.end_fill()        #filling complete in broken heart right part

t.update()      #makeing chages visible on screen

t.done          #drawing complte
