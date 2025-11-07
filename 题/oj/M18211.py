p=int(input())
money=list(map(int,input().split()))
money.sort()
left=0
a=0
b=0
right=len(money)-1
while left<=right:
    if p>=money[left]:
        a+=1
        p-=money[left]
        left += 1
    elif a>b and left<right:
        b+=1
        p+=money[right]
        right -= 1
    else:
        break
print(a-b)

