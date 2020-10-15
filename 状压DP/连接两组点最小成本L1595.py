from functools import lru_cache
from typing import List
class Solution:
    """
    给你两组点，其中第一组中有 size1 个点，第二组中有 size2 个点，且 size1 >= size2 。
    """
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        """
        思路是状压DP
        简单来说这道题可以看作先满足第一组，结束之后看第二组还有哪些未连接的点再进行连接
        由于题目的数据限制考虑状态压缩DP
        压缩第二组的状态
        我在官网上找到了一个较好理解的版本

        :param cost:
        :return:
        """

        m, n = len(cost), len(cost[0])
        mi = [min(cost[i][j] for i in range(m)) for j in range(n)]  # 预处理第二组每个点的最小cost

        @lru_cache(None)
        def dp(i, used):
            if i == m:  # 第一组点全部选完后，处理第二组还没选的点的最小成本和
                ans = 0
                for j in range(n):
                    if not 1 << j & used:  # 如果第二组这个点没被选过，那么就选它在第一组中最小代价点
                        ans += mi[j]
                return ans
            res = float('inf')
            for j in range(n):
                res = min(res, cost[i][j] + dp(i + 1, used | 1 << j))  # 转移方程
            return res

        return dp(0, 0)

