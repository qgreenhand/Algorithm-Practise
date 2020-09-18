from typing import List


class Solution:
    '''
    给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
    '''
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack([], 0, nums)

        return self.res

    def backtrack(self, sol, index, nums):
        self.res.append(sol)

        for i in range(index, len(nums)):
            self.backtrack(sol + [nums[i]], i + 1, nums)