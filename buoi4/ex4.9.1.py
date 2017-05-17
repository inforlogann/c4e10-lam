from turtle import *
bgcolor("lightgreen")
pensize(3)
color("hotpink")
def draw_square(a):
    for i in range(4):
        fd(a)
        lt(90)
    penup()
    fd(a+20)
    pendown()
num = int(input("Number of Square?\t"))
for i in range(num):
    draw_square(20)
input()
