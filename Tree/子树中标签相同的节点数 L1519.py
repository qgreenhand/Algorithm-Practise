from typing import List
class Solution:
    '''
    给你一棵树（即，一个连通的无环无向图），这棵树由编号从 0  到 n - 1 的 n 个节点组成，且恰好有 n - 1 条 edges 。树的根节点为节点 0 ，树上的每一个节点都有一个标签，也就是字符串 labels 中的一个小写字符（编号为 i 的 节点的标签就是 labels[i] ）
    边数组 edges 以 edges[i] = [ai, bi] 的形式给出，该格式表示节点 ai 和 bi 之间存在一条边。
    返回一个大小为 n 的数组，其中 ans[i] 表示第 i 个节点的子树中与节点 i 标签相同的节点数。
    '''

    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        """
        怎么说呢我tm理解错了这个是无向图第一个不代表是第二个的父节点
        算了这个反正逻辑差不多不改了
        :param n:
        :param edges:
        :param labels:
        :return:
        """
        res = [0] * n

        def help(root, edges):
            return_res = dict()
            return_res[labels[root]] = 1
            for i in edges:
                if i[0] == root:
                    subdict = help(i[1], edges)
                    for k in subdict.keys():
                        if k in return_res.keys():
                            return_res[k] += subdict[k]
                        else:
                            return_res[k] = subdict[k]
            nonlocal res
            res[root] = return_res[labels[root]]

            return return_res

        help(0, edges)
        return res

