# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        用迭代算法
        采用栈作为信息保存数据结构
        """
        if not root:
            return []
        stack=[]
        res=[]
        curr=root
        while stack or curr:
            while curr:                       #遍历到最左下
                stack.append(curr)
                curr=curr.left
            curr=stack.pop()
            res.append(curr.val)
            curr=curr.right
        return res