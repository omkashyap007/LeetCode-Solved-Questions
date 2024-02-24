class Solution:

    def manhattanDistance(self , first , second):
        return abs(first[0]-second[0]) + abs(first[1]-second[1])        

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj_list = [[] for _ in range(len(points))]
        for i in range(len(points)):
            for j in range(i+1 , len(points)):
                distance = self.manhattanDistance(points[i],points[j])
                adj_list[i].append((j,distance))
                adj_list[j].append((i,distance))
        heap = [(0 , 0 )]   
        dist_sum = 0
        visited = [False for _ in range(len(points))]
        while heap : 
            dist , root = heapq.heappop(heap)
            if visited[root] :
                continue
            visited[root] = True
            dist_sum += dist
            for node, node_dist in adj_list[root] :
                if not visited[node] :
                    heapq.heappush(heap , (node_dist , node))
        return dist_sum
