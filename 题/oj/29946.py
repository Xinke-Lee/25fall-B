n=int(input())
k=int(input())
N=str(n)
l=len(N)
L=l
K=k
rest=L-K
ans=''
ind=0
while True:
    a=10
    for i in range(0,l-rest+1):
        if int(N[i])<a:
            a=int(N[i])
            ind=i
    ans=ans+str(a)
    N=N[ind+1:]
    rest-=1
    l=len(N)
    k-=1
    if len(ans)==L-K:
        break
print(int(ans))