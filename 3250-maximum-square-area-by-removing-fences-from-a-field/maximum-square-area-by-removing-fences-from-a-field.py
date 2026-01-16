class Solution:
    def maximizeSquareArea(self, m: int, n: int, h: List[int], v: List[int]) -> int:
        h.append(1)
        h.append(m)
        v.append(1)
        v.append(n)
        h.sort()
        v.sort()
        MOD = 10**9 + 7
        h_set = set()
        v_set = set()
        answer = -1
        for i in range(len(h)-1):
            for j in range(i+1, len(h)):
                h_set.add(h[j] - h[i])
        
        for i in range(len(v)-1):
            for j in range(i+1, len(v)):
                v_set.add(v[j] - v[i])

        for i in h_set:
            if i in v_set:
                a = i*i
                answer = max(a, answer)
        return answer if answer == -1 else answer % MOD
