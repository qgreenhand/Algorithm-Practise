from typing import List
class Solution:
    '''
    给出一个区间的集合，请合并所有重叠的区间。
    '''
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        newlist=sorted(intervals,key=lambda a:a[0])
        print(intervals)
        answer=[]
        for i in newlist:
            if answer == []:
                answer.append(i)
            elif answer[-1][1]>=i[0]:
                answer[-1][1]=max(i[1],answer[-1][1])
            else:
                answer.append(i)
        return answer