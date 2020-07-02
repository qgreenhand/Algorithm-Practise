from typing import List

class Solution:
    '''
    给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
    请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。
    '''
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        '''
        我想可以取n个指针然后每个放在第i行每次取最小的指针往前进一

        '''
        n = len(matrix)
        pointers = [0] * n
        res = 0

        for epoch in range(k):
            min_index = -1
            min_num = float('inf')
            for i in range(n):
                # 找出最小的准备前进的
                if pointers[i] < n and min_num > matrix[i][pointers[i]]:
                    min_num = matrix[i][pointers[i]]
                    min_index = i
            res = matrix[min_index][pointers[min_index]]
            pointers[min_index] += 1
        return res

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        '''
        二分做法
        :param matrix:
        :param k:
        :return:
        '''
        n = len(matrix)

        def check(mid):
            i, j = n - 1, 0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num >= k

        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left
