from turtle import *
speed(-1)
pensize(2)
bgcolor("lightgreen")
color("blue")
def draw_maze(n):
    a=0
    b=n
    for i in range(n):
        fd(5+a)
        rt(90)
        fd(5+a)
        rt(90)
        a+=5
        lt(360/(b+100))
draw_maze(52)
input()
