#pusher
#box
#destination
#map

#set pusher ccoordinate
#rep: P

pusher={
    "x":1,
    "y":0
    }



#set box coordinate
#rep: B
boxes = [
    {
        "x": 3,
        "y": 2
    },
    {
        "x": 1,
        "y": 3
    }
]

#set destination coordinate
#rep: D
dests =[{
    "x":2,
     "y": 3
    },
       {"x":3,
        "y":3
        }
       ]
       

#set map_size
size ={
    "x":6,
    "y":7
    }

##level saved
#dung de luu lai trai thai ban dau cua game:"))
saved_pusher = pusher.copy()
saved_boxes = [box.copy() for box in boxes]

# re-structure
# day nhieu hop
def reset_level(saved_pusher,saved_boxes):
    global pusher,boxes
    pusher = saved_pusher.copy()
    boxes = [box.copy() for box in saved_boxes]
    
def is_in_map(x, y, size):
    return 0 <= x < size["x"] and 0 <= y < size["y"]

def check_overlap(x, y, items):
    for item in items:
        if x == item["x"] and y == item["y"]:
            return item
    return None
def move(item,dx,dy):
    item["x"] += dx
    item["y"] +=dy
    return item
def print_map(size, pusher, boxes):    
    for y in range(size["y"]):
        for x in range(size["x"]):
            if x == pusher["x"] and y == pusher["y"]:
                print(" P ", end ="")
            elif check_overlap(x, y, boxes):
                print(" B ", end ="")
            elif check_overlap(x,y,dests):
                print(" D ", end ="")
            else:
                print(" - ", end ="")
        print()

def check_win(boxes,dests):
    win=0
    for box in boxes:
        for dest in dests:
            if (box["x"]==dest["x"] and box["y"]==dest["y"]):
                win+=1
    return win

def input_process(direction):
    dx = 0
    dy = 0
    if direction == "W":
        dy -= 1
        #dy = dy - 1
    elif direction == "A":
        dx -= 1
    elif direction == "S":
        dy += 1
    elif direction == "D":
        dx += 1
    else:
        print("You enter wrong button pls do this again bro :)")

    return dx, dy
undo =1
undo_pusher =[]
undo_boxes=[]
# main GAME_LOOP
while undo != 0:
    print_map(size, pusher, boxes)
    command = input("What is your next move? W/A/S/D? \nEnter R to reset the Game \nEnter U to undo a step\n").upper()
    if command == "R":
        reset_level(saved_pusher,saved_boxes)
        
    elif command =="U":
        undo -=1
       
        reset_level(undo_pusher[len(undo_pusher)-1],undo_boxes[len(undo_boxes)-1])
        undo_pusher.pop()
        undo_boxes.pop()
    else:
        undo +=1
        undo_pusher.append(pusher.copy())
        undo_boxes.append([box.copy() for box in boxes])
        
    
    
                
        
        
        
    # xu ly dau vao` 
    dx, dy = input_process(command)
    found_box= check_overlap(pusher["x"]+dx,pusher["y"]+dy,boxes)
    if found_box is not None:

        if check_overlap(found_box["x"]+dx,found_box["y"]+dy,boxes) is None:

            if is_in_map(found_box["x"]+dx,found_box["y"]+dy,size):
                found_box= move(found_box,dx,dy)
                pusher=move(pusher,dx,dy)

    elif is_in_map(pusher["x"]+dx,pusher["y"]+dy,size):
        pusher=move(pusher,dx,dy)





    win=check_win(boxes,dests)
    if win==len(dests):
        print(print_map(size,pusher,boxes))
        print("   winner  <3 .\n Do you wanna be my lover?")
        break
    
   

    














