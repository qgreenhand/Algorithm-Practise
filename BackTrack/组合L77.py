from typing import List
class Solution:
    """
    给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
    """
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        回溯算法练习。。。
        :param n:
        :param k:
        :return:
        """

        haveused=[]
        res=[]
        def dfs(cur,k):
            
            if k==0:
                
                res.append(haveused[:])
                return
            for i in range(cur,n+1):
                if i not in haveused:
                    haveused.append(i)
                    dfs(i,k-1)
                    haveused.pop()
        dfs(1,k)
        return res
            