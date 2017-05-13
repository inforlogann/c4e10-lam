clothes = ["jeans","T-Shirt","Polo"]
print("Add: 'a', delete:'d', edit:'e',update:'u'" )
while True:
    print("Items in shop: ")
    item_no=1
    for clothe in clothes:
        print("{0}.{1}".format(item_no+1,clothe))
        item_no+=1
    action =input("what's up?")
    action = action.upper()
    if action == "A":
        item = input("item to add?")
        clothes.append(item)
    elif action == "D":
        itemd= input("item wants delete?")
        clothes.remove(itemd)
    elif action == "E":
        iteme = int(input("vi tri muon sua?"))
        clothes.pop(iteme)
        newitem= input("edit : ")
        clothes.insert(iteme,newitem)
    elif action == "U":
         items = int(input("number: "))
         location= int(input("location: "))
         clothes.insert(location,clothes.pop(items))
         
