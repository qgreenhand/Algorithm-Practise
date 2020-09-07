from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        题目可以采用L215的方式加上一个hash表用于存储出现次数
        当然也可使用堆排序方式加上hash表
        :param nums:
        :param k:
        :return:
        '''