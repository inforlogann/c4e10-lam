#pusher
#map
#box
#destination

#set pusher coordinate:P
pusher_x=1
pusher_y=0

#set box coordinate:B
box={
    "x":3,
    "y":2
    }
box2={
    "x":1,
    "y":4
    }
boxes=[box,box2]
    

#set distination coordinate:D
dest={
        "x":1,
        "y":3
    }
dest2={
        "x":5,
        "y":3
    }
dests=[dest,dest2]


#set map_size
size_x = 6
size_y = 6

#re_structure
#day nhieu hop
        
def check_win(boxes,dests):
    win=0
    for a in boxes:
        for b in dests:
            if( a["x"]==b["x"] and a["y"]==b["y"]):
                win+=1
    return win
def check_lose(ax,ay,size_x,size_y):
    if([ax,ay]==[0,0] or [ax,ay]==[0,size_y-1] or [ax,ay]==[size_x-1,0] or [ax,ay]==[size_x-1,size_y-1]):
        return True
    return False
def in_map(x,y,size_x,size_y):
    return 0 <= x < size_x and 0 <= y < size_y
def check_overlap(x,y,items):
    for item in items:
        if x==item["x"] and y==item["y"]:
            return True
    return False
def print_map(size_x,size_y,pusher_x,pusher_y,boxes):
    for y in range(size_y):
        for x in range(size_x):
            if y==pusher_y and  x==pusher_x:
                print(" P " ,end="")
            elif check_overlap(x,y,boxes):
                print(" B ", end="")
            elif check_overlap(x,y,dests):
                print(" D ",end="")
            else:
                print(" - ",end="")
        print()

def input_process(direction ):
    dx=0
    dy=0
    if direction=="W":
        dy-=1
    elif direction=="A":
        dx-=1
    elif direction=="S":
        dy+=1
    elif direction=="D":
        dx+=1
    else:
        print("    Stupid   ")
    return dx,dy
#
while True:
    print_map(size_x,size_y,pusher_x,pusher_y,boxes)    
    direction=input("what is your next move? A/W/S/D").upper()
    dx,dy=input_process(direction)
    if box["x"]==pusher_x+dx and box["y"]==pusher_y+dy:
        if(in_map(box["x"] + dx,box["y"] + dy,size_x,size_y)):
            if((box["x"]+dx != box2["x"]) or (box["y"]+dy != box2["y"])):
                 box["x"]+=dx
                 box["y"]+=dy
                 pusher_x+=dx
                 pusher_y+=dy
            else:
                print(" you cant push   ")
        else:
            print("     You can't push  ")
    elif box2["x"]==pusher_x+dx and box2["y"]==pusher_y+dy:
        if(in_map(box2["x"]+dx,box2["y"]+dy,size_x,size_y)):
            if((box2["x"]+dx != box["x"]) or (box2["y"]+dy != box["y"])):
                box2["x"]+=dx
                box2["y"]+=dy
                pusher_x+=dx
                pusher_y+=dy
            else:
                print("  you cant push  ")
        else:
            print("you cant push")
    else:
        next_pusher_x=pusher_x+dx
        next_pusher_y=pusher_y+dy
        if(in_map(pusher_x+dx,next_pusher_y,size_x,size_y)):
            pusher_x+=dx
            pusher_y+=dy
        else:
            print("you cant move")
    if(check_lose(box["x"],box["y"],size_x,size_y)):
        print("   LOSE   ")
        break
    elif(check_lose(box2["x"],box2["y"],size_x,size_y)):
        print("   LOSE   ")
        break

        
    
    win=check_win(boxes,dests)
    if win==len(dests):       
        print(print_map(size_x,size_y,pusher_x,pusher_y,boxes))
        print("   winner  <3 ")
        break
    
