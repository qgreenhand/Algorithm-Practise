from typing import List

"""
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        这道题其实就是有没有组合使得和值为sum(nums)//2

        这道题转化为01背包问题
        dp[i][j]代表第[0：i]有没有可能使组合和为j

        :param nums:
        :return:
        """
        n = len(nums)
        if n < 2:
            return False

        total = sum(nums)
        maxNum = max(nums)
        if total & 1:
            return False

        target = total // 2
        if maxNum > target:
            return False

        dp = [[0] * (target + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True

        dp[0][nums[0]] = True
        for i in range(1, n):
            num = nums[i]
            for j in range(1, target + 1):
                if j >= num:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - num]
                else:
                    dp[i][j] = dp[i - 1][j]

        return bool(dp[n - 1][target])
