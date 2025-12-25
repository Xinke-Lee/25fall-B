class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])
        parent = list(range(n * m + 1))
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
            return n*i+j
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='1':
                    for di,dj in [(0,1),(1,0),(-1,0),(0,-1)]:
                        if 0<=i+di<n and 0<=j+dj<m and grid[i+di][j+dj]=='1':
                            union(two_to_one(i+di,j+dj),two_to_one(i,j))
        num=0
        for i in range(n*m):
            if parent[i]==i:
                num+=1
        return num