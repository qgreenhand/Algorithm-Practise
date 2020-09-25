# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    根据一棵树的中序遍历与后序遍历构造二叉树。
    注意:
    你可以假设树中没有重复的元素。
    """
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(in_left, in_right):
            """
            由于是后序遍历顺序为左右根所以要先建右子树再建左子树
            :param in_left:
            :param in_right:
            :return:
            """
            # 如果这里没有节点构造二叉树了，就结束
            if in_left > in_right:
                return None

            # 选择 post_idx 位置的元素作为当前子树根节点
            val = postorder.pop()
            root = TreeNode(val)

            # 根据 root 所在位置分成左右两棵子树
            index = idx_map[val]

            # 构造右子树
            root.right = helper(index + 1, in_right)
            # 构造左子树
            root.left = helper(in_left, index - 1)
            return root

        # 建立（元素，下标）键值对的哈希表
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """
        我写的。。。
        效率很低但是易于理解
        :param inorder:
        :param postorder:
        :return:
        """
        if not inorder or not postorder:
            return None
        root_val = postorder[-1]
        root = TreeNode(root_val)
        index = inorder.index(root_val)
        right_length = (len(inorder) - 1) - index
        left_length = index
        left = right = None
        if right_length > 0:
            right = self.buildTree(inorder[index + 1:], postorder[index:index + right_length])
        if left_length > 0:
            left = self.buildTree(inorder[:left_length], postorder[:left_length])
        root.left = left
        root.right = right
        return root

