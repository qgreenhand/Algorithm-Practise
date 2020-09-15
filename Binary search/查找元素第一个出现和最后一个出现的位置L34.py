'''
建议看这个
https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/da-jia-bu-yao-kan-labuladong-de-jie-fa-fei-chang-2/
'''
from typing import List


class Solution:
    '''
    给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
    求数组第一个位置函数是searchFirst。。。还是挺简单的之前被tm前面那个题解忽悠了。。。。
    2020/09/15
    当然searchLast同理
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


    def searchFirst(self, nums: List[int], target: int):
        """
        通过二分查找找到出现的第一个target的下标
        :param nums:
        :param target:
        :return:
        """
        start=0
        end=len(nums)-1

        while(start<=end):
            mid=start+(start-end)//2            #另外求mid的时候最好这么写，这样写可以防止start end 过大 start+end导致和值溢出
            if nums[mid]==target:               #由于是要找到第一个出现的所以就算找到了还是要向左边找
                end=mid-1
            elif nums[mid]>target:
                end=mid-1
            elif nums[mid]<target:
                start =mid+ 1
        if nums[start]==target and start<len(nums)-1:   #此时 start 和 end 的位置关系是 [start, end] 所以需要对start进行边界判断
            return start
        else:
            return -1