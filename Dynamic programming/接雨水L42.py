from typing import List
class Solution:
    """
    给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
    """
    def trap(self, height: List[int]) -> int:
        # 动态规划思想遍历获取每一格左右的最高高度

        sum = 0
        n = len(height)
        if n == 0 or n == 1:
            return 0

        right_h = [0] * n
        left_h = height[0]
        right_h[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            right_h[i] = max(right_h[i + 1], height[i])
        for i in range(n):
            left_h = max(left_h, height[i])
            sum += min(left_h, right_h[i]) - height[i]
        return sum