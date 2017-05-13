from turtle import*
shape("turtle")
speed(-1)

for i in range (5):
    if i==1:
        color("red","red")
    elif i==2:
        color("blue","blue")
    elif i==3:
        color("pink","pink")
    elif i==4:
        color("yellow","yellow")
    else:
        color("grey","grey")
    begin_fill()
    forward(50)
    left(90)
    forward(100)
    left(90)
    forward(50)
    left(90)
    forward(100)
    left(90)
    forward(50)
    end_fill()
        
    
