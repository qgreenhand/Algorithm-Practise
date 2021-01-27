from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        荷兰三色旗问题解
        给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

        此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

        """
        # 对于所有 idx < p0 : nums[idx < p0] = 0
        # curr是当前考虑元素的下标
        p0 = curr = 0
        # 对于所有 idx > p2 : nums[idx > p2] = 2
        p2 = len(nums) - 1
        while curr <= p2:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1