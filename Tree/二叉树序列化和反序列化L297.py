# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    """
    请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
    先序遍历保留空节点为‘|’
    主要思想也是这个保留空节点就可以通过先序遍历获取
    另外后序中序以及BFS应该也可以
    。。。。。
    2020/11/12
    好烦啊就记得怎么序列化了
    这个题目比较重要，感觉面经经常看到

    """

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return '|,'  # 加上逗号是为了防止负数产生bug
        left_str = self.serialize(root.left)
        right_str = self.serialize(root.right)
        return str(root.val) + ',' + left_str + right_str

    def rdeserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        now = data[0]
        if now == '|':
            data.pop(0)
            return None

        root = TreeNode(int(now))
        data.pop(0)
        root.left = self.rdeserialize(data)
        root.right = self.rdeserialize(data)
        return root

    def deserialize(self, data):
        data = data.split(',')
        return self.rdeserialize(data)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
