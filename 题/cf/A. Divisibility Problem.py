t=int(input())
num=[]
for i in range(t):
    a,b=map(int,input().split())
    k=b*(a//b+1)-a
    if k==b:
        k=0
    num.append(k)
for j in num:
    print(j)
