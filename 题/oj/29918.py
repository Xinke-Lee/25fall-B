import math
def add(a):
    A=1
    for i in range(2,int(math.sqrt(a))+1):
        if a % i == 0:
            if i == int(a/i):
                A += i
            else:
                A += i + int(a/i)
    return A
n=int(input())
B=[]
adds=[0]*(n+1)
for i in range(1,n+1):
    adds[i]=add(i)
for i in range(1,n+1):
    if adds[i]<=n and i<adds[i]:
        if adds[adds[i]]==i:
            B.append((i,adds[i]))
B.sort(key=lambda x:x[0],reverse=False)
for i in B:
    print(int(i[0]),int(i[1]))

