# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    '''
    给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
    你应当保留两个分区中每个节点的初始相对位置。
    '''
    def partition(self, head: ListNode, x: int) -> ListNode:
        head1=ListNode(-1)
        head2=ListNode(-2)
        i=head1
        j=head2
        k=head
        while k:
            if k.val<=x:
                i.next=k
                i=i.next
            else:
                j.next=k
                j=j.next
            k=k.next
        i.next=head2.next
        head2.next=None
        return head1.next