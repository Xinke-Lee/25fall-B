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

k=int(input())
for _ in range(k):
    a,b=map(int,input().split())
    if find(a)!=find(b):
        print('No')
    else:
        print('Yes')
