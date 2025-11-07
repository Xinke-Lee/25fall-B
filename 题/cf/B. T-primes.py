import math
n=int(input())
num=list(map(int,input().split()))
for i in range(n):
    sqrt=math.sqrt(num[i])
    if int(sqrt)==sqrt:
        print('YES')
    else:
        print('NO')