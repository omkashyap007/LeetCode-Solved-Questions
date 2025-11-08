class ListNode:
    
    def  __init__(self, key, next=None):
        self.key = key
        self.next = next

class MyHashSet:

    def __init__(self):
        self.hash_key = 10**4
        self.hash_set = [ListNode(0) for _ in range(self.hash_key)]

    def add(self, key: int) -> None:
        hash_index = key % self.hash_key
        node = self.hash_set[hash_index]
        while node.next:
            if node.next.key == key:
                return True
            node = node.next
        node.next = ListNode(key)

    def remove(self, key: int) -> None:
        hash_index = key % self.hash_key
        node = self.hash_set[hash_index]
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return True
            node = node.next


    def contains(self, key: int) -> bool:
        hash_index = key % self.hash_key
        node = self.hash_set[hash_index]
        while node.next:
            if node.next.key == key:
                return True
            node = node.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)