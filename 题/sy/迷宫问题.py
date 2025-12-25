from collections import deque
n,m = map(int,input().split())
matrix=[]
for _ in range(n):
    matrix.append(list(map(int,input().split())))

def bfs(i,j):
    q = deque([(0,(i, j))])
    in_queue = {(i,j)}
    while q:
        step, (r,c) = q.popleft()  # 取出队首元素
        if (r,c)==(n-1,m-1):
            return step
        for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
            new_r=r+dr
            new_c=c+dc
            if 0<=new_r<n and 0<=new_c<m and (new_r,new_c) not in in_queue and matrix[new_r][new_c]!=1:
                in_queue.add((new_r,new_c))
                q.append((step+1,(new_r,new_c)))
    return -1
print(bfs(0,0))
