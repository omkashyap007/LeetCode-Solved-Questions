# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odds = []
        evens = []
        count = 1
        _head = head
        while _head:
            if count %2:
                odds.append(_head.val)
            else:
                evens.append(_head.val)
            _head = _head.next
            count += 1
        t = ListNode(0)
        _t = t
        for i in odds:
            t.next = ListNode(i)
            t = t.next
        for i in evens:
            t.next = ListNode(i)
            t = t.next
        return _t.next