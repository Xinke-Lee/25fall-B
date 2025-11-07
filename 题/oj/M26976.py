n = int(input())
nums = list(map(int, input().split()))
delta=nums[1]-nums[0]
if delta==0:
    length = 1
else:
    length = 2
for i in range(2,n):
    delta1=nums[i]-nums[i-1]
    if delta1 == 0:
        continue
    if (delta> 0 and delta1<= 0) or (delta< 0 and delta1>= 0):
        length+=1
        delta=delta1
if n < 2:
    print(n)
else:
    print(length)