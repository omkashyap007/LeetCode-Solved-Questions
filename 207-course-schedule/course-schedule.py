class LinkedListNode :
    def __init__(self , data , next = None , prev = None) :
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList :
    
    def __init__(self) :
        self.head = None
        self.tail = None
        self.length = 0
    
    def __len__(self):
        return self.length

    def addAtTail(self , data) :
        node = LinkedListNode(data)
        if not self.head :
            self.head = node
            self.tail = node
        else :
            curr_tail = self.tail
            self.tail = node
            curr_tail.next = self.tail
            self.tail.prev = curr_tail
        self.length += 1

    def deleteAtHead(self) :
        value = None
        if self.head is self.tail :
            value = self.head.data
            self.head = None
            self.tail = None
        else :
            value = self.head.data
            curr_head = self.head
            next_head = self.head.next
            next_head.prev = None
            self.head = next_head
            del curr_head
        self.length -= 1
        return value

class Deque : 

    def __init__(self):
        self.ll = LinkedList()

    def popleft(self) :
        return self.ll.deleteAtHead()

    def append(self , data):
        self.ll.addAtTail(data)

    def __len__(self):
        return len(self.ll)

class Solution:
    def canFinish(self, numCourses: int, edges : List[List[int]]) -> bool:
        indegree = [0 for _ in range(numCourses)]
        adj_list = [[] for _ in range(numCourses)]
        for start , end in edges :
            adj_list[end].append(start)
            indegree[start] += 1
        queue = Deque()
        for i in range(numCourses) :
            if indegree[i] == 0 :
                queue.append(i)
        topo_sort = []
        while len(queue) > 0 : 
            root = queue.popleft()
            topo_sort.append(root)
            for node in adj_list[root] :
                indegree[node] -= 1
                if indegree[node] == 0 :
                    queue.append(node)
        return len(topo_sort) == numCourses