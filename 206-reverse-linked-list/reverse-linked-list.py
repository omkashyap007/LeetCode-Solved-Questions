class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t = None
        if not head:
            return head
        def f(n):
            nonlocal t
            if n.next:
                l = f(n.next)
                l.next = n
                n.next = None
            else:
                t = n
            return n
        f(head)
        return t
