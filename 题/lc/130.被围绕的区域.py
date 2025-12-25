class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n = len(board),len(board[0])
        total=m*n
        parent = list(range(total+1))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY
        def two_to_one(i,j):
            return i*n+j
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':
                    if i==0 or i==m-1 or j==0 or j==n-1:
                        union(two_to_one(i,j),total)
                    else:
                        for di,dj in [(0,1),(1,0),(-1,0),(0,-1)]:
                            if 0<=i+di<m and 0<=j+dj<n and board[i+di][j+dj]=='O':
                                union(two_to_one(i+di,j+dj),two_to_one(i,j))
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':
                    if find(two_to_one(i,j))!=find(total):
                        board[i][j]='X'