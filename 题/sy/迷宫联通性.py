n,m=map(int,input().split())

parent = list(range(n + 1))
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
        parent[rootX] = rootY

for _ in range(m):
    a,b=map(int,input().split())
    union(a,b)

roots=[]
for i in range(1,n+1):
    if find(i) not in roots:
        roots.append(find(i))
if len(roots)==1:
    print('Yes')
else:
    print('No')