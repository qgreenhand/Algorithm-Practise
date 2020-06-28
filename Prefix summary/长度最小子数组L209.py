from typing import List
import bisect

class Solution:

    '''
        给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，并返回其长度。如果不存在符合条件的连续子数组,返回 0。
    '''

    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        '''
        另一种前缀和配合二分查找的方法
        :param s:
        :param nums:
        :return:
        '''
        if not nums: return 0
        # 求前缀和
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        # print(nums)
        # 总和都小于 s 时候
        if nums[-1] < s: return 0
        res = float("inf")
        nums = [0] + nums
        for i in range(1, len(nums)):
            if nums[i] - s >= 0:
                # 二分查找
                loc = bisect.bisect_left(nums, nums[i] - s)
                if nums[i] - nums[loc] >= s:
                    res = min(res, i - loc)
                    continue
                if loc > 0:
                    res = min(res, i - loc + 1)
        return res


    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        '''
        双指针法
        '''
        if not nums:
            return 0
        i=j=0
        sumnum=0
        minlenth=len(nums)+1
        while j<len(nums)+1:
            if sumnum<s:
                if j==len(nums):
                    break
                sumnum+=nums[j]
                j=j+1
            else:
                print(i,j)
                minlenth=min(minlenth,j-i)
                sumnum-=nums[i]
                i=i+1
        if minlenth==len(nums)+1:
            return 0
        return minlenth