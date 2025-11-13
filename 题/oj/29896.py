X,N=map(int,input().split())
val=sorted(map(int,input().split()))
if val[0]!=1:
    print(-1)
else:
    num = 0
    max_val = 0
    while max_val<X:
        add=0
        for x in reversed(val):
            if x<=max_val+1:
                add=x
                break
        max_val+=add
        num+=1
print(num)

