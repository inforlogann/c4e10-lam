clothes = ["jeans","T-Shirt","Polo"]
print("Add: 'a', delete:'d', edit:'e',update:'u'" )
while True:
    print("Items in shop: ")
    item_no=1
    for clothe in clothes:
        print("{0}.{1}".format(item_no,clothe))
        item_no+=1
    action =input("what's up?")
    action = action.upper()
    if action == "A":
        item = input("item to add?")
        clothes.append(item)
    elif action == "D":
        itemd= int(input("item wants delete?"))
        clothes.remove(itemd)
    elif action == "E":
        edit_index = int(input("position?"))-1
        new_item= input("edit : ")
        clothes[edit_index]=new_item
             
