from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        1. 先排序再弄
        '''
        number=nums[0]
        result=nums[0]
        count=0
        new=sorted(nums)
        for i in range(0,len(new)):
            if number!=new[i]:
                number=new[i]
                count=0
            if number==new[i]:
                count+=1

            if count>=len(new)/2:
                result=new[i]
                break

        return result
class Solution:
    '''
    投票算法
    '''
    def majorityElement(self, nums: List[int]) -> int:
        count, majority = 1, nums[0]
        for num in nums[1:]:
            if count == 0:
                majority = num
            if num == majority:
                count += 1
            else:
                count -= 1
        return majority





