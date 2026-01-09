# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        child_parent_map = {}
        queue = [(root, None)]
        while queue:
            new_queue = []
            for node, parent in queue:
                child_parent_map[node] = parent
                if node.left:
                    new_queue.append((node.left, node))
                if node.right:
                    new_queue.append((node.right, node))
            queue = new_queue
        hash_set = set()
        while p:
            hash_set.add(p)
            p = child_parent_map[p]
        while q:
            if q in hash_set:
                return q
            q = child_parent_map[q]
            