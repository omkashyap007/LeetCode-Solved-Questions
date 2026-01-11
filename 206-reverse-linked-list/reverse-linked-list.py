class Solution:
    def f(self, n, t):
        if n.next:
            l = self.f(n.next, t)
            l.next = n
            n.next = None
        else:
            t.next = n
        return n


    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        t = ListNode()
        self.f(head, t)
        return t.next
