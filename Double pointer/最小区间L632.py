import heapq

from typing import List
class Solution:
    '''
    你有 k 个升序排列的整数数组。找到一个最小区间，使得 k 个列表中的每个列表至少有一个数包含在其中
    '''

    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        '''
        大概思路是多指针
        为每个数组建个指针
        每次考虑这些指针所指的的最小和最大值
        维持最小窗口
        每次是最小值对应指针前移
        这个里面最小采用的是优先队列的方法做的优化
        '''
        heap = []
        n = len(nums)
        mi = float('inf')
        ma = float('-inf')
        for i in range(n):
            heapq.heappush(heap, (nums[i][0], 0, i))
            mi = min(mi, nums[i][0])
            ma = max(ma, nums[i][0])

        res = [mi, ma]
        while True:
            cur = heapq.heappop(heap)
            if cur[1] == len(nums[cur[2]]) - 1:
                break
            heapq.heappush(heap, (nums[cur[2]][cur[1] + 1], cur[1] + 1, cur[2]))
            ma = max(ma, nums[cur[2]][cur[1] + 1])
            mi = heap[0][0]
            if ma - mi < res[1] - res[0]:
                res = [mi, ma]
            elif ma - mi == res[1] - res[0] and mi < res[0]:
                res = [mi, ma]
        return res
