from typing import List
class Solution:

    def reversePairs(self, nums: List[int]) -> int:
        '''
        之前做过，采用类似归并排序的做法
        '''
        result=0
        def do(nums):
            nonlocal result
            r=[]
            if len(nums)==1:
                return nums
            mid=len(nums)//2
            left=do(nums[:mid])
            right=do(nums[mid:])
            print(left ,right)
            i=j=0
            while i<len(left) and j<len(right):
                if left[i]<=right[i]:
                    r.append(left[i])
                    i+=1
                else:
                    r.append(right[j])
                    result=result+len(left)-i
                    j+=1
            while i<len(left):
                r.append(left[i])
                i+=1
            while j<len(right):
                r.append(right[j])
                j+=1
            return r
        do(nums)
        return result
s=Solution()
print(s.reversePairs([7,5,6,4]))
