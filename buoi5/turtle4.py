from turtle import*
pensize(1)
bgcolor("yellow")
speed(-1)
def draw_star(x,y,length):
       pu()
       goto(x,y)
       pd()
       for i in range(5):
            fd(length)
            lt(144)
speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300) 
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)
