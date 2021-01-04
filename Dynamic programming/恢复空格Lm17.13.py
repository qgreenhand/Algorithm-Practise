from typing import List


class Solution:
    """
    哦，不！你不小心把一个长篇文章中的空格、标点都删掉了，并且大写也弄成了小写
    像句子"I reset the computer. It still didn’t boot!"已经变成了"iresetthecomputeritstilldidntboot"。
    在处理标点符号和大小写之前，你得先把它断成词语。当然了，你有一本厚厚的词典dictionary，不过，有些词没在词典里。
    假设文章用sentence表示，设计一个算法，把文章断开，要求未识别的字符最少，返回未识别的字符数。

    """

    def respace(self, dictionary: List[str], sentence: str) -> int:
        """
        动态规划解决
        主要就是当遍历到字母dp[i]考察sentence[i-j:i]在不在字典里面如果在的话就dp[i]=dp[i-j]
        把字典里面每个单词都试一遍找到最小的可能
        如果不在就dp[i]=dp[i-1]+1
        。。。
        2021.1.4 review
        :param dictionary:
        :param sentence:
        :return:
        """
        if sentence == "":
            return 0
        if not dictionary:
            return len(sentence)

        dp = [0] * (len(sentence) + 1)
        for i in range(1, len(sentence) + 1):
            dp[i] = dp[i - 1] + 1
            for j in dictionary:
                if len(j) > i:
                    continue
                if sentence[i - len(j): i] == j:
                    dp[i] = min(dp[i], dp[i - len(j)])
        return dp[-1]
