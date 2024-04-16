class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1  : return TreeNode(val , left = root)
        a = root
        queue = [root]
        level = 1
        for _ in range(depth-2) :
            temp_queue = []
            for node in queue :
                if node.left :
                    temp_queue.append(node.left)
                if node.right : 
                    temp_queue.append(node.right)
            queue = temp_queue
        for node in queue :
            node.left = TreeNode(val , left = node.left) 
            node.right = TreeNode(val , right = node.right)
        return a
                