import random

class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        temp_head = head
        self.arr = []
        while temp_head :
            self.arr.append(temp_head.val)
            temp_head = temp_head.next
        
    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()