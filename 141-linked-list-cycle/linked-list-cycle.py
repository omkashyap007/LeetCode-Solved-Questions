# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow = head
        fast = head.next
        found = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                found = True
                break
        return found