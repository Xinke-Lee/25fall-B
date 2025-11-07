n=int(input())
a=0
for i in range(n+1):
    if i%7==0:
        a=a
    elif (i-7)%10==0:
        a=a
    elif i//10==7:
        a=a
    else:
        a=a+i**2
print(a)