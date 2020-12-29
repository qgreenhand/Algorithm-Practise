class Solution(object):
    """
    给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
    不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
    """
    def removeDuplicates(self, nums):

        """
        ...
        2020/12/29
        review 挺简单的
        :type nums: List[int]
        :rtype: int
        """

        # Initialize the counter and the second pointer.
        j, count = 1, 1

        # Start from the second element of the array and process
        # elements one by one.
        for i in range(1, len(nums)):

            # If the current element is a duplicate,
            # increment the count.
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                # Reset the count since we encountered a different element
                # than the previous one
                count = 1

            # For a count <= 2, we copy the element over thus
            # overwriting the element at index "j" in the array
            if count <= 2:
                nums[j] = nums[i]
                j += 1

        return j

