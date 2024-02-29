class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        level = 0
        queue = deque([root])
        while queue :
            prev_val = None
            temp_queue = []
            for node in queue :
                if level%2 == 0 :
                    if node.val%2 == 0 :
                        return False
                    if prev_val != None :
                        if prev_val >= node.val :
                            return False
                else :
                    if node.val%2 == 1 :
                        return False
                    if prev_val != None :
                        if prev_val <= node.val :
                            return False
                prev_val = node.val
                if node.left :
                    temp_queue.append(node.left)
                if node.right :
                    temp_queue.append(node.right)
            level += 1
            queue = temp_queue
        return True
    