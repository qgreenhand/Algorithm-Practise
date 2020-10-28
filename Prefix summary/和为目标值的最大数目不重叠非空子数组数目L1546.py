from typing import List
class Solution:
    """
    给你一个数组 nums 和一个整数 target 。
    请你返回 非空不重叠 子数组的最大数目，且每个子数组中数字和都为 target 。
    """
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        """
        由于题目要求所有的子数组互不重叠，因此对于某个满足条件的子数组
        ，如果其右端点是所有满足条件的子数组的右端点中最小的那一个，则该子数组一定会被选择。
        采用贪心算法和前缀和的方法，用个set保存出现过的前缀和，当满足和为target的子数组出现，清空set，res+=1
        :param nums:
        :param target:
        :return:
        """
        s = {0}
        presum = 0
        res = 0
        for i in nums:
            presum += i
            if presum - target in s:
                #清空set防止出现重叠的答案
                res += 1
                s = {0}
                presum = 0
            else:
                s.add(presum)
        return res

