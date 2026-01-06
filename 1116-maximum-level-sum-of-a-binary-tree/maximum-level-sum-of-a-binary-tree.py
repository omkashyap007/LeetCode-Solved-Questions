# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level = 1
        queue = [root]
        max_value = float("-inf")
        min_level = 1
        while queue:
            level_value = 0
            next_queue = []
            for node in queue:
                level_value += node.val
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            if level_value > max_value:
                min_level = level
                max_value = level_value
            level += 1
            queue = next_queue
        return min_level
    