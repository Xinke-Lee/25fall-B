n=int(input())
money=sorted(list(map(int,input().split())))
N=sum(money)
M=0
cost=0
for i in range(n):
   cost+=money[i]
   if cost>=N/2:
      M=i-1
      break
print(len(money)-M-1)