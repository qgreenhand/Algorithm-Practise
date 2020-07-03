 #Definition for a binary tree node.
from typing import List
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    '''
    将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
    本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
    '''


    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        '''
        刚看感觉挺难想想这tm不就是找有序数组中点吗？。。
        '''
        n=len(nums)
        if n==0:
            return None
        root=TreeNode(nums[(n-1)//2])
        root.left=self.sortedArrayToBST(nums[:(n-1)//2])
        root.right=self.sortedArrayToBST(nums[(n-1)//2+1:])
        return root