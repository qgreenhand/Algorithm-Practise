class Solution:
    '''
    给定两个数组，编写一个函数来计算它们的交集。
    '''
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        这种方法采用先排序再两个数组每个指针遍历的方法
        还可以直接hash
        :param nums1:
        :param nums2:
        :return:
        '''
        nums1.sort()
        nums2.sort()

        length1, length2 = len(nums1), len(nums2)
        intersection = list()
        index1 = index2 = 0
        while index1 < length1 and index2 < length2:
            if nums1[index1] < nums2[index2]:
                index1 += 1
            elif nums1[index1] > nums2[index2]:
                index2 += 1
            else:
                intersection.append(nums1[index1])
                index1 += 1
                index2 += 1

        return intersection

