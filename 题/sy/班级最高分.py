n,m=map(int,input().split())
scores=list(map(int,input().split()))
parent=list(range(n+1))
def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(x, y):
    rootX=find(x)
    rootY=find(y)
    if rootX!=rootY:
        parent[rootX]=rootY

for _ in range(m):
    a,b=map(int,input().split())
    union(a,b)
scores_divided={}
max_scores=[]
for i in range(1,n+1):
    root=find(i)
    if root not in scores_divided:
        scores_divided[root]=[scores[i-1]]
    else:
        scores_divided[root].append(scores[i-1])
for i in scores_divided:
    max_scores.append(max(scores_divided[i]))
max_scores.sort(reverse=True)
print(len(max_scores))
print(*max_scores)