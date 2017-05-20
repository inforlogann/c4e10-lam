from turtle import *
pensize(3)
bgcolor("lightgreen")
color("hotpink")
def draw_star(x,y,length):
    pu()
    fd(x)
    lt(69)
    fd(y)
    pd()
    for i in range(5):
        fd(length)
        rt(144)
draw_star(100,100,50)
