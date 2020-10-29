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

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        官方题解没事重用python写一遍
        为了清晰条件判断分的比较细
        :param nums:
        :return:
        """
        res=[]
        vist=[False]*len(nums)
        nums=sorted(nums)
        def backtrack(havedone):
            if len(havedone)==len(nums):
                res.append(havedone)
                return
            for i in range(len(nums)):
                if i==0 and not vist[i]:
                    vist[0]=True
                    backtrack(havedone+[nums[0]])
                    vist[0]=False
                if i>0 and nums[i]==nums[i-1] and not vist[i] and vist[i-1]:
                    #去重 由于nums已经排过序所以一样的数字都相邻，每次只能相同数中第一个未被取的数
                    vist[i] = True
                    backtrack(havedone + [nums[i]])
                    vist[i] = False
                if i>0 and nums[i]!=nums[i-1] and not vist[i]:
                    vist[i] = True
                    backtrack(havedone + [nums[i]])
                    vist[i] = False
        backtrack([])
        return res




