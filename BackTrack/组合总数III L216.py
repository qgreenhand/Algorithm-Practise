from typing import List
class Solution:
    """
    找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
    """
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """
        题目感觉和前面组合总数一应该没啥区别，let me try
        。。。果然没啥区别算了写着玩
        """
        resultList=list()
        def dfs(index,target,k,res):
            if target==0 and k==0:
                nonlocal resultList
                resultList.append(res)
                return
            if index>9:
                return
            dfs(index+1,target,k,res)      #不考虑当前数
            newres=res[:]
            newres.append(index)
            if k>=1:
                dfs(index+1,target-index,k-1,newres) #考虑当前数
        dfs(1,n,k,[])
        return resultList