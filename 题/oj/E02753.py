n=int(input())
li=[]
for i in range(n):
    a=int(input())
    f=1
    s=1
    for j in range(2,a):
        f,s=s,f+s
    li.append(s)
for i in range(len(li)):
    print(li[i])