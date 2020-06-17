from typing import List
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        '''
        最长有效括号数
        考虑采用动态规划
        :param s:
        :return:
        '''
        lenth=len(s)
        '''
        dp=[[0]*lenth for _ in range(lenth)]  #考虑i表示起始j表示结束下标dp[i][j]表示其中的连续有效括号
        for i in range(lenth-1):
            for j in range(i+1,lenth):
        '''
        '''
        看官方题解，只需要一个一维数组即可，其中第 i个元素表示以下标为 i 的字符结尾的最长有效子字符串的长度。
        还有种用栈的方法更简单
        '''
        dp=[0]*lenth
        result=0
        for i in range(lenth):
            if s[i]=='(' or i==0:          #以（结尾的不会是有效括号
                continue
            else:
                if s[i-1]=='(':    #型如...（）
                    if i==2:        #防止数组溢出
                        dp[i] = 2
                    else:
                        dp[i] = dp[i - 2] + 2
                elif i-dp[i-1]>0 and s[i-dp[i-1]-1]=='(':               #型如...))
                    dp[i]=dp[i-1]+dp[i-dp[i-1]-2]+2
            result=max(result,dp[i])
        return result



s=Solution()
print(s.longestValidParentheses(")("))