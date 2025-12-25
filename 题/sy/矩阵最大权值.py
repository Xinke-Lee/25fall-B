n,m=map(int,input().split())
matrix=[]
visited=[[False]*m for j in range(n)]
for _ in range(n):
    matrix.append(list(map(int,input().split())))

counts=[]
def dfs(i,j,count):
    if i==n-1 and j==m-1:
        count+=matrix[i][j]
        counts.append(count)
        return
    if 0<=i<n and 0<=j<m and not visited[i][j]:
        visited[i][j]=True
        dfs(i-1,j,count+matrix[i][j])
        dfs(i+1,j,count+matrix[i][j])
        dfs(i,j-1,count+matrix[i][j])
        dfs(i,j+1,count+matrix[i][j])
        visited[i][j]=False
dfs(0,0,0)
print(max(counts))