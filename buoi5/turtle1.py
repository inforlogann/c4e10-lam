from turtle import*
pensize(3)
bgcolor("yellow")
speed(1)
def draw_square(length,colors):
    color(colors)
    for _ in range(4):
        fd(length)
        lt(90)
draw_square(50,"green")
        
    
    
