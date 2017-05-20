from turtle import*
pensize(3)
bgcolor("yellow")
speed(-1)
def draw_square(length,colors):
    color(colors)
    for i in range(4):
            fd(length)
            lt(90)
##draw_square(90,"red")    
for i in range(30):
    draw_square(i * 5, "red")
    left(17)
    penup()
    forward(i * 2)
    pendown()

