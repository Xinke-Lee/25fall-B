class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        parent = {}
        # weight[x] 存储的是 x / parent[x] 的比值
        weight = {}
        def find(x):
            if parent[x] != x:
                # 记录当前的父节点，用于在路径压缩后更新权值
                origin_parent = parent[x]
                parent[x] = find(parent[x])
                # 更新权值：x / new_root = (x / old_parent) * (old_parent / new_root)
                weight[x] *= weight[origin_parent]
            return parent[x]
        def union(x, y, val):
            # 初始化新变量
            for var in [x, y]:
                if var not in parent:
                    parent[var] = var
                    weight[var] = 1.0
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY
                # 计算 rootX / rootY 的比值
                weight[rootX] = val * weight[y] / weight[x]
        # 1. 建立带权并查集
        for (a, b), val in zip(equations, values):
            union(a, b, val)
        # 2. 处理查询
        res = []
        for a, b in queries:
            if a not in parent or b not in parent:
                res.append(-1.0)
            else:
                rootA = find(a)
                rootB = find(b)
                if rootA != rootB:
                    res.append(-1.0)  # 不在同一个连通分量，无法确定比值
                else:
                    # a / b = (a / root) / (b / root)
                    res.append(weight[a] / weight[b])
        return res