# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    '''
    给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。
    。。。
    虽然是个简单题但是爷做了好久啊。。。有将近半小时
    '''
    def convertBST(self, root: TreeNode) -> TreeNode:
        """
        由于是二叉搜索树，所以很明显每个节点的右子树都大于该节点
        每个节点的左子树都小于该节点
        另外，一个节点所有先辈节点和先辈节点的右子树均大于该节点
        考虑先更新右子树和根节点然后再更新左子树
        换而言之使用先右再根再左的遍历顺序
        """
        def dfs_changed(root: TreeNode,pre_value) -> int:
            '''
            先右再根再左的dfs,返回值为右子树的值
            pre_value为父节点的值,只有左子树需要右子树无需(右子树参数置0)
            。。。
            右子树并不是无需pre_value,因为虽然右子树值都大于根节点但是不大于爷爷节点和爷爷节点的右子树
            然后返回值不能是右子树根节点的值，得是右子树的和
            '''
            if not root:
                return 0
            #print(root.val,pre_value)
            right_value=dfs_changed(root.right,pre_value)
            right_sum=right_value+root.val                                  #定一个right_sum用来储存dfs的节点和,放在这里是为了防止下一行把root.val修改了
            root.val=root.val+right_value+pre_value
            left_value=dfs_changed(root.left,root.val)
            right_sum=right_sum+left_value
            return right_sum
        dfs_changed(root,0)
        return root