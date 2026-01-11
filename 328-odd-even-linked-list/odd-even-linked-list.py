# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode()
        _odd = odd
        even = ListNode()
        _even = even
        _head = head
        count = 1
        while _head:
            if count % 2:
                odd.next = _head
                odd = odd.next
            else:
                even.next = _head
                even = even.next
            count += 1
            _head = _head.next
        even.next = None
        odd.next = _even.next
        return _odd.next
