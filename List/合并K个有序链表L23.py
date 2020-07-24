# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    '''
    合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

    '''

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        '''
        这次用的每次取每个链表头最小的那个
        这个题目可以用分治法但是时间复杂度会比较高
        '''
        head = ListNode()
        tmp = head
        for one in lists:
            if one == []:
                lists.remove(one)
        while lists:
            min_node = None
            for one in lists:
                if one:
                    min_node = one
                    min_val = min_node.val
                    break
            if min_node == None:
                break

            for one in lists:
                if one:
                    if min_val >= one.val:
                        min_val = one.val
                        min_node = one
                else:
                    lists.remove(one)
            tmp.next = min_node
            tmp = tmp.next
            lists.remove(min_node)
            min_node = min_node.next
            if min_node:
                lists.append(min_node)
        return head.next