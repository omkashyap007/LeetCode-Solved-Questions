class Solution:

    def dfs(self , root , destination , array , adj_list , visited , answer):
        if root == destination :
            answer.append(array.copy())
            return
        for node in adj_list[root] :
            if not visited[node] :
                visited[node] = True
                array.append(node)
                self.dfs(node , destination , array , adj_list , visited , 
                answer)
                array.pop()
                visited[node] = False
        return

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        answer = []
        visited = [False for _ in range(len(graph))]
        visited[0] = True
        self.dfs(0 , len(graph)-1 ,  [0] , graph , visited ,  answer)
        return answer