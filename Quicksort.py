def Quicksort(nums):
    '''
    旨在实现一个非递归快速排序
    :param nums:
    :return:
    '''
    lenth=len(nums)
    stack=[]        #用栈来保存需要遍历的子集
    stack.append((0,lenth-1))
    while stack:
        stack_tmp=stack.pop()
        start=stack_tmp[0]
        end=stack_tmp[1]
        index,nums=do_sort(start,end,nums)
        if index-1>start:
            stack.append((start,index-1))
        if index+1<end:
            stack.append((index+1,end))
    return nums

def do_sort(start,end,nums):
    '''
    该函数旨在实现一轮开始于start下标结束于end下标的快排
    :param strat:
    :param end:
    :param nums:
    :return:
    '''
    key=nums[start]

    while start<end:
        while  start<end and key<nums[end] :
            end=end-1
        nums[start]=nums[end]
        while start<end and key>=nums[start] :
            start=start+1
        nums[end]=nums[start]
    nums[start]=key
    return start,nums
print(Quicksort([2,1,3,2,8,7]))