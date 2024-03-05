class Solution:

    def isBipartite(self , adj_list , visited , colors , node):
        colors[node] = 0
        visited[node] = True
        queue = deque([node])
        while queue :
            node = queue.popleft()
            nodeColor = colors[node]
            newColor = 0 if nodeColor == 1 else 1
            for neighbor in adj_list[node] :
                if visited[neighbor] :
                    if colors[neighbor] == nodeColor :
                        return False
                else :
                    visited[neighbor] = True
                    colors[neighbor] = newColor
                    queue.append(neighbor)
        return True



    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(n+1)]
        node = None
        for x ,y  in dislikes :
            adj_list[x].append(y)
            adj_list[y].append(x)
            node = x
        visited = [False for _ in range(n+1)]
        colors = [-1 for _ in range(n+1)]
        for i in range(n+1):
            if not visited[i] :
                if not self.isBipartite(adj_list , visited , colors , i) :
                    return False
        return True