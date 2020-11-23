from typing import List


class Solution:
    """
    魔术索引。 在数组A[0...n-1]中，有所谓的魔术索引，满足条件A[i] = i。给定一个有序整数数组，编写一种方法找出魔术索引，若有的话，在数组A中找出一个魔
    术索引，如果没有，则返回-1。若有多个魔术索引，返回索引值最小的一个。

    """

    def findMagicIndex(self, nums: List[int]) -> int:
        """
        考虑二分查找
        由于抽屉原理当i-nums[i]>=i查找左半部分否则右半部分
        由于找左边界考虑左开右闭
        但是实际上这种做法错误因为不保证有没有重复元素
        下面跳跃法
        """

        if not nums:
            return -1
        if nums[0] == 0:
            return 0
        p, n = 0, len(nums)
        while p < n:
            if nums[p] > p:
                p = nums[p]
            elif nums[p] == p:
                return p
            else:
                p += 1
        return -1
