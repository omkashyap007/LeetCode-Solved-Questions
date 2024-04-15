class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        answer = [0]
        def dfs(root , value ) :
            if not root : 
                return 
            value *= 10
            value += root.val
            if not root.left and not root.right :
                answer[0] += value
                return
            dfs(root.left, value)
            dfs(root.right, value)
        dfs(root , 0)
        return answer[0]