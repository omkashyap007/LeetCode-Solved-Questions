class Solution:
    def numberOfWays(self, c: str) -> int:
        count = 1
        MOD = 10**9 + 7
        old_i = 0
        s = 0
        _count = 0
        if len(c) < 2:
            return 0
        for i in c:
            if i == "S":
                _count += 1
        if _count %2 == 1:
            return 0
        for i in range(len(c)):
            if c[i] == "P":
                continue
            if c[i] == "S":
                s += 1
            if s == 2:
                old_i = i
            if  s == 3:
                count *= (i-old_i)
                count %= MOD
                s = 1
        return count %MOD if s != 0 else 0


