class Solution:

    def reverseList(self , head):
        prev = None
        while head :
            the_next = head.next
            head.next = prev
            prev = head
            head = the_next
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        odd_even = 0
        thead = head
        while thead :
            odd_even += 1
            thead = thead.next
        if odd_even == 1 :
            return head
        fast = slow = thead = head 
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
        if odd_even %2 == 0 : 
            rev = self.reverseList(slow)
        else : 
            rev = self.reverseList(slow.next)
        while rev :
            if rev.val != thead.val :
                return False
            rev = rev.next
            thead = thead.next
        return True
            