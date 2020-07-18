class Solution(object):
    '''
  给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的
    '''
    def isInterleave(self, s1, s2, s3):
        '''
        动态规划
        假设dp[i][j]表示一个布尔值，代表的是“s3 的前 i+j 个字符是否是由s1 的前 i 个字符和s2 的前 j 个字符交错组成的”。
        因为s3是由s1和s2交错组成的，所以s3的末尾必定取自s1的末尾或者s2的末尾。
        dp[i][j] = ( dp[i-1][j] and s1[i-1] == s3[i+j-1] ) or (dp[i][j-1] and s2[[j-1] == s3[i+j-1]] )

        '''
        if len(s1)+len(s2) != len(s3):
            return False
        if len(s1) == len(s2) == len(s3) == 0:
            return True
        col = len(s2) + 1
        row = len(s1) + 1
        dp = [[False]*col for i in range(row)]
        dp[0][0] = True
        for i in range(row):
            for j in range(col):
                if i > 0:
                    dp[i][j] |= ( dp[i-1][j] and s1[i-1] == s3[i+j-1] )
                if j > 0:
                    dp[i][j] |= ( dp[i][j-1] and s2[j-1] == s3[i+j-1] )
        return dp[-1][-1]
