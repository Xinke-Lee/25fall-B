n,m,k=map(int,input().split())
matrix=[]
visited=[[False]*m for _ in range(n)]
can_move=False
for _ in range(n):
    matrix.append(list(map(int,input().split())))

def dfs(i,j,count):
    if count==k and i==n-1 and j==m-1 and matrix[i][j]!=1 and not visited[i][j]:
        global can_move
        can_move=True
        return
    if 0<=i<n and 0<=j<m and matrix[i][j]!=1 and not visited[i][j]:
        visited[i][j]=True
        dfs(i,j+1,count+1)
        dfs(i+1,j,count+1)
        dfs(i,j-1,count+1)
        dfs(i-1,j,count+1)
        visited[i][j]=False
    return

dfs(0,0,0)
if can_move:
    print("Yes")
else:
    print("No")