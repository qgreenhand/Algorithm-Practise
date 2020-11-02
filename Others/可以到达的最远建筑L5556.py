import heapq
from typing import List
class Solution:
    """
    给你一个整数数组 heights ，表示建筑物的高度。另有一些砖块 bricks 和梯子 ladders 。

    你从建筑物 0 开始旅程，不断向后面的建筑物移动，期间可能会用到砖块或梯子。

    当从建筑物 i 移动到建筑物 i+1（下标 从 0 开始 ）时：

    如果当前建筑物的高度 大于或等于 下一建筑物的高度，则不需要梯子或砖块
    如果当前建筑的高度 小于 下一个建筑的高度，您可以使用 一架梯子 或 (h[i+1] - h[i]) 个砖块

    如果以最佳方式使用给定的梯子和砖块，返回你可以到达的最远建筑物的下标（下标 从 0 开始 ）。
    """
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        """
        先全部上梯子
        然后建立一个小根堆
        当梯子不够时取出一个最小值用砖块代替
        """
        n = len(heights)
        # 由于我们需要维护最大的 l 个值，因此使用小根堆
        q = list()
        # 需要使用砖块的 delta h 的和
        sumH = 0
        for i in range(1, n):
            deltaH = heights[i] - heights[i - 1]
            if deltaH > 0:
                heapq.heappush(q, deltaH)
                # 如果优先队列已满，需要拿出一个其中的最小值，改为使用砖块
                if len(q) > ladders:
                    sumH += heapq.heappop(q)
                if sumH > bricks:
                    return i - 1
        return n - 1