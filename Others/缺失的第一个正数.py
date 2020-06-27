from typing import List
class Solution:

    '''
    给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。
    这个题目主要难点在于如何使用常数空间
    题目使用hash表的方法  通过打负号的方式使数组具有hash表功能
    不懂看官方题解
    '''

    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # 遍历一遍如果数小于0代表不在1~n-1 之间 把他设置为N+1 排除所有负数
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        # 如果数是在1~N-1  之间打上负号作为标记
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])
        # 遍历找到第一个未标记的
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1