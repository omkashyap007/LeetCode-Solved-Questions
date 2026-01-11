from heapq import heappush, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in nums:
            if len(heap) < k:
                heappush(heap, i)
            else:
                if heap[0] < i:
                    heappop(heap)
                    heappush(heap, i)
        return heap[0]
