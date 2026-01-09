class Solution:

    def dfs(self, root, p, q):
        if not root:
            return None
        
        if root.val == p.val or root.val == q.val:
            return root
        
        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)

        if left and right:
            return root
        return left or right

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dfs(root, p, q)
