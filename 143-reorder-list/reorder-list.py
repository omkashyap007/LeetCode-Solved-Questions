class Solution:

    def reverseList(self , head):
        prev = None
        while head :
            the_next = head.next
            head.next = prev
            prev = head
            head = the_next
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head : 
            return None
        if not head.next : 
            return head
        dummy = ListNode(0, head)
        prev = dummy
        slow = fast = head
        thead = head
        while fast and fast.next :
            prev = slow
            if fast.next.next :
                fast = fast.next.next
            else : 
                fast = fast.next
            slow = slow.next
        prev.next = None
        rev = self.reverseList(slow)
        del dummy
        dummy = ListNode(0)
        temp = dummy
        while head  and rev :
            dummy.next = head
            head = head.next
            dummy = dummy.next
            dummy.next = rev
            rev = rev.next
            dummy = dummy.next
        if head :
            dummy.next = head
        if rev : 
            dummy.next = rev
        return temp