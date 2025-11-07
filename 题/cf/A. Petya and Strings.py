a=str(input())
b=str(input())
c=[a.lower(),b.lower()]
d=sorted(c)
if c[0]==c[1]:
    print(0)
elif c[0]==d[0]:
    print(-1)
else:
    print(1)