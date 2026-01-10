class Solution:

    def dfs(self, root):
        if not root:
            return None, 0
        
        left_node, left_height = self.dfs(root.left)
        right_node, right_height = self.dfs(root.right)

        if left_height == right_height:
            return root, 1 + left_height
        elif left_height > right_height:
            return left_node, 1 + left_height
        else:
            return right_node, 1 + right_height
        

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.dfs(root)[0] 