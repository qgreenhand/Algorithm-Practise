class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
class Solution:
    '''
    没啥好说的快慢指针让快指针先走k步
    '''
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        former, latter = head, head
        for _ in range(k):
            former = former.next
        while former:
            former, latter = former.next, latter.next
        return latter

