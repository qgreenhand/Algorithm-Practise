# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    给你二叉树的根节点 root 和一个整数 distance 。
    如果二叉树中两个 叶 节点之间的 最短路径长度 小于或者等于 distance ，那它们就可以构成一组 好叶子节点对 。
    返回树中 好叶子节点对的数量 。
    """

    def countPairs(self, root: TreeNode, distance: int) -> int:
        """
        做这种题目思路要清晰。。。唉又看了答案
        1. 首先题目提示distance<10这样我们就可以用一个长度为10的数组保存当前子树的好节点候选数
        比如a[i]代表距离当前节点i的叶子节点个数
        2. 一个树中好节点可以是子树的好节点对也可以是最近公共祖先为当前根节点的叶子节点对
        3. 用DFS方式返回distance数组，和子树的好节点对。用distance数组来计算根节点为公共祖先可以产生的好节点对
        :param root:
        :param distance:
        :return:
        """

        def dfs(root,distance)->(List[int],int):
            """

            :param root: root指当前根节点
            :param distance:
            :return: 返回一个列表指示叶子节点到当前根节点的距离情况
                     返回一个整数指示当前子树的好节点对个数
            """
            right_depth=left_depth=depth=[0]*(distance+1)
            right_res=left_res=0
            if not root.left and not root.right:
                #当前节点为叶子节点
                depth[0]=1
                return (depth,0)
            if  root.left:
                left_depth,left_res=dfs(root.left,distance)
            if  root.right:
                right_depth,right_res=dfs(root.right,distance)

            #更新当前depth数组
            for i in range(1,distance+1):
                depth[i]=depth[i]+left_depth[i-1]+right_depth[i-1]
            #最近公共祖先为当前节点的可能对
            res=0
            #注意这里遍历的上下界
            for i in range(distance):
                for j in range(distance-i-1):
                    res+=right_depth[i]*left_depth[j]
            #子树结果
            res+=left_res+right_res
            return (depth,res)
        d,res=dfs(root,distance)
        return res

