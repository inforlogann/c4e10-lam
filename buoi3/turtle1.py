from turtle import*
shape("turtle")
speed(-1)
for i in range(6,2,-1):
    if  i==6 :
        color("yellow")
    elif i==5:
        color("blue")
    elif i==4 :
        color("red")
    else:
        color("green")
    
   
    for _ in range(i):
          forward(100)
          left(360/float(i))
   
