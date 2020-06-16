from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        寻找子集
        :param nums:
        :return:
        '''
        self.res = []
        self.backtrack([], 0, nums)

        return self.res

    def backtrack(self, sol, index, nums):
        self.res.append(sol)

        for i in range(index, len(nums)):
            self.backtrack(sol + [nums[i]], i + 1, nums)

s=Solution()
print(s.subsets([1,2,3]))
