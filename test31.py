from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        寻找下一个排列
        '''
        i=j=0
        flag=0         #是否没有下一个排列
        for i in range(len(nums)-1,0,-1):
            if nums[i-1]<nums[i]:
                for j in range(len(nums)-1,i-1,-1):
                    if nums[j]>nums[i-1]:
                        tmp=nums[i-1]
                        nums[i-1]=nums[j]
                        nums[j]=tmp
                        break
                flag=1
                break
        j=len(nums)-1
        if flag==0:
            i=0
        while i<j:
            tmp = nums[i ]
            nums[i ] = nums[j]
            nums[j] = tmp
            i=i+1
            j=j-1


