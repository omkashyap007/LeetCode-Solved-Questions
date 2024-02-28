class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        value = root.val
        while queue :
            temp_queue = []
            for node in queue :
                if node.left :
                    temp_queue.append(node.left)
                if node.right : 
                    temp_queue.append(node.right)
            if temp_queue :
                value = temp_queue[0].val
            queue = temp_queue
        return value