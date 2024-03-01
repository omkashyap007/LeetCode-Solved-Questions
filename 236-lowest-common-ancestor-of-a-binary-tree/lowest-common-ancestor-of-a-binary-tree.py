class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root : 
            return None
        if root == p or root == q :
            return root
        left = self.lowestCommonAncestor(root.left , p , q)
        right = self.lowestCommonAncestor(root.right , p , q)
        if not left :
            return right
        if not right :
            return left
        if left and right :
            return root
            