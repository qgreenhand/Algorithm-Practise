from typing import List
class Solution:
    '''
    给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
    '''

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        动态规划题
        设dp[i]=1代表前0-(i-1)合法
        dp[i]=dp[j] and if s[j:i] in wordDict
        '''

        lenth = len(s)
        dp = [0] * (lenth + 1)
        dp[0] = 1
        for i in range(1, lenth + 1):
            for j in range(0, i):
                if dp[j] == 1 and s[j:i] in wordDict:
                    dp[i] = 1

        if dp[lenth] == 1:
            return True
        else:
            return False
