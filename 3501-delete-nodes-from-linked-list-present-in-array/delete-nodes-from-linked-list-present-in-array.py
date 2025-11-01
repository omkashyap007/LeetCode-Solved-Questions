# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode(0, None)
        return_head = new_head
        nums = set(nums)
        while head:
            if head.val not in nums:
                new_head.next = head
                new_head = new_head.next
            head = head.next
        new_head.next = None
        return return_head.next
