from typing import  List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
        candidates 中的数字可以无限制重复被选取。
        :param candidates:
        :param target:
        :return:
        '''
        def do(candidates: List[int], target: int):

            result=[]
            if target<min(candidates):
                return []
            for one in candidates:
                if target<one:
                    continue
                if target==one:
                    result.append([one])
                else :
                    subresult= do(candidates,target-one)
                    #print(subresult,target-one)
                    if subresult:
                        for subone in subresult:
                            if one>=max(subone):
                                subone.append(one)
                                result.append(subone)
                    #print(subresult,target)
            return result
        return do(candidates,target)