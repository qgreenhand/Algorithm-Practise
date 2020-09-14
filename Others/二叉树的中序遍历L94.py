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
        卧槽这个中序遍历不会写了
        """
        if not root:
            return []
        stack = []
        res = []
        curr = None
        if root.left:
            curr = root.left
        stack.append(root)
        while stack:

            while curr:  # 遍历到最左下
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()

            res.append(curr.val)
            curr = curr.right

        return res