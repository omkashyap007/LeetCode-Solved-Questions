class Solution:
    def maximumHappinessSum(self, h: List[int], k: int) -> int:
        x = 0
        h.sort(reverse=True)
        _sum = 0
        for i in range(k):
            val = h[i] - x
            _sum += val if val > 0 else 0 
            x += 1
        return _sum