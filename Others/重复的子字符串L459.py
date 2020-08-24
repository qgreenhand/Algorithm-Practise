class Solution:
    '''
    给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。
    '''
    def repeatedSubstringPattern(self, s: str) -> bool:
        '''
        我们将两个 s 连在一起，并移除第一个和最后一个字符。如果 s 是该字符串的子串，那么 s 就满足题目要求。
        感觉1很巧妙注意看充分性证明
        '''
        return (s + s).find(s, 1) != len(s)

