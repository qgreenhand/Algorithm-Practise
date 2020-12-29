from typing import  List
class Solution:
    """
    字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。返回一个表示每个字符串片段的长度的列表。
    """

    def partitionLabels(self, S: str) -> List[int]:
        """
        唉多简单的一道题居然还是看了答案
        。。。。
        2020/12/29
        review 卧槽还是看答案了而且还看了好长时间

        :param S:
        :return:
        """
        last = [-1] * 26
        for i, s in enumerate(S):
            last[ord(s) - ord('a')] = max(last[ord('s') - ord('a')], i)
        print(last)
        start = 0
        end = 0
        res = []
        for i, s in enumerate(S):
            end = max(last[ord(s) - ord('a')], end)
            if end == i:
                res.append(end - start + 1)
                start = end + 1
        return res