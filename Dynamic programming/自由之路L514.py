class Solution:
    """
    给定一个字符串 ring，表示刻在外环上的编码；给定另一个字符串 key，表示需要拼写的关键词。您需要算出能够拼写关键词中所有字符的最少步数。
    最初，ring 的第一个字符与12:00方向对齐。您需要顺时针或逆时针旋转 ring 以使 key 的一个字符在 12:00 方向对齐，然后按下中心按钮，以此逐个拼写完 key 中的所有字符。

    """
    def findRotateSteps(self, ring: str, key: str) -> int:
        """
        这题名字我很喜欢

        这题用动态规划
        实际上其实是记忆化搜索，有点像dfs
        困难题但是实际上好像没那么难，但是我还是看了眼题解才做出来的
        dp[i][j]表示当前的字符为key[i] ring的位置为j的时候（当key[i]==ring[j]的时候有效）
        使用一个位置字典用于存储有效位置
        :param ring:
        :param key:
        :return:
        """
        pos = dict()
        for i, r in enumerate(ring):

            if r not in pos:
                pos[r] = [i]
            else:
                pos[r].append(i)
        # 表示当前遍历到第i个key
        dp = [[float('inf')] * len(ring) for _ in range(len(key))]

        for j in pos[key[0]]:
            dp[0][j] = min(j, len(ring) - j) + 1
        for i in range(1, len(key)):
            for j in pos[key[i]]:
                for k in pos[key[i - 1]]:
                    dp[i][j] = min(dp[i][j], min(abs(k - j), abs(len(ring) - abs(k - j))) + dp[i - 1][k] + 1)
        return min(dp[len(key) - 1])