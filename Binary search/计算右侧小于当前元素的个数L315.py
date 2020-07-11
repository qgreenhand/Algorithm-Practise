class Solution:
    '''
    给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。
    输入: [5,2,6,1]
    输出: [2,1,1,0]
    '''

    def countSmaller(self, nums: List[int]) -> List[int]:
        '''
        不会做
        他用的二分法
        大概就是维持一个数组qq从后往前遍历每次用二分法得到应该插入的下标这个下标即为比他小的值个数
        然后插入
        我觉得这个插入可能会产生较大时间复杂度
        那个官网题解没看懂
        '''

        if not nums:
            return []

        N = len(nums)
        dp = [0] * N
        dp[-1] = 0
        qq = [nums[-1]]
        for i in range(N - 2, -1, -1):
            l = 0
            r = len(qq)
            while l < r:
                m = (r + l) // 2
                if qq[m] < nums[i]:
                    l = m + 1
                else:
                    r = m
            # print(qq,l,nums[i])
            dp[i] = l
            qq.insert(l, nums[i])
        return dp