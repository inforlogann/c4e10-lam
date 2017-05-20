import turtle
def draw_poly(t,n,sz):
    for i in range(n):
        t.fd(sz)
        t.lt(360/n)
def draw_equitriangle(t, sz):
    draw_poly(t,3,sz)
tess=turtle.Turtle()
tess=turtle.color("red")
tess.speed(1)
draw_equitriangle(tess,100)  
    
