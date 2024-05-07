class Solution:

    def reverseList(self , head):
        prev = None
        while head :
            the_next = head.next
            head.next = prev
            prev = head
            head = the_next
        return prev

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num = 0
        thead = head
        while thead :
            num *= 10
            num += thead.val
            thead = thead.next
        if num == 0 :
            return head
        num *= 2 # 378
        dummy = ListNode()
        d = dummy
        while num : 
            rem = num%10 # 8
            num = num//10
            dummy.next = ListNode(rem)
            dummy = dummy.next
        return self.reverseList(d.next)
