n,m = map(int, input().split())
level=list(map(int, input().split()))
level.sort()
diverse=[]
for i in range(n-1):
    diverse.append(level[i+1]-level[i])
diverse.sort(reverse=True)
for i in range(m-1):
    diverse[i]=0
print(sum(diverse))