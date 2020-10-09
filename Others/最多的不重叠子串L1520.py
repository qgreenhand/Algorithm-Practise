from typing import List
class Solution:
    """
    给你一个只包含小写字母的字符串 s ，你需要找到 s 中最多数目的非空子字符串，满足如下条件：

    这些字符串之间互不重叠，也就是说对于任意两个子字符串 s[i..j] 和 s[k..l] ，要么 j < k 要么 i > l 。
    如果一个子字符串包含字符 char ，那么 s 中所有 char 字符都应该在这个子字符串中。

    """
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        """
        半看答案做的
        1.首先遍历获取每个字母起始终止的下标保存入字典(官方题解写了个类)
        2.然后遍历扩展使每个区间符合要求二
        3.贪心求得最多不重叠区间（按照所有区间的右端进行排序由小到大）
        :param s:
        :return:
        """
        d = dict()
        #1.首先遍历获取每个字母起始终止的下标保存入字典(官方题解写了个类)
        for i in range(len(s)):
            if s[i] not in d.keys():
                d[s[i]] = [i, i]
            else:
                d[s[i]][1] = i

        res = []
        pre = [-1, -1]
        #  2.然后遍历扩展使每个区间符合要求二 这个时间复杂度怕是有点高，，，，
        for kd in d.keys():
            start = d[kd][0]
            end = d[kd][1]
            while start <= end:
                if d[s[start]][0] < d[kd][0] or d[s[start]][1] > d[kd][1]:
                    d[kd][0] = min(d[s[start]][0], d[kd][0])
                    d[kd][1] = max(d[s[start]][1], d[kd][1])
                    start = d[kd][0]
                    end = d[kd][1]
                else:
                    start += 1
        #3.贪心求得最多不重叠区间（按照所有区间的右端进行排序由小到大）
        sorted_d = sorted(d.items(), key=lambda d: d[1][1])
        pre = [-1, -1]
        res = []
        for sd in sorted_d:
            if sd[1][0] < pre[1]:
                continue
            res.append(s[sd[1][0]:sd[1][1] + 1])
            pre = [sd[1][0], sd[1][1]]

        print(d)
        return res