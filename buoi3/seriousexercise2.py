from operator import add
sheep = [5,7,300,90,24,50,75]
print("hello,my name is lam and these are my ship size: ",sheep)
print("after shearing",sheep)
for i in range(3):
        print("month: " ,i)
        print("now here is my fock: ",sheep)
        sheep.sort()
        a = sheep[6]
        print("biggest sheep in your list: ", a)
        sheep[6]= 8
        print("after shearing",sheep)
        b= [50,50,50,50,50,50,50]
        sheep= [sum(x) for x in zip(sheep, b)]
print("month 3:" )       
print("now here is my fock", sheep)
b=sum(sheep)
print("my flock has size in total: ",b)
print("i would get: ",b*2,"$")

