class Solution:
    def numSub(self, s: str) -> int:
        rem = 10**9 + 7
        i = 0
        c = 0
        answer = 0
        while i < len(s):
            if s[i] == "0":
                i += 1
                c = 0
            else:
                j = i
                while j < len(s) and s[j] == "1":
                    c += 1
                    j += 1
                answer += ((c*(c+1))//2)
                answer %= rem
                i = j
        return answer%rem
    