L,M=map(int,input().split())
length=[]
for i in range(L+1):
        length.append(i)
for i in range(M):
    a,b=map(int,input().split())
    for i in range(a,b+1):
        if i in length:
            length.remove(i)
print(len(length))
##超时！以下是优化
'''
L, M = map(int, input().split())
# 创建一个集合，包含从0到L的所有树的位置
trees_set = set(range(L + 1))

for i in range(M):
    a, b = map(int, input().split())
    # 对于区间[a, b]内的每一个位置，从集合中移除
    for j in range(a, b + 1):
        # 如果j在集合中，则移除。注意：使用discard可以避免如果j不在集合中而报错，但这里j应该在集合中，因为初始是0到L。但是如果有重复区域，可能已经移除了，所以用discard更安全。
        trees_set.discard(j)

print(len(trees_set))
'''
