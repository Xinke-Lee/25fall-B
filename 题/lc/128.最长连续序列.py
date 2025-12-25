class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=sorted(list(set(nums)))
        n=len(nums)
        parent=list(range(n + 1))

        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]

        def union(x, y):
            rootX=find(x)
            rootY=find(y)
            if rootX!=rootY:
                parent[rootX]=rootY
        for i in range(n-1):
            if nums[i]==nums[i+1]-1:
                union(i+1,i+2)
        starts={}
        for i in range(1,n+1):
            a=find(i)
            if a not in starts:
                starts[a]=[i]
            else:
                starts[a].append(i)
        length=0
        for i in starts:
            if len(starts[i])>length:
                length=len(starts[i])
        return length