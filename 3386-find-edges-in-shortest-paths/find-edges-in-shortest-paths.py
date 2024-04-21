class Solution:

    def dijkstra(self , source ,  n , adj_list):
        distances = [float("inf") for _ in range(n)]
        distances[source] = 0
        visited = [False for _ in range(n)]
        heap = [(0,source)]
        while heap :
            root_dist , root = heapq.heappop(heap)
            if visited[root] :
                continue
            for node , node_dist in adj_list[root] :
                new_distance = node_dist + root_dist
                if new_distance < distances[node] :
                    distances[node] = new_distance
                    heapq.heappush(heap , (new_distance , node))
            visited[root] = True
        return distances

    # def dfs(self , root , distance , paths , visited , adj_list , shortest_distance , answer , hash_set) :
    #     if root == len(adj_list)-1 :
    #         if distance == shortest_distance :
    #             for i in paths :
    #                 hash_set.add(i)
    #         return
    #     visited[root] = True
    #     for node , node_dist , edge_index in adj_list[root] :
    #         if visited[node] :
    #             continue
    #         paths.add(edge_index)
    #         self.dfs(node , node_dist + distance , paths , visited , adj_list , shortest_distance , answer , hash_set)
    #         paths.remove(edge_index)
    #     visited[root] = False

    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        adj_list = [[] for _ in range(n)]
        for start , end , weight in edges:
            adj_list[start].append((end , weight))
            adj_list[end].append((start , weight))
        source_dist = self.dijkstra(0 , n , adj_list)
        answer = [False for _ in range(len(edges))]
        if source_dist[n-1] == float("inf") :
            return answer
        end_dist = self.dijkstra(n-1 , n , adj_list)
        for i in  range(len(edges)):
            start , end , weight = edges[i]
            if source_dist[start] + weight + end_dist[end] == source_dist[n-1]:
                answer[i] = True
            if source_dist[end] + weight + end_dist[start] == source_dist[n-1]:
                answer[i] = True
        return answer