class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(root , the_sum) :
            if not root :
                return
            if root.left :
                if not root.left.left and not root.left.right :
                    the_sum[0] += root.left.val
                else :
                    dfs(root.left , the_sum)
            if root.right :
                dfs(root.right , the_sum)
        the_sum = [0]
        dfs(root ,the_sum)
        return the_sum[0]