c=0
for i in range(5):
    a=list(map(int,input().split()))
    if 1 in a:
        for j in range(5):
            if a[j]==1:
                c=abs(2-i)+abs(2-j)
print(c)
