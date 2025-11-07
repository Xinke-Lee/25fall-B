n=int(input())
c={}
b=[]
dicta={'A':2,'B':2,'C':2,'D':3,'E':3,'F':3,'G':4,'H':4,'I':4,'J':5,'K':5,'L':5,'M':6,'N':6,'O':6,'P':7,'R':7,'S':7,'T':8,'U':8,'V':8,'W':9,'X':9,'Y':9}
for i in range(n):
    s=input()
    s=s.replace('-','')
    for j in s:
        if j in dicta:
            s=s.replace(j,str(dicta[j]))
    s=s[:3]+'-'+s[3:]
    c[s]=c.get(s,0)+1
for i in c:
    if c[i]>=2:
        b.append((i,c[i]))
if len(b)==0:
    print('No duplicates.')
else:  
    for i in sorted(set(b)):
        print(i[0],i[1])


