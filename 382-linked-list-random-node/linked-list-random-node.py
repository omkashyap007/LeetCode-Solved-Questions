import random

class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.length = 0
        temp_head = self.head
        while temp_head:
            self.length += 1
            temp_head = temp_head.next

    def getRandom(self) -> int:
        random_index = random.randint(1 ,self.length)
        temp_head = self.head
        curr_index = 1
        while temp_head :
            if curr_index == random_index :
                return temp_head.val
            curr_index += 1
            temp_head = temp_head.next

        
        
