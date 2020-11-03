class Solution:
    """
    统计只差一个字符的子串数目
    """

    def countSubstrings(self, s: str, t: str) -> int:
        """
        不会做。。。看了答案
        :param s:
        :param t:
        :return:
        """
        s_len = len(s)
        t_len = len(t)
        # dp1用来储存以i，j为下标的只差一个字符的字串数目
        dp1 = [[0] * t_len for _ in range(s_len)]
        # dp2用来储存以i，j为下标的相同后缀数目
        dp2 = [[0] * t_len for _ in range(s_len)]
        """
        dp1[i][j]=dp2[i-1][j-1]+1 (s[i]!=t[j])
        dp2[i][j]=0
        
        dp1[i][j]=dp1[i-1][j-1]   (s[i]==t[j])
        dp2[i][j]=dp2[i-1][j-1]+1
        """
        res = 0
        for i in range(s_len):
            for j in range(t_len):
                if s[i] == t[j]:
                    if i == 0 or j == 0:
                        dp1[i][j] = 0
                        dp2[i][j] = 1
                    else:
                        dp1[i][j] = dp1[i-1][j-1]
                        dp2[i][j] = dp2[i-1][j-1]+1
                else:
                    if i == 0 or j == 0:
                        dp1[i][j] = 1
                        dp2[i][j] = 0
                    else:
                        dp1[i][j] = dp2[i-1][j-1]+1
                        dp2[i][j] = 0
                res += dp1[i][j]
        return res