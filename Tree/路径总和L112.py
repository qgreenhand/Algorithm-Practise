# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    '''
    给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
    蛮简单的就直接递归深搜
    '''
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        if root == None:
            return False
        if root.left == None and root.right == None:
            return root.val == sum

        left = self.hasPathSum(root.left, sum - root.val)
        right = self.hasPathSum(root.right, sum - root.val)
        return left or right