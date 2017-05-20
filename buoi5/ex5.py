def remove_dollar_sign(s):
    for char in s:
        if char in " $":
           s=s.replace(char,'')  
    return s
while True:
    sentence=input(("Import Sequence?\t"))
    print(remove_dollar_sign(sentence))
