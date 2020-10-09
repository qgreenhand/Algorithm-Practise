from typing import List
class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        d = dict()
        for i in range(len(s)):
            if s[i] not in d.keys():
                d[s[i]] = [i, i]
            else:
                d[s[i]][1] = i

        res = []
        pre = [-1, -1]
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