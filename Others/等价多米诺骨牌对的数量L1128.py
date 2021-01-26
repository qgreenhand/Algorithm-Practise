from typing import  List
class Solution:
    """
    给你一个由一些多米诺骨牌组成的列表 dominoes。
    如果其中某一张多米诺骨牌可以通过旋转 0 度或 180 度得到另一张多米诺骨牌，我们就认为这两张牌是等价的。
    形式上，dominoes[i] = [a, b] 和 dominoes[j] = [c, d] 等价的前提是 a==c 且 b==d，或是 a==d 且 b==c。
    在 0 <= i < j < dominoes.length 的前提下，找出满足 dominoes[i] 和 dominoes[j] 等价的骨牌对 (i, j) 的数量。

    1 <= dominoes.length <= 40000
    1 <= dominoes[i][j] <= 9

    """
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        """
        由于元素都小于10 使用二元组表示时可以用二位整数来代替hash表
        :param dominoes:
        :return:
        """

        num = [0] * 100
        ret = 0
        for x, y in dominoes:
            val = (x * 10 + y if x <= y else y * 10 + x)
            ret += num[val]
            num[val] += 1
        return ret

