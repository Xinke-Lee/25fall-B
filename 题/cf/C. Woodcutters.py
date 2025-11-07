n=int(input())
trees=[]
choose=[-1]+[0]*(n-2)+[1]
nums=2
for _ in range(n):
    xi,hi=map(int,input().split())
    trees.append((xi,hi))
for i in range(1,n-1):
    delta_x1 = trees[i][0] - trees[i - 1][0]
    delta_x2 = trees[i + 1][0] - trees[i][0]
    if choose[i-1]<=0:
        if delta_x1>trees[i][1]:
            choose[i]=-1
            nums+=1
        elif delta_x2>trees[i][1]:
            choose[i]=1
            nums+=1
        else:
            choose[i]=0
    else:
        if delta_x1>trees[i-1][1]+trees[i][1]:
            choose[i]=-1
            nums+=1
        elif delta_x2>trees[i][1]:
            choose[i]=1
            nums+=1
        else:
            choose[i]=0
if n>1:
    print(nums)
else:
    print(1)

