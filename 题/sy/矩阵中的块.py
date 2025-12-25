from collections import deque
n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
visited = [[False] * m for _ in range(n)]
block_count = 0
def bfs(start_row,start_col):
    q=deque([(start_row,start_col)])
    visited[start_row][start_col]=True
    while q:
        r,c = q.popleft()
        for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            new_r,new_c = r+dr,c+dc
            if 0<=new_r<n and 0<=new_c<m and matrix[new_r][new_c]==1 and not visited[new_r][new_c]:
                visited[new_r][new_c]=True
                q.append((new_r,new_c))
for i in range(n):
    for j in range(m):
        if matrix[i][j]==1 and not visited[i][j]:
            block_count+=1
            bfs(i,j)
print(block_count)