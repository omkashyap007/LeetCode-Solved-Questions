class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        a = dummy
        curr = head
        while curr :
            dup = False
            while curr.next and curr.next.val == curr.val :
                dup = True
                curr = curr.next
            t = curr.next
            if not dup :
                dummy.next = curr
                dummy = dummy.next
                dummy.next = None
            curr = t
        return a.next