from typing import List


class UnionSearch:
    def __init__(self, n):
        self.parent = [_ for _ in range(n)]

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x1, x2):
        self.parent[self.find(x1)] = self.find(x2)


class Solution:
    """
    有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。
    省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
    给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。
    返回矩阵中 省份 的数量。
    """

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        unionSet = UnionSearch(len(isConnected))
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    unionSet.union(i, j)
        res = 0
        for i in range(len(isConnected)):
            if unionSet.find(i) == i:
                res += 1
        return res


s = Solution()
print(s.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
