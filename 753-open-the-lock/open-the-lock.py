class Solution:

    def string(self , l) :
        return "".join(l)

    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        start = ["0" , "0" , "0" , "0"]
        if self.string(start) in deadends : 
            return -1
        level = 0
        queue = deque([start])
        while queue :
            for _ in range(len(queue)) :
                root = queue.popleft()
                if self.string(root) == target : 
                    return level
                if self.string(root) in deadends :
                    continue
                deadends.add(self.string(root))
                for i in range(4) :
                    char = root[i]
                    add = root.copy()
                    add[i] = "0" if char == "9" else str(int(char)+1)
                    # if self.string(add) not in deadends :
                    queue.append(add)
                    sub = root.copy()
                    sub[i] = "9" if char == "0" else str(int(char)-1)
                    # if self.string(sub) not in deadends :
                    queue.append(sub)
            level += 1
        return -1