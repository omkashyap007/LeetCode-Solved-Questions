class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        adj_list = [[] for _ in range(n)]
        for i , j in edges :
            adj_list[i].append(j)
            adj_list[j].append(i)
        restricted = set(restricted)
        queue = deque([0])
        count = 0
        visited = [False for _ in range(n)]
        if 0 in restricted :
            return 0
        visited[0] = True
        while queue : 
            root = queue.popleft()
            count += 1
            for node in adj_list[root] :
                if node in restricted or visited[node] :
                    continue
                visited[node] = True
                queue.append(node)
        return count