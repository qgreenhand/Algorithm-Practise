class Solution:
    '''
    给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，并且这些子字符串中的所有0和所有1都是组合在一起的。
    重复出现的子串要计算它们出现的次数。
    '''
    def countBinarySubstrings(self, s: str) -> int:
        '''
        特殊方法，采用count数组存储0或1连续出现的个数
        如  001101001 就是 2 2 1 1 2 1
        这样每次考虑count i和j 的时候 答案就是min(i,j)
        如  2 1 1 1 1
        '''
        # 统计counts数组
        counts = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] == s[i]:
                j += 1

            counts.append(j - i)
            i = j
        # 计算结果
        ans = 0
        for i in range(len(counts) - 1):
            ans += min(counts[i], counts[i+1])
        return ans