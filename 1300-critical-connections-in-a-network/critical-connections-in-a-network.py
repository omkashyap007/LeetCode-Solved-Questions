class Solution:

    time = 1

    def dfs(self , node , parent , visited , adj_list , insertion_time , lowest_time , bridges) :
        visited[node] = True
        insertion_time[node] = lowest_time[node] = self.time
        self.time += 1
        for adj in adj_list[node] :
            if adj == parent :
                continue
            if not visited[adj] :
                self.dfs(adj , node , visited , adj_list , insertion_time , lowest_time , bridges ) 
                lowest_time[node] = min(lowest_time[node] , lowest_time[adj])
                if lowest_time[adj] > insertion_time[node] :
                    bridges.append((adj,node))
            else :
                lowest_time[node] = min(lowest_time[node] , lowest_time[adj])


                

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj_list = [[] for _ in range(n)]
        for start , end in connections :
            adj_list[start].append(end)
            adj_list[end].append(start)
        visited = [False for _ in range(n)]
        insertion_time = [float("inf") for _ in range(n)]
        lowest_time    = [float("inf") for _ in range(n)]
        bridges = []
        self.dfs(0 ,-1 , visited , adj_list, insertion_time , lowest_time , bridges)
        return bridges