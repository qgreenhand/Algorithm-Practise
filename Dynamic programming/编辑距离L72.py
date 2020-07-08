class Solution:
    '''
    给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
    你可以对一个单词进行如下三种操作：
    插入一个字符
    删除一个字符
    替换一个字符


    '''
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        动态规划方法
        dp[i,j]表示第一个字符串以i下标结尾的字串和第二个字符串以j下标结尾字串之间的编辑距离
        :param word1:
        :param word2:
        :return:
        '''
        m=len(word1)+1
        n=len(word2)+1
        dp=[[0]*n for _ in range(m)]
        for i in range(0,m):
            for j in range(0,n):
                if i == 0 :
                    dp[i][j]=j
                elif j == 0:
                    dp[i][j]=i
                else:
                    '''
                    如果此时两个字符相等的话那么为dp[i][j]=dp[i-1][j-1]
                    不然有两种情况，分别是更改和添加来使两个字符一样
                    添加则为 dp[i-1][j]+1和dp[i][j-1]+1
                    更改则为 dp[i-1][j-1]+1
                    '''
                    if word1[i-1]==word2[j-1]:
                        dp[i][j]=dp[i-1][j-1]
                    else:
                        dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+1)
        return dp[m-1][n-1]