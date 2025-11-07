n=int(input().strip())
birthdays={}
for i in range(n):
    a,b,c=input().split()
    B=int(b)
    C=int(c)
    key=(B,C)
    if key not in birthdays:
        birthdays[key]=[]
    birthdays[key].append(a)
sortedkeys=sorted(birthdays.keys())
for keysA in sortedkeys:
    if len(birthdays[keysA])>1:
        print(keysA[0],keysA[1],*birthdays[keysA])
