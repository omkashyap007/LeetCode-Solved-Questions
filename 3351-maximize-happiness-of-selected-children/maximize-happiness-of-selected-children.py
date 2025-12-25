class Solution:
    def maximumHappinessSum(self, h: List[int], k: int) -> int:
        h = [-1*i for i in h]
        heapq.heapify(h)
        x = 0
        _sum = 0
        for _ in range(k):
            val = -1*(heapq.heappop(h))
            val -= x
            if val > 0:
                _sum += val
            else:
                break
            x += 1
        return _sum


