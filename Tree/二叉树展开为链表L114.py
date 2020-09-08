# Definition for a binary tree node.
class TreeNode:
   def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
Do not return anything, modify root in-place instead.
"""
'''
考虑采用递归方法每个使左子树转到右子树最后一个节点
不行这个题结果必须先序遍历的单链表。。。
if root==None:
    return None
tmp=root
while(tmp.right): 
    tmp=tmp.right
if root.left:

    tmp.right=root.left
root.left=None
self.flatten(root.right)
'''


class Solution:
    '''
    给定一个二叉树，原地将它展开为一个单链表。
    '''

    def flatten(self, root: TreeNode) -> None:
        '''
        每次从栈内弹出一个节点作为当前访问的节点，获得该节点的子节点，如果子节点不为空，则依次将右子节点和左子节点压入栈内（注意入栈顺序）。
        展开为单链表的做法是，维护上一个访问的节点 prev，每次访问一个节点时，令当前访问的节点为 curr，将 prev 的左子节点设为 null 以及将 prev的右子节点设为 curr，
        然后将 curr 赋值给 prev，进入下一个节点的访问，直到遍历结束。需要注意的是，初始时 prev 为 null，只有在 prev 不为null 时才能
        对 prev 的左右子节点进行更新。

        '''
        if not root:
            return

        stack = [root]
        prev = None

        while stack:
            curr = stack.pop()
            if prev:
                prev.left = None
                prev.right = curr
            left, right = curr.left, curr.right
            if right:
                stack.append(right)
            if left:
                stack.append(left)
            prev = curr
