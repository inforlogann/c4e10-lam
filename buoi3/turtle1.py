from turtle import*
shape("turtle")
speed(-1)
colors=["red","blue","grey","orange","cyan"]
color_index=0
for i in range(17,2,-1):
    color(colors[color_index%len(colors)])
    color_index+=1
    for _ in range(i):
        forward(20)
        left(360/float(i))
   
