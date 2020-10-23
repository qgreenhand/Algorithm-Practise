# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        请判断一个链表是否为回文链表。
        :param head:
        :return:
        """
        # 要求O(n)时间复杂度和O(1)空间复杂度
        # 我想干脆先遍历得到有多少个再把前一半逆序链表然后遍历。。。。
        #.....
        #看题解找中间节点时可以用快慢指针的方法
        lenth = 0
        cur = head
        while cur:
            cur = cur.next
            lenth += 1

        left = (lenth - 1) // 2

        # 逆序链表
        pre = None
        cur = head
        for i in range(left + 1):
            ncur = cur.next
            cur.next = pre
            pre = cur
            cur = ncur

        if lenth % 2 == 0:
            li = pre
            ri = cur
        else:
            li = pre.next
            ri = cur
        while li and ri:

            if li.val != ri.val:
                return False
            li = li.next
            ri = ri.next
        return True

