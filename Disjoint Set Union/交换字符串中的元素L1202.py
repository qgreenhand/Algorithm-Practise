from typing import List

class UnionSearch:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x1, x2):
        self.parent[self.find(x1)] = self.find(x2)


class Solution:
    """
    给你一个字符串 s，以及该字符串中的一些「索引对」数组 pairs，其中 pairs[i] = [a, b] 表示字符串中的两个索引（编号从 0 开始）。
    你可以 任意多次交换 在 pairs 中任意一对索引处的字符。
    返回在经过若干次交换后，s 可以变成的按字典序最小的字符串。
    """

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        """
        使用并查集，每次填入可填入的最小字母
        这个方法超时了，官方题解使用优先队列进行了优化。
        对每个并查集代表元建立一个优先队列用于存储对应位置可以添加的可能元素，这样就可以直接弹出最小字典序字母。
        :param s:
        :param pairs:
        :return:
        """
        unionSearch = UnionSearch(len(s))

        for i, j in pairs:
            unionSearch.union(i, j)
        used = [0] * len(s)
        res = ""
        for i in range(len(s)):
            cur = 'z'
            curitem = -1
            for j in range(len(s)):
                if used[j] == 0 and unionSearch.find(j) == unionSearch.find(i) and s[j] <= cur:
                    cur = s[j]
                    curitem = j
            res += cur
            used[curitem] = -1
        return res
