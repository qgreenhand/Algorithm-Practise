# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    二叉搜索树中的两个节点被错误地交换。
    请在不改变其结构的情况下，恢复这棵树。
    主要思路是二叉搜索树的中序遍历是递增的
    """

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        '''
        '''