class Solution:

    def dfs(self , root , height , val , depth) :
        if not root  : return 
        if height + 1 == depth :
            node = TreeNode(val)
            l = root.left
            root.left = node
            node.left = l
            node = TreeNode(val)
            r = root.right
            node.right = r
            root.right = node
            return

        else :
            self.dfs(root.left , height+1 , val , depth)
            self.dfs(root.right , height+1 , val , depth)

    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:return TreeNode(val , left  = root)
        self.dfs(root , 1 , val , depth)
        return root