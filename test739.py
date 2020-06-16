from typing import List
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        '''
        根据每日 气温 列表，请重新生成一个列表，对应位置的输入是你需要再等待多久温度才会升高超过该日的天数。
        如果之后都不会升高，请在该位置用 0 来代替。
        这种方法使用栈，使栈顶向栈底是从小到大的，还有种是建立一个长度为温度变化范围的辅助数组。
        :param T:
        :return:
        '''
        result=[0]*len(T)
        stack=[]
        stack.append(len(T)-1)

        for i in range(len(T)-2,-1,-1):
            '''
            if T[stack[-1]]>T[i]:
                result[i]=stack[-1]-i
                stack.append(i)
            else:
            '''

            while  stack and T[stack[-1]]<=T[i]: #这里and前后两个条件不要调换
                stack.pop()
            if stack:
                result[i]=stack[-1]-i
            stack.append(i)
        return result

s=Solution()
print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))

