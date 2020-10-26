from typing import List
class Solution:
    '''
    并查集题目
    给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串方程 equations[i] 的长度为 4，并采用两种不同的形式之一：
    "a==b" 或 "a!=b"。
    在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。
    只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回 true，否则返回 false。

    '''

    class UnionFind:
        def __init__(self):
            # 一般来说并查集初始化为它自己
            self.parent = list(range(26))

        def find(self, index):
            if index == self.parent[index]:
                return index
            #同时做路径压缩，经过这一步儿子节点都指向并查集的根节点防止出现单链形式降低性能
            self.parent[index] = self.find(self.parent[index])
            return self.parent[index]

        def union(self, index1, index2):
            self.parent[self.find(index1)] = self.find(index2)

    def equationsPossible(self, equations: List[str]) -> bool:
        uf = Solution.UnionFind()
        for st in equations:
            # 将相等的并入一个子集
            if st[1] == "=":
                index1 = ord(st[0]) - ord("a")
                index2 = ord(st[3]) - ord("a")
                uf.union(index1, index2)
        for st in equations:
            #如果发生矛盾就返回错误
            if st[1] == "!":
                index1 = ord(st[0]) - ord("a")
                index2 = ord(st[3]) - ord("a")
                if uf.find(index1) == uf.find(index2):
                    return False
        return True