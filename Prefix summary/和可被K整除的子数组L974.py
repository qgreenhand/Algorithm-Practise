from typing import List
class Solution:
    '''
    给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。
    '''
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        '''
        忙于安卓实在没时间写

        。。。
        2020/09/16  review
        这个题目使用字典用于存储对应的余数值的上一个位置
        '''
        res = 0
        pre_mod = 0  # 存储当前位置的上一个位置的前缀和的余数加上当前位置的值对K的余数
        presum_count = dict()
        presum_count[0] = 1
        for i in range(len(A)):
            pre_mod = (pre_mod + A[i]) % K
            # 下面这行感觉最不好理解
            res += presum_count[pre_mod]  # 如果能在dict中找到相同的pre_mod，说明当前节点前的某个位置的前缀和到当前位置的前缀和间存在若干个K
            presum_count[pre_mod] += 1
        return res