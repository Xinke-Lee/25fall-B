roman=input()
try:                   
    Roman=int(roman)
    Roman_str=[]
    a=[{'1':'M','2':'MM','3':'MMM'},{'1':'C','2':'CC','3':'CCC','4':'CD','5':'D','6':'DC','7':'DCC','8':'DCCC','9':'CM'},{'1':'X','2':'XX','3':'XXX','4':'XL','5':'L','6':'LX','7':'LXX','8':'LXXX','9':'XC'},{'1':'I','2':'II','3':'III','4':'IV','5':'V','6':'VI','7':'VII','8':'VIII','9':'IX'}]
    for i in range(-1,-len(roman),-1):
        if roman[i]!='0':
            Roman_str.append(a[i][roman[i]])
    if roman[0]!='0':
        Roman_str.append(a[-len(roman)][roman[0]])
    Roman_str.reverse()
    print(''.join(Roman_str))
except:
    d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    s=0
    for i in range(len(roman)-1):
        if d[roman[i]]<d[roman[i+1]]:
            s-=d[roman[i]]
        else:
            s+=d[roman[i]]
    print(s+d[roman[-1]])
