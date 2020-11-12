from typing import List
class Solution:

    """
    有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。

    现在要求你戳破所有的气球。如果你戳破气球 i ，就可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球
    i 后， 气球 left 和气球 right 就变成了相邻的气球。 求所能获得硬币的最大数量。


    """

    def maxCoins(self, nums: List[int]) -> int:
        """
        动态规划感觉好像思路蛮简单的但是是困难题
        时间复杂度得n^3
        。。。。。。。。。。。。
        2020/09/15
        看到题目没想出来
        。。。。。。。。。。。。
        2020/11/11
        卧槽看到题目又蒙蔽了
        核心思想在这我之前都没发现？？？
        我们观察戳气球的操作，发现这会导致两个气球从不相邻变成相邻，使得后续操作难以处理。于是我们倒过来看这些操作，将全过程看作是每次添加一个气球。

        主要是记忆化搜索
        rec[i][j]  表示（i，j） 所能产生的最大硬币数注意这里是开区间
        后面的话就很容易理解了
        为了方便这里在原数组头和尾添加了两个 "1" 气球

        """
        n = len(nums)
        rec = [[0] * (n + 2) for _ in range(n + 2)]
        val = [1] + nums + [1]

        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n + 2):
                for k in range(i + 1, j):
                    total = val[i] * val[k] * val[j]
                    total += rec[i][k] + rec[k][j]
                    rec[i][j] = max(rec[i][j], total)

        return rec[0][n + 1]
