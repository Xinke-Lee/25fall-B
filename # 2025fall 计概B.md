# 2025fall 计概B
## 1.数组
### 1.寻找数组的中心索引(一维前缀和)
https://leetcode.cn/problems/find-pivot-index/description/

```python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        T=sum(nums)
        A=0
        for i in range(len(nums)):
            if A==T-A-nums[i]:
                return i
                break
            else:
                A+=nums[i]
            if i==len(nums)-1 and A!=T-A-nums[i]:
                return -1
```
**前缀和**：
前缀和也是基础算法之一，它一般应用于快速求出某个连续区间的和/积。前缀和一般包括一维前缀和，二维前缀和，其实它的做题流程有一点点像动态规划的感觉。前缀和算法的时间复杂度是O(1)。下面是一个二维前缀和的例子：

### 2.垃圾炸弹(二维前缀和)
matrices, http://cs101.openjudge.cn/pctbook/M04133/

```python
d=int(input())
n=int(input())
trash=[[0]*1026 for i in range(1026)]
for _ in range(n):
    x,y,i=map(int,input().split())
    trash[y+1][x+1]=i
for y in range(1,1026):
    for x in range(1,1026):
        trash[y][x]+= trash[y-1][x]+trash[y][x-1]-trash[y-1][x-1]
A=-1
count=0
for y in range(1025):
    for x in range(1025):
        x1=max(0,x-d)
        x2=min(x+d,1024)
        y1=max(0,y-d)
        y2=min(y+d,1024)
        num=trash[y1][x1]+trash[y2+1][x2+1]-trash[y2+1][x1]-trash[y1][x2+1]
        if num>A:
            A=num
            count=1
        elif num==A:
            count+=1
print(count,A)
```
### 3.搜索插入位置(二分查找)
https://leetcode.cn/problems/search-insert-position/description/

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        high=len(nums)-1
        low=0
        guess=0
        while low<=high:
            mid=low+(high-low)//2
            guess=nums[mid]
            if guess>target:
                high=mid-1
            else:
                low=mid+1
            if guess==target:
                return mid
        return low
```
标准的二分查找，记住模板即可

### 4.区间合并(排序)
https://leetcode.cn/problems/merge-intervals/description/

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans=[]
        intervals.sort(key=lambda x:x[0])
        for i in range(len(intervals)-1):
            if intervals[i][1]<intervals[i+1][0]:
                pass
            else:
                intervals[i+1]=[intervals[i][0],max(intervals[i][1],intervals[i+1][1])]
                intervals[i]=0
        for i in range(len(intervals)):
            if intervals[i]!=0:
                ans.append(intervals[i])
        return ans
```

### 2.二维数组
https://leetcode.cn/problems/rotate-image/
```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # Step 1: 转置矩阵
        # 遍历上三角矩阵，将 matrix[i][j] 与 matrix[j][i] 互换
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Step 2: 翻转每一行
        # 遍历转置后的矩阵的每一行，并将其翻转
        for row in matrix:
            row.reverse()
```
这题与算法关系不大

### 3.