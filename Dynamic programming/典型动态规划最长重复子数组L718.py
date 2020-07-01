from typing import List
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        '''
        算是经典动态规划
        给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
        '''
        i=0
        j=0
        dp=[[0]*(len(A)+1) for _ in range(len(B)+1)]
        max_lenth=0
        for i in range(1,len(A)+1):
            for j in range(1,len(B)+1):
                if A[i-1]==B[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                    max_lenth=max(max_lenth,dp[i][j])
                else:
                    dp[i][j]=0
        return max_lenth