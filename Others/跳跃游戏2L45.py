from typing import List
class Solution:
    '''
    说实话没大看懂，
    今年天太热刚拖得地实在不想看了
    看题解第三个比较好理解
    '''
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step