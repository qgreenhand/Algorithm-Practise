from typing import List
class Solution:
    '''
    给定一个非负整数数组，你最初位于数组的第一个位置。
    数组中的每个元素代表你在该位置可以跳跃的最大长度。
    判断你是否能够到达最后一个位置
    '''

    def canJump(self, nums: List[int]) -> bool:
        # 想法是把所有值为0的都提出来看前面能否有点可以绕过。
        lenth = len(nums)
        if (lenth == 1):
            return True
        answer = True
        for i in range(lenth - 1):
            if nums[i] == 0:
                oneanswer = False
                for j in range(i - 1, -1, -1):
                    if nums[j] > i - j:
                        oneanswer = True
                        break
                if oneanswer == False:
                    answer = False
                    break
        return answer
    def canJump1(self, nums: List[int]) -> bool:
        #每次记录能跑到的最远点，要是这个点达不到就gg
        farest=0
        for i in range(len(nums)):
            if i >farest:
                return False
            farest=max(farest,i+nums[i])
        return True




s=Solution()
print(s.canJump([0]
))





