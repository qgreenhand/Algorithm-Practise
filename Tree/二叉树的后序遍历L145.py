# Definition for a binary tree node.
from typing import  List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def postorder(root):
            res = []
            stack = list()
            stack.append([root, 1])
            while stack:
                cur = stack.pop()
                if cur[0] and cur[1] == 1:
                    stack.append([cur[0], 0])
                    stack.append([cur[0].right, 1])
                    stack.append([cur[0].left, 1])
                elif cur[0] and cur[1] == 0:
                    res.append(cur[0].val)
            return res

        res = postorder(root)
        return res
