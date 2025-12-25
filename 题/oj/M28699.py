n,m=map(int,input().split())
price=list(map(int,input().split()))
fruits={}
for _ in range(m):
    fruit=input()
    if fruit not in fruits:
        fruits[fruit]=1
    else:
        fruits[fruit]+=1
sorted_fruits=sorted(fruits.items(),key=lambda x:x[1],reverse=True)
price.sort()
min_price=0
max_price=0
for i in range(len(sorted_fruits)):
    min_price+=sorted_fruits[i][1]*price[i]
price.reverse()
for i in range(len(sorted_fruits)):
    max_price+=sorted_fruits[i][1]*price[i]
print(min_price,max_price)
