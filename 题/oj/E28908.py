pascal=input().split(';')
a=0
b=0
c=0
for i in pascal:
    if i!='':
        if i[0]=='a':
            a=int(i[-1])
        elif i[0]=='b':
            b=int(i[-1])
        elif i[0]=='c':
            c=int(i[-1])
print(a,b,c)