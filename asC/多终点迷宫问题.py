from collections import deque

n,m=map(int,input().split())
district=[]
for _ in range(n):
    district.append(list(map(int,input().split())))
q=deque()
q.append((0,0))
ans=[[-1]*m for _ in range(n)]
ans[0][0]=0
while q:
    coo=q.popleft()
    x,y=coo
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            if abs(dx)!=abs(dy) and 0<=x+dx<n and  0<=y+dy<m and district[x+dx][y+dy]==0 and ans[x+dx][y+dy]==-1:
                ans[x+dx][y+dy]=ans[x][y]+1
                q.append((x+dx,y+dy))
for i in ans:
    print(*i)