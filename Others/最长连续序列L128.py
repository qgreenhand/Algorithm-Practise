class Solution:
    def longestConsecutive(self, nums):
        '''
        给定一个未排序的整数数组，找出最长连续序列的长度。
        要求算法的时间复杂度为 O(n)。
        使用哈希表，建议看收藏题解中另一个较为好懂这个也蛮好懂
        '''
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak