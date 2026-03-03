# 2025fall 计概B
以下是cheeting sheet，如要使用可以把pdf转化成短边两页后使用。
## 语法
### 位运算的语法
1. 按位与 (AND) &
规则：上下两位对着看，都是 1 结果才是 1，否则就是 0。（也就是“找相同且为真”）

常用场景：提取特定位（比如我们之前用的 n & 1 提取最低位），或者掩码操作。
```python
a = 5  # 0101
b = 3  # 0011
print(a & b)  # 结果是 1 (二进制 0001)
```
2. 按位或 (OR) |
规则：上下两位对着看，只要有一个是 1 结果就是 1，两个都是 0 结果才是 0。

常用场景：合并位（比如我们之前用的 res | bit 把提取出来的 1 贴上去）。
```python
a = 5  # 0101
b = 3  # 0011
print(a | b)  # 结果是 7 (二进制 0111)
```
3. 按位异或 (XOR) ^
规则：上下两位对着看，不一样就是 1，一样就是 0。（也就是“找不同”）

常用场景：它有一个神奇的特性：任何数和自己异或都是 0 (x ^ x = 0)，任何数和 0 异或都是自己 (x ^ 0 = x)。常用于加密、数据校验，或者“寻找数组中只出现一次的数字”。
```python
a = 5  # 0101
b = 3  # 0011
print(a ^ b)  # 结果是 6 (二进制 0110)
```
4. 按位取反 (NOT) ~
规则：单目运算符（只对一个数操作），0 变 1，1 变 0。

注意：在 Python 中，因为整数是没有长度限制的（底层用补码表示），~x 的数学计算结果固定等于 -(x + 1)。
```python
a = 5
print(~a)  # 结果是 -6
```
5. 左移 (Left Shift) <<
规则：把数字的二进制整体向左移动指定的位数，右边空出来的位置补 0。

数学意义：左移 1 位相当于乘以 2，左移 n 位相当于乘以 2 的 n 次方。
```python
a = 5  # 0101
print(a << 1)  # 结果是 10 (二进制 1010)
print(a << 2)  # 结果是 20 (二进制 10100)
```
6. 右移 (Right Shift) >>
规则：把数字的二进制整体向右移动指定的位数，最右边多出来的位直接丢弃。

数学意义：右移 1 位相当于整除 2（向下取整）。
```python
a = 5  # 0101
print(a >> 1)  # 结果是 2 (二进制 0010，最右边的 1 被丢弃了)
```

### sys数据输入
如果数据中数字或字符串被空格、换行、Tab 杂乱地分割，直接这样写：
```python
import sys
input = sys.stdin.read
data = input().split()  # 读入所有数据并分割为列表
```
配合后面的迭代器
```python
import sys
# 获取所有输入的迭代器
input_data = iter(sys.stdin.read().split())
# 每次调用 next() 就会拿出一个字符串
try:
    n = int(next(input_data))  # 读取数量 N
    m = int(next(input_data))  # 读取数量 M    
    # 批量读取
    # 比如读一个 n * m 的矩阵
    matrix = []
    for _ in range(n):
        row = [int(next(input_data)) for _ in range(m)]
        matrix.append(row)        
except StopIteration:
    pass # 处理输入结束的情况
```
如果需要处理的数据“行”本身有意义（例如每行代表一个独立的操作），但每行内部又有不规则空格：
```python
import sys
# 一次性读入所有行，且自动去掉末尾的换行符
lines = sys.stdin.read().splitlines()
for line in lines:
    if not line.strip(): # 跳过空行
        continue
    # 处理每一行的数据
    parts = line.split() 
    print(f"处理行内容: {parts}")
```

### 列表反转
```python
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)  # 输出: [5, 4, 3, 2, 1]
```
```python
my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]
print(reversed_list)  # 输出: [5, 4, 3, 2, 1]
```
```python
my_list = [1, 2, 3, 4, 5]
reversed_list = list(reversed(my_list))
print(reversed_list)  # 输出: [5, 4, 3, 2, 1]
```
### 转二进制
```python
decimal_number = 10
binary_number = bin(decimal_number)
print(binary_number)  # 输出: 0b1010
```
去前缀
```python
binary_number_without_prefix = bin(decimal_number).lstrip("0b")
print(binary_number_without_prefix)  # 输出: 1010
```
```python
binary_number = "1010"
decimal_number = int(binary_number, 2)
print(decimal_number)  # 输出: 10
```

### 迭代器
Python内置函数iter()可将可迭代对象（如列表）转换为迭代器。
```python
my_list = [1, 2, 3]
my_iterator = iter(my_list)
print(next(my_iterator))  # 输出: 1
print(next(my_iterator))  # 输出: 2
```

### bisect库
bisect是内置二分查找库
```python
import bisect

# 准备一个有序列表
nums = [1, 3, 3, 5]

# 1. bisect_left: 查找左侧插入点
# 如果元素存在，返回第一个相同元素的位置
idx_l = bisect.bisect_left(nums, 3)   # 结果: 1 (nums[1]是第一个3)

# 2. bisect_right (同 bisect): 查找右侧插入点
# 如果元素存在，返回最后一个相同元素之后的位置
idx_r = bisect.bisect_right(nums, 3)  # 结果: 3 (nums[3]是5，插入在所有3之后)

# 3. insort: 查找并直接执行插入操作
# 相当于 nums.insert(bisect_right(...), 4)，保持列表有序
bisect.insort(nums, 4)                # nums 变为 [1, 3, 3, 4, 5]
```
### 函数的局部变量和全局变量
对于函数内的不可变的数据结构：int（整数）、float（浮点数）、bool（布尔值）、str（字符串）、tuple（元组）、None，需要使用global声明后才能修改；对于可变对象list（列表）、dict（字典）、set（集合）以及自定义的类对象，你可以直接调用它们的方法或修改其内部元素。Python 会沿着作用域往外找，找到这个对象并直接在原地修改它。

### enumerate函数
enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中
```python
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))
#[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
list(enumerate(seasons, start=1))       # 下标从 1 开始
#[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
```

### 排序函数总结
```python
import operator
from functools import cmp_to_key

# 1. 基础用法：sort() vs sorted()
nums = [3, 1, 4, 1, 5, 9]

# list.sort() : 原地修改列表，返回 None
nums.sort() 
print(f"原地排序: {nums}") # [1, 1, 3, 4, 5, 9]

# sorted() : 不改变原对象，返回一个新列表。适用于所有可迭代对象
original = [3, 1, 4]
new_list = sorted(original)
print(f"新列表: {new_list}, 原列表不变: {original}")

# 2. 核心参数：reverse (升序/降序)
data = [10, 20, 30]
print(f"降序: {sorted(data, reverse=True)}") # [30, 20, 10]

# 3. 核心参数：key (自定义排序逻辑)
# 场景 A: 按字符串长度排序
words = ["banana", "apple", "cherry", "kiwi"]
print(f"按长度排序: {sorted(words, key=len)}")

# 场景 B: 忽略大小写排序
mixed_case = ["a", "B", "c", "D"]
print(f"忽略大小写: {sorted(mixed_case, key=str.lower)}")

# 场景 C: 使用 Lambda 处理复杂结构 (如元组/列表)
students = [("Alice", 22), ("Bob", 18), ("Charlie", 20)]
# 按年龄 (索引为1的元素) 排序
sorted_students = sorted(students, key=lambda x: x[1])
print(f"按年龄排序: {sorted_students}")

# 4. operator 模块 (大型数据排序推荐，性能更优)
data_dicts = [{"name": "A", "val": 10}, {"name": "B", "val": 5}]
# 相当于 lambda x: x["val"]
data_dicts.sort(key=operator.itemgetter("val"))
print(f"itemgetter排序: {data_dicts}")

# 5. 多级排序 (Multiple Levels)
# 先按成绩降序，成绩相同时按名字升序
# 技巧：数字取反可实现升降序混合排列
results = [("Alice", 90), ("Bob", 95), ("Charlie", 90)]
results.sort(key=lambda x: (-x[1], x[0]))
print(f"多级排序: {results}") # [('Bob', 95), ('Alice', 90), ('Charlie', 90)]

# 6. 对非列表对象进行排序
# 字典排序 (默认对 key 排序，返回 key 列表)
d = {'b': 2, 'a': 1, 'c': 3}
print(f"字典Key排序: {sorted(d)}") # ['a', 'b', 'c']
# 按字典的值排序，返回键值对元组列表
print(f"字典按Value排序: {sorted(d.items(), key=lambda x: x[1])}")

# 7. 复杂自定义比较 (cmp_to_key)
# Python 3 移除了 cmp 参数。若需比较两个元素 x, y 的逻辑：
def custom_compare(x, y):
    # 示例逻辑：将数字拼接，看哪种组合更大 (常用于算法题)
    if str(x) + str(y) > str(y) + str(x):
        return -1 # x 应该排在前面
    else:
        return 1

nums_str = [3, 30, 34, 5, 9]
high_order = sorted(nums_str, key=cmp_to_key(custom_compare))
print(f"自定义比较排序: {high_order}")
```

### 抄来的
```python
"""语法糖和常用函数"""
print(bin(9)) #bin函数返回二进制，形式为0b1001
dict.items()#同时调用key和value
print(round(3.123456789,5))# 3.12346
print("{:.2f}".format(3.146)) # 3.15
a,b=b,a
dict.get(key,default=None) # 其中，my_dict是要操作的字典，key是要查找的键，default是可选参数，表示当指定的键不存在时要返回的默认值
ord() # 字符转ASCII
chr() # ASCII转字符
for index,value in enumerate([a,b,c]): # 每个循环体里把索引和值分别赋给index和value。如第一次循环中index=0,value="a" 
```

### 日期与时间
```python
import calendar, datetime

print(calendar.isleap(2020))  # 输出: True

print(datetime.datetime(2023, 10, 5).weekday())  # 输出: 3 (星期四)
```
### math
```python
import math

# 1. 数论与数值操作 (最常用)
# 向上取整
print(math.ceil(3.1))   # 4

# 向下取整
print(math.floor(3.9))  # 3

# 阶乘
print(math.factorial(5)) # 120 (即 5*4*3*2*1)

# 最大公约数 (GCD)
print(math.gcd(12, 18))  # 6

# 最小公倍数 (LCM) - Python 3.9+
print(math.lcm(12, 18))  # 36

# 组合数 C(n, k) - Python 3.8+
print(math.comb(5, 2))   # 10

# 排列数 P(n, k) - Python 3.8+
print(math.perm(5, 2))   # 20

# 截断整数部分 (向0取整)
print(math.trunc(-3.9)) # -3

# 2. 幂、对数与开方
# 平方根 (返回浮点数)
print(math.sqrt(16))    # 4.0

# 整数平方根 (返回整数，常用于判断素数时的遍历上限)
# 等价于 int(math.sqrt(n))，但效率更高且避开了浮点误差
print(math.isqrt(17))   # 4

# 幂运算 (返回浮点数，通常直接用 ** 或 pow() 更快)
print(math.pow(2, 3))   # 8.0

# 自然对数 (ln x)
print(math.log(math.e)) # 1.0

# 以 2 或 10 为底的对数 (比 math.log(x, 2) 更精确)
print(math.log2(8))     # 3.0
print(math.log10(100))  # 2.0

# 3. 几何与三角函数
# 弧度转角度
print(math.degrees(math.pi)) # 180.0

# 角度转弧度
print(math.radians(180))     # 3.14159...

# 三角函数 (注意输入是弧度)
print(math.sin(math.radians(30))) # 0.4999... (约等于0.5)
print(math.cos(0))                # 1.0

# 计算两点间的欧几里得距离 (Python 3.8+)
# 相当于 sqrt((x2-x1)**2 + (y2-y1)**2)
p1 = [0, 0]
p2 = [3, 4]
print(math.dist(p1, p2)) # 5.0

# 计算斜边长度 (sqrt(x*x + y*y))
print(math.hypot(3, 4))  # 5.0

# 4. 常量
print(math.pi)  # 3.141592653589793
print(math.e)   # 2.718281828459045
print(math.inf) # 正无穷大 (float('inf'))
print(-math.inf)# 负无穷大
print(math.nan) # 非数字 (Not a Number)

# 5. 判断函数
# 判断两个浮点数是否足够接近 (解决浮点数精度问题)
print(math.isclose(0.1 + 0.2, 0.3)) # True

# 判断是否为无穷大
print(math.isinf(math.inf)) # True

# 判断是否为 NaN
print(math.isnan(math.nan)) # True

# 判断是否是完全平方数 (Python 3.11+)
# print(math.isqrt(n)**2 == n) # 在老版本中这样写
```

## 数组
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

### 二维数组
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
这题与算法关系不大，主要是语法

### 素数筛
写法1（欧拉筛）：

```python
def Euler_sieve(n):
    primes = [True for _ in range(n+1)]
    p = 2
    while p*p <= n:
        if primes[p]:
            for i in range(p*p, n+1, p):
                primes[i] = False
        p += 1
    primes[0]=primes[1]=False
    return primes
print(Euler_sieve(20))
# [False, False, True, True, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, True, False]
```

写法2（埃氏筛）：

```python
# 胡睿诚 23数院 
# 埃氏筛 基本够用
N=20
primes = []
is_prime = [True]*N
is_prime[0] = False;is_prime[1] = False
for i in range(1,N):
    if is_prime[i]:
        primes.append(i)
        for k in range(2*i,N,i): #用素数去筛掉它的倍数
            is_prime[k] = False
print(primes)
# [2, 3, 5, 7, 11, 13, 17, 19]
```

写法3（欧拉筛）：

```python
# 胡睿诚 23数院 
N=20
primes = []
is_prime = [True]*N
is_prime[0] = False;is_prime[1] = False
for i in range(2,N):
    if is_prime[i]:
        primes.append(i)
    for p in primes: #筛掉每个数的素数倍
        if p*i >= N:
            break
        is_prime[p*i] = False
        if i % p == 0: #这样能保证每个数都被它的最小素因数筛掉！
            break
print(primes)
# [2, 3, 5, 7, 11, 13, 17, 19]
```

## 排序

### 冒泡排序
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # 标记是否发生了交换
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # 交换元素
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # 如果没有发生交换，说明数组已经排序完成
        if not swapped:
            break
    return arr

if __name__ == "__main__":
    arr_in = [6, 5, 18, 2, 16, 15, 19, 13, 10, 12, 7, 9, 4, 4, 8, 1, 11, 14, 3, 20, 17, 10]
    print(arr_in)
    arr_out = BubbleSort(arr_in)
    print(arr_out)
```
重复遍历并比较相邻元素，并交换他们的位置。

### 选择排序
```python
def SelectSort(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
               minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

if __name__ == "__main__":
    arr_in = [6, 5, 18, 2, 16, 15, 19, 13, 10, 12, 7, 9, 4, 4, 8, 1, 11, 14, 3, 20, 17, 10]
    print(arr_in)
    arr_out = SelectSort(arr_in)
    print(arr_out)
```

### 插入排序
```python
def InsertSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == "__main__":
    arr_in = [6, 5, 18, 2, 16, 15, 19, 13, 10, 12, 7, 9, 4, 4, 8, 1, 11, 14, 3, 20, 17, 10]
    print(arr_in)
    arr_out = InsertSort(arr_in)
    print(arr_out)
```
类似的排序还有很多例子，不一一列举

## 查找
### 线性查找
```python
def linear_search(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return i  # 返回目标元素的索引
    return -1  # 如果未找到目标元素，返回 -1

# 示例
arr = [3, 5, 2, 8, 1, 9, 4]
target = 8
result = linear_search(arr, target)
print(f"Target {target} found at index {result}")
# Target 8 found at index 3
```

## 二分查找
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # 返回目标元素的索引
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # 如果未找到目标元素，返回 -1

# 示例
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 8
result = binary_search(arr, target)
print(f"Target {target} found at index {result}")
# Target 8 found at index 7
```

## 单调栈
栈（Stack）用列表实现，从尾部取出或加入元素，用pop实现。单调栈是一种特殊的栈结构，其中的元素按照某种特定的顺序（如递增或递减）排列。
### 有效的括号
https://leetcode.cn/problems/valid-parentheses/description/?envType=problem-list-v2&envId=stack&
```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        left=['{','[','(']
        right=['}',']',')']
        for c in s:
            if c in left:
                stack.append(c)
            else:
                if not stack:
                    return False
                if left.index(stack.pop())!=right.index(c):
                    return False
        return not stack
```

### 有效路径
https://leetcode.cn/problems/simplify-path/submissions/687019514/?envType=problem-list-v2&envId=stack
```python
class Solution:
    def simplifyPath(self, path: str) -> str:
        document=list(path.split('/'))
        stack=[]
        for s in document:
            if s=='.':
                continue
            elif s=='':
                continue
            elif s=='..':
                if stack:
                    stack.pop()
            else:
                stack.append(s)
        return '/'+'/'.join(stack)
```

### 最小新整数（删数）
http://cs101.openjudge.cn/practice/04137/
```python
for  _ in range(int(input())):
    n,k=map(int,input().split())
    N=str(n)
    stack=[]
    for i in N:
        while k>0 and stack and stack[-1]>i:
            stack.pop()
            k-=1
        stack.append(i)
    while k>0:
        stack.pop()
        k-=1
    print(''.join(stack))
```
### 接雨水
https://leetcode.cn/problems/trapping-rain-water/solutions/692342/jie-yu-shui-by-leetcode-solution-tuvc/?envType=problem-list-v2&envId=stack&
```python
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = list()
        n = len(height)
        
        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                currWidth = i - left - 1
                currHeight = min(height[left], height[i]) - height[top]
                ans += currWidth * currHeight
            stack.append(i)
        return ans
```

作者：力扣官方题解
链接：https://leetcode.cn/problems/trapping-rain-water/solutions/692342/jie-yu-shui-by-leetcode-solution-tuvc/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

## 递归
递归是⼀种解决问题的方法，它涉及将⼀个问题分解成越来越小的子问题，直到得到⼀个足够小的问题，可以轻易地解决。递归涉及到⼀个函数调用自身。虽然表面上看起来可能没什么特别之处，但递归使我们能够编写出优雅的解决⽅案，来解决那些可能⾮常难以编程的问题。
### 1.汉诺塔问题
http://cs101.openjudge.cn/pctbook/M04147
```python
def Hanuota(a,b,c,N):
    if N==1:
        print(f"{1}:{a}->{c}")
    else:
        Hanuota(a,c,b,N-1)
        print(f"{N}:{a}->{c}")
        Hanuota(b,a,c,N-1)
n,a,b,c=input().split()
N=int(n)
Hanuota(a,b,c,N)
```

### 2.晶矿的个数
http://cs101.openjudge.cn/pctbook/M05585
```python
def nums(m):
    hang,lie=len(m),len(m[0])
    table=[[False for _ in range(lie)] for _ in range(hang)]
    nums_r=0
    nums_b=0

    def dfs(i,j,cry):
        if 0<=i<hang and 0<=j<lie and m[i][j]==cry and not table[i][j]:
            table[i][j]=True
            dfs(i+1,j,cry)
            dfs(i-1,j,cry)
            dfs(i,j-1,cry)
            dfs(i,j+1,cry)

    for i in range(hang):
        for j in range(lie):
            if m[i][j]=='r' and not table[i][j]:
                dfs(i,j,'r')
                nums_r+=1
            if m[i][j]=='b' and not table[i][j]:
                dfs(i,j,'b')
                nums_b+=1
    return nums_r,nums_b

k=int(input())
for _ in range(k):
    n=int(input())
    m=[[] for ___ in range(n)]
    for i in range(n):
        district=input()
        for k in district:
            m[i].append(k)
    print(*nums(m))
```
这题是标准的dfs，事实上dfs也是利用递归实现的，后面有专门刷dfs的。

### 3.Pell数列
http://cs101.openjudge.cn/pctbook/M02786/
```python
def pell(k):
    if k == 1:
        return 1
    elif k == 2:
        return 2
    a1, a2 = 1, 2
    for i in range(3, k + 1):
        a1, a2 = a2, (2 * a2 + a1) % 32767
    return a2
n = int(input())
for _ in range(n):
    k = int(input())
    print(pell(k))
```
这题类似斐波那契数列，非常基本的递归

### 4.全排列
https://leetcode.cn/problems/permutations/
```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums_list=[]
        nums_bool=[False]*len(nums)

        def permulation(A):
            if len(nums)==len(A):
                nums_list.append(A.copy())
                return
            for i in range(len(nums)):
                if not nums_bool[i]:
                    nums_bool[i]=True
                    A.append(nums[i])
                    permulation(A)
                    A.pop()
                    nums_bool[i]=False
        permulation([])
        return nums_list    
```
这题涉及到了回溯。

### 5.八皇后
http://cs101.openjudge.cn/pctbook/T02754
```python
bools=[[False]*8 for i in range(8)]
def is_safe(x,y):
    for i in range(8):
        for j in range(8):
            if bools[y][j]==True or bools[i][x]==True or (abs(x-j)==abs(y-i) and bools[i][j]==True):
                return False
    return True

ans=[]
def queen(n,num):
    if n==8:
        ans.append(num)
        return
    else:
        for x in range(8):
            if (not bools[n][x]) and is_safe(x,n):
                bools[n][x]=True
                queen(n+1,num+(x+1)*(10**n))
                bools[n][x]=False
queen(0,0)
ans.sort()

for _ in range(int(input())):
    b=int(input())
    print(ans[b-1])
```
经典的递归。

### 6.四塔问题
http://cs101.openjudge.cn/practice/01958/
```python
def three_tower(n):
    if n==1:
        return 1
    if n==0:
        return 0
    else:
        times=0
        times+=three_tower(n-1)
        times+=1
        times+=three_tower(n-1)
        return times

def four_tower(n):
    if n==1:
        return 1
    if n==0:
        return 0
    min_times = 0
    for i in range(1,n+1):
        times=0
        times+=four_tower(n-i)
        times+=three_tower(i)
        times+=four_tower(n-i)
        if times<min_times or min_times==0:
            min_times=times
    return min_times

for i in range(1,13):
    print(four_tower(i))
```
三塔问题的进阶，但是只是规模大了一点罢了。

## 并查集
并查集也包含了递归的思想，并查集的思想在于：合并两个集合，将一个集合所在的树作为另一个集合的子树即可。注意是根节点进行合并，才能保证树结构。判断两个集合是否属于同一集合——判断根节点是否相同。

模板：
```python   
parent=list(range(n+1))
def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(x, y):
    rootX=find(x)
    rootY=find(y)
    if rootX!=rootY:
        parent[rootX]=rootY
```
解读：union就是建立两个元素关系的函数，find就是找到根节点的函数

### 学校的班级个数
https://sunnywhy.com/sfbj/9/6/360
```python 
n,m=map(int,input().split())

parent = list(range(n + 1))
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
        parent[rootX] = rootY

for _ in range(m):
    a,b=map(int,input().split())
    union(a,b)

nums=0
for i in range(1,n+1):
    if parent[i]==i:
        nums+=1
print(nums)
```
或者也可以一开始count=n，表示一开始有n个班级，每次建立联系班级数-1；关于union(x,y)中的判断，在本题里可有可无，但是在某些特殊情形下不能略掉。

### 学校的班级人数
https://sunnywhy.com/sfbj/9/6/361
```python
n,m=map(int,input().split())

parent = list(range(n + 1))
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
        parent[rootX] = rootY

for _ in range(m):
    a,b=map(int,input().split())
    union(a,b)

nums=0
nums_student={}
nums_student_output=[]
for i in range(1,n+1):
    if parent[i]==i:
        nums+=1
    a=find(i)
    if a not in nums_student:
        nums_student[a] = 1
    else:
        nums_student[a]+=1
for i in nums_student:
    nums_student_output.append(nums_student[i])
nums_student_output.sort(reverse=True)
print(nums)
print(*nums_student_output)
```


### 最长连续序列
https://leetcode.cn/problems/longest-consecutive-sequence/?envType=problem-list-v2&envId=union-find
```python
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
```

### 被围绕的区域
https://leetcode.cn/problems/surrounded-regions/description/?envType=problem-list-v2&envId=union-find

这又是一道连通区域的题，本质和dfs一样（递归），如果要找连通区域个数就计算根节点的个数就好了

```python
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
```                    
### 除法求值(带权并查集)
https://leetcode.cn/problems/evaluate-division/description/?envType=problem-list-v2&envId=union-find
```python
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 1. 将字符串变量映射为数字索引
        var_map = {}
        idx = 0
        for eq in equations:
            for var in eq:
                if var not in var_map:
                    var_map[var] = idx
                    idx += 1
        
        n = idx
        # --- 你的并查集模板开始 ---
        parent = list(range(n))
        # 新增 weight 数组，weight[x] 表示 x / parent[x]
        weight = [1.0] * n

        def find(x):
            if parent[x] != x:
                # 在递归更新父节点之前，先记录当前的父节点
                origin_parent = parent[x]
                parent[x] = find(parent[x])
                # 关键：更新权值，x 到新根的比值 = (x 到旧父节点的比值) * (旧父节点到新根的比值)
                weight[x] *= weight[origin_parent]
            return parent[x]

        def union(x, y, value):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY
                # 关键：计算 rootX / rootY 的比值
                # 比例关系推导：rootX/rootY = (rootX/x) * (x/y) * (y/rootY)
                # 即：1/weight[x] * value * weight[y]
                weight[rootX] = value * weight[y] / weight[x]
        # --- 你的并查集模板结束 ---

        # 2. 构建并查集
        for i in range(len(equations)):
            var1, var2 = equations[i]
            union(var_map[var1], var_map[var2], values[i])

        # 3. 处理查询
        res = []
        for var1, var2 in queries:
            if var1 not in var_map or var2 not in var_map:
                res.append(-1.0)
                continue
            
            idx1, idx2 = var_map[var1], var_map[var2]
            root1 = find(idx1)
            root2 = find(idx2)
            
            if root1 != root2:
                res.append(-1.0) # 不连通，无法计算
            else:
                # 结果计算：var1 / var2 = (var1 / root) / (var2 / root)
                res.append(weight[idx1] / weight[idx2])
        
        return res
```

## 双端队列
### 语法
```python
from collections import deque

# 1. 初始化
d = deque()                 # 标准初始化
d = deque(maxlen=3)         # 定长队列 (类似滑动窗口)
                            # 当队列满时，添加新元素会自动“挤掉”另一端的老元素

# 2. 增删操作 (两端均为 O(1) 极快)
d.append(1)                 # 右端进
d.appendleft(2)             # 左端进
d.pop()                     # 右端出
d.popleft()                 # 左端出 (比 list.pop(0) 快得多)

# 3. 批量扩展
d.extend([3, 4])            # 右端扩展: deque([... 3, 4])
d.extendleft([5, 6])        # 左端扩展: deque([6, 5 ...]) *注意顺序是反的*

# 4. 查改与中间操作 (两端 O(1)，中间 O(n) 较慢)
v = d[0]                    # 访问两端很快
v = d[len(d)//2]            # 访问中间很慢 (需要遍历链表)
d[1] = 99                   # 修改指定位置
if 10 in d: pass            # 查找元素是否存在 O(n)

# 5. 特有功能
d.rotate(2)                 # 向右旋转2步 (尾部2个跑到头部)
d.rotate(-1)                # 向左旋转1步 (头部1个跑到尾部)
d.reverse()                 # 将队列逆序
```

### 回文数字
```python
from collections import deque
while True:
    try:
        num=input()
        num_deque=deque(num)
        if len(num_deque)==1:
            print('YES')
        else:
            is_palindrome=True
            while len(num_deque)>1:
                a=num_deque.popleft()
                b=num_deque.pop()
                if a==b:
                    continue
                else:
                    is_palindrome=False
                    break
            if is_palindrome:
                print('YES')
            else:
                print('NO')
    except EOFError:
        break
```

## 动态规划
### 最大连续子序列和Kadane
Kadane 算法用于解决 最大子数组和问题（Maximum Subarray Problem）：给定一个整数数组，找出其中连续子数组的元素和的最大值。

https://sunnywhy.com/sfbj/11/2
```python
n = int(input())
a = map(int, input().split())
dp = [0]*n
dp[0] = a[0]
for i in range(1, n):
    dp[i] = max(dp[i-1]+a[i], a[i])
print(max(dp))
```

### 最大子矩阵
```python
import sys
data=sys.stdin.read().split()
N=int(data[0])
matrix=[]
for i in range(N):
    matrix.append(list(map(int, data[N*i+1:N*(i+1)+1])))
a=0
for i in range(N):
    sum1=[0]*N
    for j in range(i,N):
        for k in range(N):
            sum1[k]+=matrix[j][k]
        dp=[0]*N
        dp[0]=sum1[0]
        for l in range(1,N):
            dp[l]=max(sum1[l],dp[l-1]+sum1[l])
        if max(dp)>a:
            a=max(dp)
print(a)
```

### 最大上升子序列
http://cs101.openjudge.cn/practice/02757
用dp做，复杂度O(N^2)
```python
N=int(input())
nums=list(map(int,input().split()))
dp=[1]*N
for i in range(1,N):
    for j in range(i):
        if nums[j]<nums[i]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))
```
但是有更快的方法(NlogN)，直接用py内置的bisect，思路是贪心：使上升子序列的末尾元素尽量小
```python
import bisect
n = int(input())
*lis, = map(int, input().split())
dp = [1e9]*n
for i in lis:
    dp[bisect.bisect_left(dp, i)] = i
print(bisect.bisect_left(dp, 1e8))
```

### 最大上升子序列和
http://cs101.openjudge.cn/pctbook/M03532

有了模板应该很好想
```python
N=int(input())
nums=list(map(int,input().split()))
dp=list(nums.copy())
for i in range(1,N):
    for j in range(i):
        if nums[i]>nums[j]:
            dp[i]=max(dp[i],dp[j]+nums[i])
print(max(dp))
```

### 0-1背包(选/不选)
由于每个物体只有两种可能的状态（取与不取），对应二进制中的0和1，这类问题便被称为「0-1背包问题」。

例题中已知条件有第 `i` 个物品的重量 `wi`，价值 `vi`，以及背包的总容量 W。

设 DP 状态 $f_{i,j}$ 为在只能放前 `i`个物品的情况下，容量为 `j` 的背包所能达到的最大总价值。

考虑转移。假设当前已经处理好了前 `i-1` 个物品的所有状态，那么对于第 `i` 个物品，当其不放入背包时，背包的剩余容量不变，背包中物品的总价值也不变，故这种情况的最大价值为 $f_{i-1,j}$；当其放入背包时，背包的剩余容量会减小 $w_{i}$，背包中物品的总价值会增大 $v_{i}$，故这种情况的最大价值为 $f_{i-1,j-w_{i}}+v_{i}$。

由此可以得出状态转移方程：

$ f_{i,j}=\max(f_{i-1,j},f_{i-1,j-w_{i}}+v_{i}) $

这里如果直接采用二维数组对状态进行记录，会出现 MLE。可以考虑改用滚动数组的形式来优化。

由于对 $f_i$ 有影响的只有 $f_{i-1}$，可以去掉第一维，直接用 $f_i$来表示处理到当前物品时背包容量为i 的最大价值，得出以下方程：

$f_j=\max \left(f_j,f_{j-w_i}+v_i\right) $

**务必牢记并理解这个转移方程，因为大部分背包问题的转移方程都是在此基础上推导出来的。**

#### 小偷背包问题
http://cs101.openjudge.cn/practice/23421
```python
N,B=map(int,input().split())
price=list(map(int,input().split()))
weight=list(map(int,input().split()))
dp=[0]*(B+1)
for i in range(N):
    for j in range(B,weight[i]-1,-1):
        dp[j]=max(dp[j],dp[j-weight[i]]+price[i])
print(max(dp))
```
总是基于“之前未包含当前物品的最优解”来更新新的状态，因此能保证每个物品在每次主循环中只会被计算一次。

#### 最长回文子串
https://leetcode.cn/problems/longest-palindromic-substring/

暴力判断的复杂度是O(N^3)，因为判断回文串会有一个O(N)，中心扩散能降低这个复杂度；dp则是用空间换了一个时间复杂度
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s

        # ---------- 第一部分：预处理所有回文子串（DP） ----------
        is_palindrome = [[False] * n for _ in range(n)]

        for right in range(n):
            for left in range(right + 1):
                if s[left] == s[right] and (right - left <= 1 or is_palindrome[left + 1][right - 1]):
                    is_palindrome[left][right] = True

        # ---------- 第二部分：扫描所有 (left, right) 求最长 ----------
        max_len = 1
        start = 0

        for left in range(n):
            for right in range(left, n):
                if is_palindrome[left][right] and (right - left + 1) > max_len:
                    max_len = right - left + 1
                    start = left

        return s[start:start + max_len]
```

### 完全背包(每种物品可以选0个-无限个)
直观来讲，转移方程是一样的，将0-1背包(小偷背包)中内层循环改为正着遍历即可
#### Cut Ribbon
https://codeforces.com/problemset/problem/189/A
```python
n, a, b, c = map(int, input().split())
dp = [0]+[float('-inf')]*n
for i in range(1, n+1):
    for j in (a, b, c):
        if i >= j:
            dp[i] = max(dp[i-j] + 1, dp[i])
print(dp[n])
```

### 多重背包(每种物品数量有上限)
最简单的思路是将多个同样的物品看成多个不同的物品，从而化为0-1背包。稍作优化：可以改善拆分方式，譬如将m个1拆成x_1,x_2,……,x_t个1，只需要这些x_i中取若干个的和能组合出1至m即可。最高效的拆分方式是尽可能拆成2的幂，也就是所谓“二进制优化”。(这个好难，会不了一点)
```python
import sys

def solve():
    # 读取所有输入，按空格分割
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    while ptr < len(input_data):
        n = int(input_data[ptr])
        m = int(input_data[ptr + 1])
        ptr += 2
        
        # 结束标志
        if n == 0 and m == 0:
            break
        
        # 按照题目描述，前 n 个是面值 A，后 n 个是数量 C
        a = []
        for i in range(n):
            a.append(int(input_data[ptr + i]))
        ptr += n
        
        c = []
        for i in range(n):
            c.append(int(input_data[ptr + i]))
        ptr += n
        
        # bits 的第 k 位为 1 表示金额 k 可以凑出
        # 初始只有 bits[0] = 1
        bits = 1
        # 掩码，用于限制金额不超过 m (即全 1 的二进制，长度为 m+1)
        mask = (1 << (m + 1)) - 1
        
        for i in range(n):
            val = a[i]
            count = c[i]
            
            # 优化：如果该种硬币总面值已超过 m，则视为无限个（完全背包）
            # 或者直接进行二进制拆分
            k = 1
            while k <= count:
                bits |= (bits << (k * val))
                bits &= mask # 及时截断，保证位运算效率
                count -= k
                k *= 2
            
            if count > 0:
                bits |= (bits << (count * val))
                bits &= mask
            
            # 剪枝：如果 1 到 m 全都能凑出了，直接退出
            if bits == mask:
                break
        
        # 计算 bits 中 1 的个数（排除掉第 0 位，因为题目要求金额从 1 到 m）
        # Python 3.10+ 使用 bit_count()，旧版本使用 bin().count('1')
        if hasattr(bits, "bit_count"):
            ans = bits.bit_count() - 1
        else:
            ans = bin(bits).count('1') - 1
            
        sys.stdout.write(str(ans) + '\n')

if __name__ == "__main__":
    solve()
```

### 恰好型背包
#### 健身房
http://cs101.openjudge.cn/practice/21458/
```python
t,n=map(int,input().split())
dp=[0]+[-1]*(t+1)
for i in range(n):
    k,w=map(int,input().split())
    for j in range(t,k-1,-1):
        if dp[j-k]!=-1:
            dp[j]=max(dp[j-k]+w,dp[j])
print(dp[t])
```

### 最长回文子串/子序列
字符类的问题，一般都是二维dp
#### 最长回文子串
https://leetcode.cn/problems/longest-palindromic-substring/solutions/255195/zui-chang-hui-wen-zi-chuan-by-leetcode-solution/
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        
        max_len = 1
        begin = 0
        # dp[i][j] 表示 s[i..j] 是否是回文串
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        
        # 递推开始
        # 先枚举子串长度
        for L in range(2, n + 1):
            # 枚举左边界，左边界的上限设置可以宽松一些
            for i in range(n):
                # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
                j = L + i - 1
                # 如果右边界越界，就可以退出当前循环
                if j >= n:
                    break
                    
                if s[i] != s[j]:
                    dp[i][j] = False 
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                
                # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        return s[begin:begin + max_len]
```
#### 最长回文子序列
https://leetcode.cn/problems/longest-palindromic-subsequence/solutions/930442/zui-chang-hui-wen-zi-xu-lie-by-leetcode-hcjqp/
```python
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]
```

### 最长公共子串/子序列
典型的二维dp，子串是连续的比较好想，矩阵里面沿一条斜线逐个累加，其他位置都是0；子序列不连续，于是详细写出：
#### 公共子序列
http://cs101.openjudge.cn/practice/02806/

dp的思路是：如果两个字母不相同，则取左边和上面的较大的一个，如果相同，则是左上方的加一
```python
while True:
    try:
        a,b=input().split()
    except EOFError:
        break

    lena=len(a)
    lenb=len(b)
    dp=[[0]*(lena+1) for _ in range(lenb+1)]
    for i in range(1,lenb+1):
        for j in range(1,lena+1):
            if b[i-1]==a[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    print(dp[lenb][lena])
```

### 双dp数组
#### 1195C. Basketball Exercise
https://codeforces.com/problemset/problem/1195/C
```python
n=int(input())
h1=list(map(int,input().split()))
h2=list(map(int,input().split()))
dp1=[0]*n
dp2=[0]*n
dp1[0]=h1[0]
dp2[0]=h2[0]
for i in range(1,n):
    dp1[i]=max(dp2[i-1]+h1[i],dp1[i-1])
    dp2[i]=max(dp1[i-1]+h2[i],dp2[i-1])
print(max(dp1[-1],dp2[-1]))
```

#### 摆动序列
http://cs101.openjudge.cn/pctbook/M26976/

经典的摆动序列也可以用dp
```python
n=int(input())
nums=list(map(int,input().split()))
dp_up=[1]*n
dp_down=[1]*n
for i in range(1,n):
    if nums[i]>nums[i-1]:
        dp_up[i]=max(dp_down[i-1]+1,dp_up[i-1])
        dp_down[i]=dp_down[i-1]
    elif nums[i]<nums[i-1]:
        dp_down[i]=max(dp_down[i-1],dp_up[i-1]+1)
        dp_up[i]=dp_up[i-1]
    else:
        dp_up[i]=dp_up[i-1]
        dp_down[i]=dp_down[i-1]
print(max(dp_up[-1],dp_down[-1]))
```

## 搜索
### dfs
#### 模板1:迷宫可行路径数
https://sunnywhy.com/sfbj/8/1/313

对于只能向右、向下的此类题，dp可以解决，但是如果是各个方向行走，则只能使用dfs
对于状态的传递，可以尝试使用全局变量，也可以采用函数内部的变量。
```python
n,m=map(int,input().split())
matrix=[]
for i in range(n):
    matrix.append(list(map(int,input().split())))
visited=[[False]*m for _ in range(n)]

def dfs(i,j):
    count=0
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
```

#### 模板2:指定步数的迷宫问题
https://sunnywhy.com/sfbj/8/1/314
```python
n, m, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def dfs(i, j, count):
    if not (0<=i<n and 0<=j<m) or matrix[i][j]==1 or visited[i][j]:
        return False
    if count == k:
        return i==n-1 and j==m-1
    visited[i][j] = True
    if (dfs(i,j+1, count+1) or dfs(i+1,j,count+1) or dfs(i,j-1,count+1) or dfs(i-1,j,count+1)):
        return True
    visited[i][j] = False
    return False
if matrix[0][0] == 0 and dfs(0, 0, 0):
    print("Yes")
else:
    print("No")
```

#### dfs小技巧
遇到递归深度不够，用sys
```python
import sys
sys.setrecursionlimit(20000)
```
如果dfs内部有类似于dp数组需要不断访问某些元素的值的时候，除了开空间创建一个dp，还可以用lru_cache。
但一定要在需要进行记忆化递归的函数头顶上写，否则无效。
```python
from functools import lru_cache
@lru_cache(maxsize=2048) #或者更大，如None，考虑内存因素自行调整
def dfs():
    ...
```
例子是滑雪，这题有dp的味道

http://cs101.openjudge.cn/pctbook/M01088/
```python
from functools import lru_cache
import sys
sys.setrecursionlimit(10000)
R,C=map(int,input().split())
matrix=[]
for _ in range(R):
    matrix.append(list(map(int,input().split())))

@lru_cache(maxsize=None)
def dfs(i,j):
    length=1
    for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
        if 0<=i+di<R and 0<=j+dj<C and matrix[i+di][j+dj]<matrix[i][j]:
            k=dfs(i+di,j+dj)
            if k+1>length:
                length=k+1
    return length
max_length=0
for i in range(R):
    for j in range(C):
        ans=dfs(i,j)
        if ans>max_length:
            max_length=ans
print(max_length)
```

### bfs
#### 模板1：数字操作(1维bfs)
https://sunnywhy.com/sfbj/8/2/318
```python
from collections import deque
def bfs(start, end):
    q = deque([(0, start)])  # (step, start)
    in_queue = {start}
    while q:
        step, front = q.popleft()  # 取出队首元素
        if front == end:
            return step
        #上面是通用的
        a=front+1
        b=2*front
        if a not in in_queue and a<=n:
            in_queue.add(a)
            q.append((step+1,a))
        if b not in in_queue and b<=n:
            in_queue.add(b)
            q.append((step+1,b))
n=int(input())
print(bfs(1,n))
```
模板后面的部分也有可说的：1.必须要检查是否重复入队，否则复杂度大大增加；2.要检查是否到达end值，否则会导致越界或复杂度增加。

#### 模板2:连通分量计数(dfs和bfs都可以的)
https://sunnywhy.com/sfbj/8/2/319

经典的问题，可以用dfs，也可以用bfs；
```python
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
```
其实bfs和dfs解决这个问题的思路的一样的：先检索满足条件的块的边界，然后计数并搜索整个块，把整个块染色后继续；bfs的思路就是先有一个开始的坐标，接着对于每个入队的点，逐步扩散出去，检测是否入队就用visited数组

#### 迷宫最短路径的步数
https://sunnywhy.com/sfbj/8/2/320

这个背景在前面dfs的模板也见到了，但是求的东西不一样。
```python
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
```


