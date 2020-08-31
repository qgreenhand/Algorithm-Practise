class Solution:
    def maxArea(self, height) :
        '''
        能解决问题的原因是控制了变量
        在这个题目里面有两个变量一个是左右墙体较矮的那个一个是坐标轴长度
        这种方式使得坐标轴始终在减小每次舍去较矮的那个墙
        保证遍历完全不会有更大的可能没有遍历到
        :param height:
        :return:
        '''
        #找最大水池容量“双指针法”
        lenth=len(height)
        i=0
        j=lenth-1
        marea=0
        while j>i:
            area=min(height[i],height[j])*(j-i)
            if area>marea: marea=area
            if height[i]>height[j]:
                j-=1
            else:
                i+=1


        return marea

s=Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))





