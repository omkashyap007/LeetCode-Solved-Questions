class Solution:

    def bfs(self , root , visited , adj_list):
        min_dist = float("inf")
        queue = deque([(root , -1 , 0)])
        visited[root] = True
        distance = {
            root:0 ,
        }
        while queue :
            root , parent , dist = queue.popleft()
            for node in adj_list[root] :
                if visited[node] :
                    if parent == node :
                        continue
                    else :
                        min_dist = min(dist + distance[node] + 1 , min_dist)
                else :
                    distance[node] = dist + 1
                    visited[node] = True
                    queue.append((node , root , dist+1))
        return min_dist



    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        for start , end in edges :
            adj_list[start].append(end)
            adj_list[end].append(start)
        shortest_length = float("inf")
        for i in range(n):
            visited = [False for _ in range(n)]
            shortest_length = min(
                self.bfs(i , visited ,  adj_list ) , 
                shortest_length 
            )
        return -1 if shortest_length == float("inf") else shortest_length