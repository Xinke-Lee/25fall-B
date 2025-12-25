from collections import deque

n,m=map(int,input().split())
district=[]
for _ in range(n):
    district.append(list(map(int,input().split())))
inq=set()
inq.add((0,0))
q=deque()
q.append((0,0))
coordinate=[[(-1,-1) for _ in range(m)] for _ in range(n)]
while q:
    x,y=q.popleft()
    if (x,y)==(n-1,m-1):
        break
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            if abs(dx)!=abs(dy) and 0<=x+dx<n and 0<=y+dy<m and (x+dx,y+dy) not in inq and district[x+dx][y+dy]==0:
                inq.add((x+dx,y+dy))
                q.append((x+dx,y+dy))
                coordinate[x+dx][y+dy]=(x,y)
path=[]
eee=(n-1,m-1)
while eee!=(-1,-1):
    path.append(eee)
    eee=coordinate[eee[0]][eee[1]]
path.reverse()
for x in path:
    print(x[0]+1,x[1]+1)