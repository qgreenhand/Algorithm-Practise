from typing import List


class Solution:
    """
    给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
    设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
    你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
    卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。

    """

    def maxProfit(self, prices: List[int]) -> int:
        """
        动态规划
        考虑用dp数组存储
        dp[i][0]表示当前未持有股票且进入第i天
        dp[i][1]表示当前已持有且进入i天
        """
        if not prices:
            return 0
        dp = [[0] * 2 for _ in range(len(prices))]
        for i in range(len(prices)):
            dp[i][1] = 0 - prices[i]
        for i in range(1, len(prices)):

            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            if i >= 3:
                dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
            else:
                dp[i][1] = max(dp[i - 1][1], dp[i][1])
            print(i, dp[i][0], dp[i][1])
        return dp[len(prices) - 1][0]
