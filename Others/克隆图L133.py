
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors


class Solution(object):
    '''
    给你无向 连通 图中一个节点的引用，请你返回该图的 深拷贝（克隆）。
    图中的每个节点都包含它的值 val（int） 和其邻居的列表（list[Node]）。

    '''

    '''
    刚开始看题目没看懂
    应该是返回一个一模一样的无向图可以用DFS或者BFS
    需要搞一个哈希表用于防止重复访问具体如下
    '''
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return node

        # 如果该节点已经被访问过了，则直接从哈希表中取出对应的克隆节点返回
        if node in self.visited:
            return self.visited[node]

        # 克隆节点，注意到为了深拷贝我们不会克隆它的邻居的列表
        clone_node = Node(node.val, [])

        # 哈希表存储
        self.visited[node] = clone_node

        # 遍历该节点的邻居并更新克隆节点的邻居列表
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return clone_node

