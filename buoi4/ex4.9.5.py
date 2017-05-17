from turtle import *
speed(-1)
pensize(2)
bgcolor("lightgreen")
color("blue")
rt(180)
def draw_maze(n):
    a=0
    for i in range(n):
        fd(5+a)
        rt(90)
        fd(5+a)
        rt(90)
        a+=5
draw_maze(51)
input()
