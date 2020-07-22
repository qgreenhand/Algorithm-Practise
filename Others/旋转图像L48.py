from typing import List
class Solution:
    '''
    给定一个 n × n 的二维矩阵表示一个图像。
    将图像顺时针旋转 90 度。
    '''

    def rotate(self, matrix: List[List[int]]) -> None:

        """
        Do not return anything, modify matrix in-place instead.
        先转置再换列

        """
        n = len(matrix)
        for i in range(n):
            for j in range(0, i):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
        for j in range(n // 2):
            for i in range(n):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[i][n - 1 - j]
                matrix[i][n - 1 - j] = tmp