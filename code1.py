from typing import List
class Solution:

    def reverseNumber(self, x,y) :
        dp=[[0]*x for _ in range(y)]
        for j in range(x):
            for i in range(y):
                if i==0 or j==0:
                    dp[i][j]=1
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return  dp[y-1][x-1]
s=Solution()
print(s.reverseNumber(20,20))
