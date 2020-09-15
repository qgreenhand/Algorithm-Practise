'''
建议看这个
https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/da-jia-bu-yao-kan-labuladong-de-jie-fa-fei-chang-2/
'''
from typing import List


class Solution:
    '''
    给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
    这个题目我用的方法不太好，建议去看上面网址比较有价值
    '''

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        flag = 0
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                flag = 1
                break
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        if flag == 0:
            return [-1, -1]
        else:
            start = end = mid
            while start >= 0:
                if nums[start] != target:
                    break
                if nums[start] == target:
                    start = start - 1
            while end < len(nums):
                if nums[end] != target:
                    break
                if nums[end] == target:
                    end = end + 1

                # print(start,end)

            start = start + 1
            end = end - 1
            return [start, end]