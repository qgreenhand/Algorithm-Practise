from typing import List
class Solution:
    """
    一支弓箭可以沿着 x 轴从不同点完全垂直地射出。在坐标 x 处射出一支箭，
    若有一个气球的直径的开始和结束坐标为 xstart，xend， 且满足  xstart ≤ x ≤ xend，则该气球会被引爆。可以射出的弓箭的数量没有限制。
    弓箭一旦被射出之后，可以无限地前进。我们想找到使得所有气球全部被引爆，所需的弓箭的最小数量。
    """
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        贪心思想，
        按照最右端排序，找到当前能射爆的最多气球位置
        :param points:
        :return:
        """
        if not points:
            return 0

        points.sort(key=lambda balloon: balloon[1])
        pos = points[0][1]
        ans = 1
        for balloon in points:
            if balloon[0] > pos:
                pos = balloon[1]
                ans += 1

        return ans
