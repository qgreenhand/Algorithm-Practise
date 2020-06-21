# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        '''
        给定一个非空二叉树，返回其最大路径和。
        本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
        注意他这个是任意节点而非任意叶子节点，所以添加了第25-28行
        :param root:
        :return:
        '''
        maxsum=float('-inf')
        def DFS(root: TreeNode):
            if root==None:
                return 0
            left_max=DFS(root.left)
            right_max=DFS(root.right)
            nonlocal maxsum
            maxsum=max(maxsum,left_max+right_max+root.val)  #经过root
            if max(left_max,right_max)+root.val>0:          #可能和小于0不如废弃它返回0
                return max(left_max,right_max)+root.val
            else:
                return 0
        DFS(root)
        return maxsum