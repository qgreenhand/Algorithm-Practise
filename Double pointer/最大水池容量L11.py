class Solution:
    """
    给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
    在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。
    找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
    """
    def maxArea(self, height):
        """
        能解决问题的原因是控制了变量
        在这个题目里面有两个变量一个是左右墙体较矮的那个一个是坐标轴长度
        这种方式使得坐标轴始终在减小每次舍去较矮的那个墙
        保证遍历完全不会有更大的可能没有遍历到
        。。。
        review 2020/12/01
        :param height:
        :return:
        """
        # 找最大水池容量“双指针法”
        lenth = len(height)
        i = 0
        j = lenth - 1
        marea = 0
        while j > i:
            area = min(height[i], height[j]) * (j - i)
            if area > marea: marea = area
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1

        return marea


s = Solution()
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
