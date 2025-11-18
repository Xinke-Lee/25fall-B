n,k=map(int,input().split())
numbers=list(map(int,input().split()))
ans=[]
check=[False]*n

def zuhe(index,A):
    if len(A)==k:
        if sorted(list(A[:])) not in ans:
            ans.append(sorted(list(A[:])))
        return
    else:
        for i in range(index,len(numbers)):
            if 0<=i<len(numbers) and not check[i]:
                check[i]=True
                A.append(numbers[i])
                zuhe(i+1,A)
                check[i]=False
                A.pop()

zuhe(0,[])
ans.sort()

for i in ans:
    print(*i)
