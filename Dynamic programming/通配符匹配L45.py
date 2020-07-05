class Solution:
    '''
    给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
    和L10 正则表达式匹配一样比它稍微简单点
    '''

    def isMatch(self, s: str, p: str) -> bool:
        '''
        动态规划做法

        '''
        m, n = len(s), len(p)
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        # 初始状态 如果两个均为空则True
        #        如果s为空则除非p均为* 否则为False
        #        如果s不空p为空则为False
        dp[0][0] = True
        for i in range(1, n + 1):
            if p[i - 1] == '*':
                dp[i][0] = True
            else:
                break

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[i - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif s[j - 1] == p[i - 1] or p[i - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[n][m]