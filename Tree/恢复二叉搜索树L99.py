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
        changed_1=TreeNode()
        changed_2=TreeNode()
        pre=TreeNode()
        def DFS(root:TreeNode):#中序遍历采用一个pre来保存遍历状态
            if not root.left:
                DFS(root.left)
            nonlocal pre
            nonlocal changed_1
            nonlocal changed_2
            if pre.val>root.val and not changed_1:
                changed_1=pre
            if pre.val>root.val and changed_1:
                changed_2=root
            pre=root
            if not root.right:
                DFS(root.right)
        tmp=changed_1
        changed_1=changed_2
        changed_2=tmp

