class Solution:
    """
    一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
    机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
    现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
    网格中的障碍物和空位置分别用 1 和 0 来表示。

    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        比较简单的动态规划

        :param obstacleGrid:
        :return:
        """
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[0]*n for i in range(0,m)]
        dp[0][0]=1
        for i in range(0,m):
            for j in range(0,n):

                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                else:
                    if i==0 and j!=0:
                        dp[i][j] = dp[i][j-1]
                    if i!=0 and j==0:
                        dp[i][j] = dp[i-1][j]
                    if i!=0 and j!=0:
                        dp[i][j]=dp[i-1][j]+dp[i][j-1]


        return dp[m-1][n-1]