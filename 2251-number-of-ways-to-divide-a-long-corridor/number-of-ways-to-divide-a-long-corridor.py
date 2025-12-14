class Solution:
    def numberOfWays(self, corridor: str) -> int:
        count = 1
        MOD = 10**9 + 7
        _count = 0
        for i in corridor:
            if i == "S":
                _count += 1
        if _count%2 == 1:
            return 0
        indices = [i for i in range(len(corridor)) if corridor[i] == "S"]
        if len(indices) < 2:
            return 0
        if len(indices) == 2:
            return 1
        for i in range(2, len(indices), 2):
            count *= (indices[i]- indices[i-1])
            count %= MOD
        return count%MOD
