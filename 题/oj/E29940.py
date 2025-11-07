n=int(input())
a=list(map(int,input().split()))
A=0
b=[]
for i in range(n):
    A+=a[i]
    b.append(A)
print(-min(b)+1)