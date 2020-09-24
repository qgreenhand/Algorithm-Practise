# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。
    。。。
    有个比较简单的方法。由于二叉搜索树的中序遍历是递增的。所以考虑中序遍历一次后得到递增序列然后hash表对比或者中序遍历同时进行记录
    但是对于O(1)空间复杂度（递归调用消耗除外）需要使用Morris方法
    """
    def findMode(self, root: TreeNode) -> List[int]:
        """
        Morris方法
        :param root:
        :return:
        """
