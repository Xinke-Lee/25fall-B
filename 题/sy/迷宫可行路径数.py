n,m=map(int,input().split())
matrix=[]
for i in range(n):
    matrix.append(list(map(int,input().split())))
visited=[[False]*m for _ in range(n)]

def dfs(i,j):
    count = 0
    if i==n-1 and j==m-1:
        return 1
    else:
        if 0<=i<n and 0<=j<m and not visited[i][j] and matrix[i][j]!=1:
            visited[i][j] = True
            count+=dfs(i-1,j)
            count+=dfs(i+1,j)
            count+=dfs(i,j-1)
            count+=dfs(i,j+1)
            visited[i][j] = False
    return count
if matrix[0][0]==1:
    print(0)
else:
    print(dfs(0,0))


