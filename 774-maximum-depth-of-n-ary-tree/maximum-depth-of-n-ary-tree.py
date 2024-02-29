"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        depth = 0
        queue = [root]
        if not root : 
            return 0
        while queue :
            depth += 1
            temp_queue = []
            for node in queue :
                if node and node.children : 
                    temp_queue.extend(node.children)
            queue = temp_queue
        return depth