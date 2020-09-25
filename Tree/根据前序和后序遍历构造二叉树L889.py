# Definition for a binary tree node.
from typing import  List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    返回与给定的前序和后序遍历匹配的任何二叉树。
    """
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        """
        算是做个练习
        没有任何优化，优化的话可以采用hash表来把"left_length = post.index(pre[1]) + 1"优化掉
        :param pre:
        :param post:
        :return:
        """
        if not pre or not post:
            return None
        left = None
        right = None

        root_val = pre[0]
        root = TreeNode(root_val)
        if len(pre) == 1:
            return root
        left_length = post.index(pre[1]) + 1
        right_length = len(post) - 1 - left_length
        if left_length > 0:
            left = self.constructFromPrePost(pre[1:left_length + 1], post[:left_length])
        if right_length > 0:
            right = self.constructFromPrePost(pre[left_length + 1:], post[left_length:left_length + right_length])
        root.left = left
        root.right = right
        return root
