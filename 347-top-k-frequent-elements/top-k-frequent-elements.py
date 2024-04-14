class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for i in nums :
            hash_map[i] = hash_map.get(i,0)+1
        heap = []
        for i in hash_map :
            heapq.heappush(heap , (-hash_map[i] , i))
        answer = []
        while heap and k > 0 :
            answer.append(heapq.heappop(heap)[1])
            k -= 1
        return answer