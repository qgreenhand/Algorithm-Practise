class Solution:
    '''
        给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，并返回其长度。如果不存在符合条件的连续子数          组,返回 0。
    '''
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        '''
        双指针法
        '''
        if not nums:
            return 0
        i=j=0
        sumnum=0
        minlenth=len(nums)+1
        while j<len(nums)+1:
            if sumnum<s:
                if j==len(nums):
                    break
                sumnum+=nums[j]
                j=j+1
            else:
                print(i,j)
                minlenth=min(minlenth,j-i)
                sumnum-=nums[i]
                i=i+1
        if minlenth==len(nums)+1:
            return 0
        return minlenth