
nicestrings = 0

for s in x:

    pairs = False
    for i in range(len(s)-2):
        subs = s[i]+s[i+1]
        check = s[i+2:]
        if(subs in check):
            pairs = True


    doubleChar = False
    for i in range(len(s)-2):
        if s[i] == s[i+2]:
            doubleChar = True
    if(doubleChar and pairs):
        nicestrings +=1
        print(s)



print(nicestrings)

yzsmlbnftftgwadz
tstwsswswrxlzrqs