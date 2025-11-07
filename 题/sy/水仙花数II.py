a,b=map(int,input().split())
num=[]
for i in range(a,b+1):
    j=str(i)
    m,n,l=map(int,j)
    if m**3+n**3+l**3==i:
        num.append(i)
if len(num)==0:
    print('NO')
else:
    print(*num)