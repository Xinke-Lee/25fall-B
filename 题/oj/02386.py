import sys
sys.setrecursionlimit(20000)
N,M=map(int,input().split())
matrix=[]
for _ in range(N):
    matrix.append(list(input()))

num=0

def dfs(i,j):
    if 0<=i<N and 0<=j<M:
        if matrix[i][j]=='W':
            matrix[i][j]='.'
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
            dfs(i+1,j+1)
            dfs(i+1,j-1)
            dfs(i-1,j+1)
            dfs(i-1,j-1)

for i in range(N):
    for j in range(M):
        if matrix[i][j]=='W':
            dfs(i,j)
            num+=1

print(num)