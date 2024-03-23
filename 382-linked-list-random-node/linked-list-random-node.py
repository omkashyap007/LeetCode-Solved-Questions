import random

class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.BIG_VALUE = 10**9+7

    def getRandom(self) -> int:
        random_index = random.randint(0 , self.BIG_VALUE)
        temp_head = self.head
        curr_index = 0
        while temp_head :
            if curr_index == random_index :
                return temp_head.val
            curr_index += 1
            temp_head = temp_head.next
        random_index %= curr_index
        temp_head = self.head
        curr_index = 0
        while temp_head :
            if curr_index == random_index :
                return temp_head.val
            curr_index +=1 
            temp_head = temp_head.next
        