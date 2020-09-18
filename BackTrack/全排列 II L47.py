from typing import List
class Solution:
    '''
    给定一个可包含重复数字的序列，返回所有不重复的全排列。
    '''
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        '''
        最初想法。。。
        由于他这个存在重复字符我考虑使用一个hash表用于存储每个字符的个数准备采用字典存储
        然后采用回溯法。。。
        。。。
        这个方法的话。。。内存耗费实在太高了但是很容易就想得到
        '''
        hashTable=dict()
        for i in nums:
            if i in hashTable:
                hashTable[i]+=1
            else:
                hashTable[i]=1
        res=[]
        def backTrack(hashTable,haveBuild):
            if not hashTable:
                nonlocal res
                res.append(haveBuild)
                return
            for k in list(hashTable.keys()):
                tmp=haveBuild[:]
                tmp.append(k)
                newTable=hashTable.copy()
                newTable[k]-=1
                if newTable[k]<=0:
                    newTable.pop(k)
                backTrack(newTable,tmp)
        backTrack(hashTable,[])
        return res