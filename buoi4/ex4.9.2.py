from turtle import *
num = int(input("Number of Square?\t"))
bgcolor("lightgreen")
pensize(3)
color("hotpink")
a = 20
def draw_square(a,num):
    for number in range(num):
        for i in range(4):
            fd(a*(number+1))
            lt(90)
        pst=a/2*(number+1)
        pu()
        setposition(-pst,-pst)
        pd()
draw_square(a,num)
input()
