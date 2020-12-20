"""
堆排序
使用顺序表实现，传入参数为一个无序数组
本次堆排序实现旨在实现一个大顶堆
"""


def adjust_Heap(i, nums):
    # i是当前正在进行调整的子树根节点序号
    lenth = len(nums)
    k = i
    while (2 * k + 1 <= lenth - 1):
        if (2 * k + 2 <= lenth - 1) and (nums[2 * k + 1] < nums[2 * k + 2]):
            big_son = 2 * k + 2
        else:
            big_son = 2 * k + 1
        if nums[big_son] > nums[k]:
            tmp = nums[k]
            nums[k] = nums[big_son]
            nums[big_son] = tmp
        else:
            break
        k = big_son


def Heapsort(nums):
    lenth = len(nums)
    result = []
    for i in range(lenth // 2 - 1, -1, -1):
        adjust_Heap(i, nums)

    while nums:
        result.append(nums[0])
        nums[0] = nums[-1]
        nums.pop(-1)
        adjust_Heap(0, nums)
    return result


print(Heapsort([3, 1, 5, 6, 2]))
