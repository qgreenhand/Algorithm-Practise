# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    给定一个链表，如果它是有环链表，实现一个算法返回环路的开头节点。
    有环链表的定义：在链表中某个节点的next元素指向在它前面出现过的节点，则表明该链表存在环路。
    """

    def detectCycle(self, head: ListNode) -> ListNode:
        """
        快慢指针
        找到结合点的办法为meet点和头节点移动相同距离再次相遇点即为结合点
        :param head:
        :return:
        """
        slow = head
        fast = head
        meet = None
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                meet = fast
                break
        index = head
        if meet == None:
            return None
        while True:
            if index == meet:
                return meet
            index = index.next
            meet = meet.next
        return -1
