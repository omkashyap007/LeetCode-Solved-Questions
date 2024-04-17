class Solution:

    def dfs(self , root , array , answer) :
        array.append(chr(ord("a")+root.val))
        if not root.left and not root.right :
            string = "".join(array[::-1])
            print(string)
            if answer[0] == None :
                answer[0] = string
            else :
                answer[0] = min(answer[0] , string)
        if root.left :
            self.dfs(root.left , array , answer)
        if root.right :
            self.dfs(root.right , array , answer)
        array.pop()

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        answer = [None]
        self.dfs(root , [] , answer)
        return answer[0]