from typing import List
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        """
        贪心做法
        还可以用动态规划
        这里贪心做法和“跳跃游戏”类似
        :param clips:
        :param T:
        :return:
        """
        # 用于记录对当前位置能达到的最大值
        maxend = [0] * T
        for s, e in clips:
            if s < T:
                maxend[s] = max(maxend[s], e)

        res = 0
        pre = 0
        last = 0
        for i in range(T):
            last = max(last, maxend[i])
            if i == last:
                #说明当前位置已经到达当前可以到达的最大值
                return -1
            if i == pre:
                #说明跑到了上一个区间的最末端，需要开启新的区间
                pre = last
                res += 1
        return res