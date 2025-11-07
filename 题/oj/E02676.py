k=int(input())
num=input().split()
count1=0
count5=0
count10=0
for i in num:
    a=int(i)
    if a==1:
        count1+=1
    if a==5:
        count5+=1
    if a==10:
        count10+=1
print(count1)
print(count5)
print(count10)   