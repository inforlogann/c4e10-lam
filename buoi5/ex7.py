def extract_even(n):
    _list=[]
    for i in n:
        if i%2==0:
            _list.append(i)
    return _list
print(extract_even([1,4,5,-1,10]))
    
