from typing import List
class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]

    def find(self, x1):
        if x1 == self.parent[x1]:
            return x1
        self.parent[x1] = self.find(self.parent[x1])
        return self.parent[x1]

    def union(self, x1, x2):
        self.parent[self.find(x1)] = self.find(x2)


class Solution:
    """
    输入一个图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。
    结果图是一个以边组成的二维数组。每一个边的元素是一对[u, v] ，满足 u < v，表示连接顶点u 和v的无向图的边。
    返回一条可以删去的边，使得结果图是一个有着N个节点的树。如果有多个答案，则返回二维数组中最后出现的边。答案边 [u, v] 应满足相同的格式 u < v。

    并查集练习
    """
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        disjointSet = DisjointSet(max(map(max, edges)))                   # map函数 求二维数组中的最大值 函数式编程典型应用
        for e1, e2 in edges:
            if disjointSet.find(e1) == disjointSet.find(e2):
                return [e1, e2]
            else:
                disjointSet.union(e1, e2)