def sum_to(n):
    a=0
    for i in range(n):
        a += (i+1)
    return a
while True:
  number = int(input("number?\t"))
  print(sum_to(number))
