class Solution:
    def maximumHappinessSum(self, h: List[int], k: int) -> int:
        x = 0
        h.sort(reverse=True)
        _sum = 0
        for i in range(k):
            val = h[i]
            val -= x
            if val > 0:
                _sum += val
            x += 1
        return _sum