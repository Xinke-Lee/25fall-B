t=int(input())
for _ in range(t):
    l,r,x=map(int,input().split())
    a,b=map(int,input().split())
    if a==b:
        print(0)
    elif b<l or b>r:
        print(-1)
    elif r-a<x and a-l<x:
        print(-1)
    elif r-a>=x and a-l<x:
        if b>=a+x:
            print(1)
        elif b<=r-x:
            print(2)
        elif b>=l+x:
            print(3)
        else:
            print(-1)
    elif r-a<x and a-l>=x:
        if b<=a-x:
            print(1)
        elif b>=l+x:
            print(2)
        elif b<=r-x:
            print(3)
        else:
            print(-1)
    elif r-a>=x and a-l>=x:
        if b<=a-x or b>=a+x:
            print(1)
        else:
            print(2)
