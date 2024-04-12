"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hash_map = {}
        def createNode(node) :
            if not node : 
                return None
            if node.val in hash_map :
                return hash_map[node.val]
            clone = Node(node.val)
            hash_map[node.val] = clone
            for neighbor in node.neighbors :
                clone.neighbors.append(createNode(neighbor))
            return clone
        createNode(node)
        if not node :
            return None
        return hash_map[node.val]
        # visited = [False for _ in range()]
        # def dfs(node) :
        #     clone = hash_map[node.val] 
        #     for neighbor in node.neighbors :
        #         clone.neighbors.append(dfs(neighbor))
        #     return clone
        # clone = dfs(node)
        # return clone
