from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
        我的做法
        :param n:
        :return:
        """
        result = []

        def output(done: str, remain_L, remain_R):
            """
            我考虑插入右括号的时候只要左括号数大于右括号就行了
            :param done:
            :param remain_L:
            :param remain_R:
            :return:
            """
            if remain_R == 0:
                result.append(done)
                return 0
            if remain_L > 0:
                output(done + '(', remain_L - 1, remain_R)
            if remain_R > remain_L:
                output(done + ')', remain_L, remain_R - 1)

        output("", n, n)
        return result

    def generateParenthesis1(self, n: int) -> List[str]:
        """
        看官网上的题解试图使用动态规划的方法
        。。。。
        2020/11/11
        实际上是记忆化搜索啊
        :param n:
        :return:
        """

        def output(number):
            result = []
            if number == 1:
                return ['()']
            if number == 0:
                return ['']
            for i in range(number):
                p = output(i)
                q = output(number - 1 - i)
                for one_p in p:
                    for one_q in q:
                        result.append('(' + one_p + ')' + one_q)
            return result

        return output(n)


s = Solution()
print(s.generateParenthesis1(3))
