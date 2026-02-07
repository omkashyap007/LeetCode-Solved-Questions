class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_count = 0
        b = []
        a = [0 for _ in range(len(s))]
        a_count = 0
        for i in range(len(s)):
            b.append(b_count)
            if s[i] == "b":
                b_count += 1
        a_count = 0
        for i in range(len(s)-1, -1, -1):
            a[i] = a_count
            if s[i] == "a":
                a_count += 1
        answer = len(s)
        for i in range(len(s)):
            answer = min(a[i]+b[i], answer)
        return answer        
