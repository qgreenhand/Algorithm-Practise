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
    def isPalindrome(self, head: ListNode) -> bool:
        """
        卧槽看到了一个nb的解法。
        直接hash方法
        hash=hash*seed+val
        seed为一个质数val为当前节点值
        那么
        考虑正向 hash1=a[1]*seed^(n-1)+a[2]*seed^(n-2)+....+a[n]*seed^0
        考虑反向 hash2=a[1]*seed^0    +a[2]*seed^1    + ...+a[n]*seed^(n-1)
        若hash1==hash2则可以确定回文链成立
        :param head:
        :return:
        """
        cur=head
        hash1=0
        hash2=0
        seed=(int)(1e9 + 7)
        h=1
        while cur:
            hash1=hash1*seed+cur.val
            hash2=hash2+h*cur.val
            h*=seed
            cur=cur.next
        return hash1==hash2
