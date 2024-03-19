class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hash_map = {}
        for i in tasks :
            hash_map[i] = hash_map.get(i,0)+1
        time = 0
        heap = []
        for i in hash_map :
            heapq.heappush(heap , (-hash_map[i] , i))
        print(heap)
        queue = deque()
        while heap or queue:
            if queue and time > queue[0][0] :
                _ , task , count = queue.popleft()
                heapq.heappush(heap , (count , task))
            if heap :
                count , task = heapq.heappop(heap)
                count += 1
                if count < 0 :
                    queue.append((time + n , task , count))
            time += 1
        return time
