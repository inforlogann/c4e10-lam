from turtle import *
speed(-1)
pensize(3)
bgcolor("lightgreen")
color("blue")
def draw_pretty_pattern(n):
    for i in range(n):
        for x in range(4):
            fd(100)
            lt(90)
        lt(360/n)
draw_pretty_pattern(20)
input()
