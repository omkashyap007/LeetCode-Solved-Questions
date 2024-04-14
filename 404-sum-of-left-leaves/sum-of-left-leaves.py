class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        the_sum = 0
        queue = [root]
        while queue : 
            temp_queue = []
            for node in queue : 
                if node.left :
                    if not node.left.left and not node.left.right :
                        the_sum += node.left.val
                    else :
                        temp_queue.append(node.left)
                if node.right : 
                    temp_queue.append(node.right)
            queue = temp_queue
        return the_sum        