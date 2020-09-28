
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next



class Solution:
    """
    给定一个二叉树填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL
    """
    def connect(self, root: 'Node') -> 'Node':
        """
        这个题目一看就是层序遍历啊。。。
        ...
        采用常数空间方法
        额。。。看了官方题解思路
        由于上一层已经建立了next指针故可以利用一下。。。
        就不用建立队列了
        。。。
        怎么说呢写的太繁琐了，再写的话用虚拟头节点为每个层建立一个虚拟头会简单很多
        """
        upHead = None
        upHead = root
        pre = None
        upPointer = upHead
        nextFloor = None
        if not root:
            return None
        if root.left:
            nextFloor = root.left
        elif root.right:
            nextFloor = root.right
        while nextFloor:
            nextFloor = None
            pre = None
            while upPointer:
                if upPointer.left:
                    if pre:
                        pre.next = upPointer.left
                        print(pre.val, upPointer.left.val)
                    pre = upPointer.left
                    if not nextFloor:
                        nextFloor = upPointer.left

                if upPointer.right:
                    if pre:
                        pre.next = upPointer.right
                        print(pre.val, upPointer.right.val)
                    pre = upPointer.right
                    if not nextFloor:
                        nextFloor = upPointer.right
                upPointer = upPointer.next
            upPointer = nextFloor

        return root