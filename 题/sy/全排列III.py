n=int(input())
nums=list(map(int,input().split()))
result=[]
check=[False]*n

def quanpailie(A):
    if len(A)==len(nums):
        if list(A[:]) not in result:
            result.append(list(A[:]))
        return
    for j in range(len(nums)):
        if not check[j]:
            check[j] = True
            A.append(nums[j])
            quanpailie(A)
            A.pop()
            check[j] = False
quanpailie([])
result.sort()
for i in result:
    print(*i)




