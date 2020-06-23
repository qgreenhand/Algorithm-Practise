from typing import List
class Solution:
    '''
    搜索旋转排序数组
    '''
    def search(self, nums: List[int], target: int) -> int:
        '''
        考虑旋转数组，采取二分查找的思想
        考虑要是中间比右端大代表左端完全升序
        反之则右端完全升序
        :param nums:
        :param target:
        :return:
        '''

        left=0
        right=len(nums)-1

        while left<=right:
            mid = (left + right) // 2
            print(left,right,mid)
            if nums[mid]==target:
                return mid
            if nums[mid]>nums[right] :        #此时左半部分完全升序
                if target<nums[mid]and target>=nums[left]:
                    right=mid-1
                else:
                    left=mid+1
            else:                            #此时右半部分完全升序
                if target>nums[mid] and target<=nums[right]:
                    left = mid + 1
                else:
                    right=mid-1

        return -1