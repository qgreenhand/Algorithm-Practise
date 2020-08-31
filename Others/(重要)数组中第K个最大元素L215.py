from typing import List
class Solution:
    '''
    在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素
    '''

    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        快速选择算法
        由于快排每次选的曲轴最后位置即为最后在排序数组中的位置
        所以当曲轴位置i>k则取i-1作为新曲轴
        否则取i+1
        如果等于k代表找到了
        '''
        def one_quicksort(start, end, nums: List):
            '''
            用来进行一轮快排，返回值为完成后的下标
            '''
            key = nums[start]
            i = start
            j = end
            while i < j:
                while nums[j] >= key:
                    j -= 1
                    '''
                    防止重复的数造成死循环
                    '''
                    if i == j:
                        break

                nums[i] = nums[j]
                while nums[i] < key:
                    i += 1
                    if i == j:
                        break

                nums[j] = nums[i]
            nums[i] = key

            return i

        end = len(nums) - 1
        start = 0
        index = 0
        while True:
            index = one_quicksort(start, end, nums)
            if len(nums) - index < k:
                end = index - 1

            elif len(nums) - index > k:
                start = index + 1

            else:
                break
        return nums[index]
