n,m=map(int,input().split())
price=sorted(list(map(int,input().split())))
cost=0
for i in range(min(m,n)):
   if price[i]<0:
      cost-=price[i]
   else:
      break
print(cost)

    















