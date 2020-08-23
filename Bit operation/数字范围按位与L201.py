class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        '''
        给定范围 [m, n]，其中 0 <= m <= n <= 2147483647，返回此范围内所有数字的按位与（包含 m, n 两端点）。
        说实话没看懂。。。。
        把转化为公共前缀
        现在太忙了以后再看


        '''
        shift = 0
        # 找到公共前缀
        while m < n:
            m = m >> 1
            n = n >> 1
            shift += 1
        return m << shift
