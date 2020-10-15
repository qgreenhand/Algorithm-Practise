"""
给你一个字符串 s ，请你拆分该字符串，并返回拆分后唯一子字符串的最大数目。
字符串 s 拆分后可以得到若干 非空子字符串 ，这些子字符串连接后应当能够还原为原字符串。但是拆分出来的每个子字符串都必须是唯一的 。
"""
class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        """
        这道题目直接用回溯我是没想到的
        但是回溯算法我感觉我理解的一直不大清楚
        这个干脆做个模板来看
        :param s:
        :return:
        """
        def backtrack(index: int, split: int):
            if index >= length:
                nonlocal maxSplit
                maxSplit = max(maxSplit, split)
            else:
                for i in range(index, length):
                    substr = s[index:i+1]
                    if substr not in seen:
                        #下面这个部分是回溯算法通用的
                        seen.add(substr)
                        backtrack(i + 1, split + 1)
                        seen.remove(substr)

        length = len(s)
        seen = set()
        maxSplit = 1
        backtrack(0, 0)
        return maxSplit

