class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def MorrisInorder(root: TreeNode):
    """
    中序遍历二叉树（Morris方法）
    这种方法的话主要是采用一个pre指针
    用pre指针建立子树最右下和当前子树root节点的关系

    :param root:
    :return:
    """
    curr = root
    pre = None
    while curr:
        if not curr.left:
            print(curr.val)  # 若不存在左子树则打印根节点,将curr指向右子树
            curr = curr.right
        else:
            pre = curr.left
            while pre.right and pre.right != curr:  # 找到左子树的最右下节点用于和当前树的根节点建立线索
                pre = pre.right
            if pre.right:  # 这代表左子树遍历完毕(pre.right==cur)，遍历根节点并使线索置空
                # 这里是到了左子树的右下节点时候curr=curr.right又顺着之前的线索绕回来了
                # 这一步应该是防止重复遍历若pre.right==curr则代表这个curr的左子树实际遍历过了所以线索置空
                pre.right = None
                print(curr.val)
                curr = curr.right
            else:  # 设置线索
                pre.right = curr
                curr = curr.left
