d=int(input())
n=int(input())
trash=[[0]*1026 for i in range(1026)]
for _ in range(n):
    x,y,i=map(int,input().split())
    trash[y+1][x+1]=i
for y in range(1,1026):
    for x in range(1,1026):
        trash[y][x]+= trash[y-1][x]+trash[y][x-1]-trash[y-1][x-1]
A=-1
count=0
for y in range(1025):
    for x in range(1025):
        x1=max(0,x-d)
        x2=min(x+d,1024)
        y1=max(0,y-d)
        y2=min(y+d,1024)
        num=trash[y1][x1]+trash[y2+1][x2+1]-trash[y2+1][x1]-trash[y1][x2+1]
        if num>A:
            A=num
            count=1
        elif num==A:
            count+=1
print(count,A)


