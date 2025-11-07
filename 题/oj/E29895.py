n=int(input())
p=0
for i in range(2,int(n**0.5)+1):
    if int(n/i)==n/i:
        p=i
        break
print(int(n/p))
