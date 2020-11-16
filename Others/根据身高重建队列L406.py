from typing import List
class Solution:
    """
    假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，
    其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。
    编写一个算法来重建这个队列。
    :param people:
    :return:
    """
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """
        。。。不会做
        看了官方题解
        1. 首先按照身高为第一要素 逆序排位 为第二要素 排序
        2. 设置一个大小为n的数组
        3. 如果来了一个p[1]=k 的 则代表它的前面应该有k个比他大的，所以它的前面应该有k个空位
        :param people:
        :return:
        """
        people.sort(key=lambda x: (x[0], -x[1]))
        n = len(people)
        ans = [[] for _ in range(n)]
        for person in people:
            spaces = person[1] + 1
            for i in range(n):
                if not ans[i]:
                    spaces -= 1
                    if spaces == 0:
                        ans[i] = person
                        break
        return ans

