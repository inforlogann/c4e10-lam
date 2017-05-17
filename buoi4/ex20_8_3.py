f = open("source.txt","r")
text = f.read().lower().split()
def count(n):
    count = 0
    for i in n:
        i=i.strip().strip('"').strip(',').strip("'").strip(".")
        if i.lower() == "alice":
            count +=1
    return count
def find_alice():
    print("Word\t\tCount")
    print("==================")
    print("{0}\t\t{1}".format("alice",count(text)))
find_alice()
